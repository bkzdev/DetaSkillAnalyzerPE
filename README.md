
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ゲーム情報抽出ツール インフォグラフィック</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', 'Noto Sans JP', sans-serif;
            background-color: #f8fafc;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        .flow-arrow {
            font-size: 2.5rem;
            color: #F9A826;
            line-height: 1;
        }
    </style>
</head>
<body class="text-gray-800">

    <!-- Color Palette: Energetic & Playful -->
    <div class="container mx-auto p-4 md:p-8">

        <header class="text-center my-8 md:my-12">
            <h1 class="text-4xl md:text-5xl font-black text-gray-900 tracking-tight">
                ゲームアセット抽出ツール
            </h1>
            <p class="mt-4 text-lg md:text-xl text-gray-600 max-w-3xl mx-auto">
                スクリーンショットから必要な情報だけを瞬時に切り出す。面倒な手作業はもう不要です。
            </p>
        </header>

        <main>
            <!-- Section 1: Process Flow -->
            <section class="mb-16 md:mb-24">
                <h2 class="text-3xl font-bold text-center mb-8">自動化の3ステップ</h2>
                <div class="flex flex-col md:flex-row items-center justify-center gap-4 md:gap-8 text-center">
                    <div class="bg-white rounded-lg shadow-lg p-6 w-full md:w-1/4">
                        <div class="text-5xl mb-3">📥</div>
                        <h3 class="text-xl font-bold text-gray-900">1. インプット</h3>
                        <p class="text-gray-600 mt-2">キャラとスキル画面のスクショをアップロード</p>
                    </div>
                    <div class="flow-arrow transform md:-translate-y-2 rotate-90 md:rotate-0">→</div>
                    <div class="bg-white rounded-lg shadow-lg p-6 w-full md:w-1/4">
                        <div class="text-5xl mb-3">⚙️</div>
                        <h3 class="text-xl font-bold text-gray-900">2. 解析・抽出</h3>
                        <p class="text-gray-600 mt-2">AIが画像内の重要領域を自動で特定・切り出し</p>
                    </div>
                    <div class="flow-arrow transform md:-translate-y-2 rotate-90 md:rotate-0">→</div>
                    <div class="bg-white rounded-lg shadow-lg p-6 w-full md:w-1/4">
                        <div class="text-5xl mb-3">🖼️</div>
                        <h3 class="text-xl font-bold text-gray-900">3. アウトプット</h3>
                        <p class="text-gray-600 mt-2">アイコンとスキル情報が個別の画像として完成</p>
                    </div>
                </div>
            </section>

            <!-- Section 2: Before and After -->
            <section class="mb-16 md:mb-24">
                <h2 class="text-3xl font-bold text-center mb-8">抽出プロセスの詳細</h2>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
                    <div class="bg-white p-6 rounded-lg shadow-lg">
                        <h3 class="text-2xl font-bold mb-4 text-center">インプット: 煩雑なスクリーンショット</h3>
                        <p class="text-center text-gray-600 mb-6">ツールはこれらの4枚のフルスクリーンショットから必要な部分だけを認識します。</p>
                        <div class="grid grid-cols-2 gap-4">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\input_archive\Screenshot_2025.07.03_01.13.01.576.png" alt="キャラクターステータスのスクリーンショット" class="rounded-md shadow-md w-full h-auto">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\input_archive\Screenshot_2025.07.03_01.13.03.239.png" alt="スキル1詳細のスクリーンショット" class="rounded-md shadow-md w-full h-auto">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\input_archive\Screenshot_2025.07.03_01.13.04.763.png" alt="スキル2詳細のスクリーンショット" class="rounded-md shadow-md w-full h-auto">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\input_archive\Screenshot_2025.07.03_01.13.06.126.png" alt="スキル3詳細のスクリーンショット" class="rounded-md shadow-md w-full h-auto">
                        </div>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-lg">
                        <h3 class="text-2xl font-bold mb-4 text-center">アウトプット: 整理された情報</h3>
                        <p class="text-center text-gray-600 mb-6">不要な部分が削ぎ落とされ、共有や管理がしやすい4つのアセットが生成されます。</p>
                        <div class="grid grid-cols-2 gap-4">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\20250703011619_icon.png" alt="抽出されたキャラクターアイコン" class="rounded-md shadow-md w-full h-auto">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\20250703011619_skill1.png" alt="抽出されたスキル1の情報" class="rounded-md shadow-md w-full h-auto">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\20250703011619_skill2.png" alt="抽出されたスキル2の情報" class="rounded-md shadow-md w-full h-auto">
                            <img src="C:\MovieMaker\ProjectD\20250626_cos\image\20250703011619\20250703011619_skill3.png" alt="抽出されたスキル3の情報" class="rounded-md shadow-md w-full h-auto">
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Section 3: Benefits -->
            <section>
                <h2 class="text-3xl font-bold text-center mb-12">ツールの主な利点</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- Benefit 1: Efficiency -->
                    <div class="bg-white p-6 rounded-lg shadow-lg">
                        <h3 class="text-2xl font-bold mb-4 text-center">圧倒的な効率化</h3>
                        <p class="text-center text-gray-600 mb-6">手作業によるトリミングと比較して、作業時間を90%以上削減。このグラフは、手作業（赤）とツール利用時（黄）の作業時間の割合を示しています。</p>
                        <div class="chart-container">
                            <canvas id="timeSavedChart"></canvas>
                        </div>
                    </div>

                    <!-- Benefit 2 & 3 -->
                    <div class="space-y-8">
                        <div class="bg-white p-6 rounded-lg shadow-lg flex items-center gap-6">
                            <div class="text-5xl">🔗</div>
                            <div>
                                <h3 class="text-xl font-bold">共有の容易さ</h3>
                                <p class="text-gray-600 mt-1">SNSや攻略サイトで、要点をまとめた画像を手軽に共有できます。</p>
                            </div>
                        </div>
                        <div class="bg-white p-6 rounded-lg shadow-lg flex items-center gap-6">
                            <div class="text-5xl">📁</div>
                            <div>
                                <h3 class="text-xl font-bold">情報管理の簡素化</h3>
                                <p class="text-gray-600 mt-1">キャラクタービルドや構成の記録を、整理された形式で保存できます。</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <footer class="text-center mt-16 md:mt-24 py-8 border-t border-gray-200">
            <p class="text-gray-500">ゲームプレイを、もっとスマートに。</p>
        </footer>
        
    </div>

    <!-- Confirmation: NEITHER Mermaid JS NOR SVG were used. All diagrams and icons are implemented with HTML/CSS and Unicode characters. Charts are rendered on Canvas via Chart.js. -->

    <script>
        function wrapText(str, len) {
            const words = str.split(' ');
            const lines = [];
            let currentLine = '';

            words.forEach(word => {
                if ((currentLine + ' ' + word).length > len && currentLine.length > 0) {
                    lines.push(currentLine);
                    currentLine = word;
                } else {
                    if (currentLine.length === 0) {
                        currentLine = word;
                    } else {
                        currentLine += ' ' + word;
                    }
                }
            });
            lines.push(currentLine);
            return lines;
        }

        const ctx = document.getElementById('timeSavedChart').getContext('2d');
        const timeSavedChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: [
                    wrapText('手作業でのトリミング時間', 16), 
                    wrapText('ツール利用で削減される時間', 16)
                ],
                datasets: [{
                    label: '作業時間',
                    data: [10, 90],
                    backgroundColor: [
                        '#FF4E50', // Energetic & Playful Red
                        '#F9D423'  // Energetic & Playful Yellow
                    ],
                    borderColor: '#ffffff',
                    borderWidth: 4,
                    hoverOffset: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '70%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            font: {
                                size: 14
                            },
                            padding: 20
                        }
                    },
                    tooltip: {
                        callbacks: {
                            title: function(tooltipItems) {
                                const item = tooltipItems[0];
                                let label = item.chart.data.labels[item.dataIndex];
                                if (Array.isArray(label)) {
                                  return label.join(' ');
                                } else {
                                  return label;
                                }
                            }
                        }
                    }
                }
            }
        });
    </script>
</body>
</html>
