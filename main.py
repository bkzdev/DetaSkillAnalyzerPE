import os
import shutil
import json
from datetime import datetime
from PIL import Image, ImageChops
from ocr_util import perform_ocr  # OCR関数をインポート
import re

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_files_to_directory(files, destination, test_mode):
    ensure_directory(destination)
    for file in files:
        shutil.copy(file, destination)
        if not test_mode:
            os.remove(file)

def compare_and_crop_images(image1_path, image2_path, output_path, test_mode):
    try:
        print(f"Comparing images: {image1_path} and {image2_path}")
        image1 = Image.open(image1_path).convert("RGB")
        image2 = Image.open(image2_path).convert("RGB")

        diff = ImageChops.difference(image1, image2)
        if test_mode:
            gray = diff.convert("L")
            gray = gray.point(lambda x: 0 if x < 10 else x)   # 値が230以下は0になる
            diff.show(title="Difference Image")
            gbbox = gray.getbbox()
            print(f"Bounding box for difference: {gbbox}")
            gray = image2.crop(gbbox)
            gray.save(output_path)

        bbox = diff.convert("L").point(lambda x: 0 if x < 10 else x).getbbox() #グレスケ化⇒10以下で二値化⇒bbox取得
        print(f"Bounding box for difference: {bbox}")

        if bbox:
            cropped = image2.crop(bbox)
            cropped.save(output_path)
            print(f"Cropped image saved to: {output_path}")
        else:
            print("No difference found. Skipping cropping.")
    except Exception as e:
        print(f"Error during image comparison and cropping: {e}")

def replace_multiple_in_file(file_path, replacements, test_mode):
    # ファイルを読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 各パターンに対して置換を実行
    for pattern, replacement in replacements.items():
        print(f"pattern: {pattern}, replacement: {replacement}")
        content = re.sub(pattern, replacement, content)

    # 置換後の内容でファイルを上書き
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # config.json読み込み
    config = load_config("config.json")

    input_dir = config["Paths"]["InputDirectory"]
    output_dir = config["Paths"]["OutputDirectory"]
    ArchiveDirectoryName = config["Paths"]["ArchiveDirectoryName"]
    ocr_output_file = config["Paths"]["OCROutputFile"]
    timestamp_flag = config["Settings"]["UseTimestampDirectory"]
    test_flag = config["Settings"]["TestMode"]
    print(f"input_dir: {input_dir}")
    print(f"output_dir: {output_dir}")
    print(f"ocr_output_file: {ocr_output_file}")
    print(f"timestamp_flag: {timestamp_flag}")
    print(f"test_flag: {test_flag}")

    #置換パターン取得
    replacements = {}
    for i in range(1, len(config['replacements']) + 1):
        pattern_key = f'pattern{i}'
        replacement_key = f'replace{i}'
        if pattern_key in config['replacements'] and replacement_key in config['replacements_values']:
            pattern = config['replacements'][pattern_key]
            replacement = config['replacements_values'][replacement_key]
            replacements[pattern] = replacement

    # inputディレクトリ作成
    ensure_directory(input_dir)

    # outputディレクトリ作成
    if timestamp_flag:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_dir = os.path.join(output_dir, timestamp)
    ensure_directory(output_dir)

    archive_dir = os.path.join(output_dir, ArchiveDirectoryName)

    # inputfileリスト取得
    input_files = sorted([os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))])
    if len(input_files) < 4:
        raise ValueError("入力ディレクトリには4枚の画像が必要です。")

    # アーカイヴディレクトリに移動
    move_files_to_directory(input_files, archive_dir, test_flag)

    # アーカイヴのリスト取得
    archive_files = sorted([os.path.join(archive_dir, f) for f in os.listdir(archive_dir) if f.endswith(('.png', '.jpg', '.jpeg'))])

    # 画像比較の前に1つめの画像をトリミングして保存
    if archive_files:
        with Image.open(archive_files[0]) as img:
            cropped = img.crop((180, 216, 180 + 256, 216 + 122))
            cropped_filename = f"{timestamp}_{config['OutputFiles']['icon']}"
            cropped.save(os.path.join(output_dir, cropped_filename))
            print(f"Cropped image saved to: {os.path.join(output_dir, cropped_filename)}")

    # 画像比較
    output_files = []
    for i, second in enumerate(archive_files[1:5], start=2):
        output_file_name = f"{timestamp}_{config['OutputFiles'][f'Skill{i - 1}']}"
        output_path = os.path.join(output_dir, output_file_name)
        print(f"Processing pair: {archive_files[0]} and {second}")
        compare_and_crop_images(archive_files[0], second, output_path, test_flag)
        output_files.append(output_path)

    # OCR利用フラグ判定
    use_ocr = config["Settings"].get("UseOCR", False)
    if use_ocr:
        with open(os.path.join(output_dir, ocr_output_file), "w", encoding="utf-8") as ocr_file:
            for output_file in output_files:
                ocr_result = perform_ocr(output_file)
                ocr_file.write(ocr_result + "\n\n")
        #OCR結果ファイルを置換
        replace_multiple_in_file(os.path.join(output_dir, ocr_output_file), replacements, test_flag)
    else:
        print("OCR機能は利用しません。")


if __name__ == "__main__":
    main()
