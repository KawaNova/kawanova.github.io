#!/usr/bin/env python3
"""
KawaNova Official Showcase Portal Builder
Generates responsive, SEO-optimized, beginner-friendly SPA with Feature Graphics and Zero Dead Links.
"""
import os
import json

ROOT_DIR = r"c:\Users\Kawamoto\Documents\AgentAIDev\kawanova.github.io"
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

# Master App Catalog with Beginner-Friendly Copy & Status
APPS = [
    # ==================== 🟢 製品版 公開中 (6本) ====================
    {
        "id": "009",
        "slug": "fp3-quiz",
        "nameJa": "FP3級 試験対策ミニドリル",
        "nameEn": "FP3 Trainer",
        "category": "exam",
        "categoryLabel": "🎓 金融・国家資格",
        "status": "published",
        "pkg": "com.kawanova.fp3trainer",
        "catch": "【通勤・通学のスキマ学習】FP3級の一発合格をサポート！",
        "benefit": "税金・不動産・資産運用など初学者がつまずきやすい6分野をスッキリ図解。完全オフライン対応で電車内でもサクサク復習できます。",
        "tags": ["FP3級", "完全無料", "オフライン対応", "丁寧な解説", "スキマ学習"],
        "featureImage": "assets/features/feature_009.png",
        "fallbackEmoji": "💰",
        "formType": "exam"
    },
    {
        "id": "002",
        "slug": "it-passport",
        "nameJa": "ITパスポート 頻出ドリル",
        "nameEn": "IT Passport Drill",
        "category": "exam",
        "categoryLabel": "🎓 国家試験",
        "status": "published",
        "pkg": "com.kawanova.itpassport",
        "catch": "【知識ゼロから合格へ】ITの基礎が丸ごと身につく過去問ドリル",
        "benefit": "難解な専門用語をわかりやすい日本語と図解で徹底解説。新シラバス・生成AI関連用語にも完全対応し、初心者でも迷わず学べます。",
        "tags": ["ITパスポート", "完全無料", "新シラバス対応", "初心者歓迎", "一問一答"],
        "featureImage": "assets/features/feature_002.png",
        "fallbackEmoji": "💻",
        "formType": "exam"
    },
    {
        "id": "004",
        "slug": "wanpo-alert",
        "nameJa": "わんぽアラート",
        "nameEn": "Wanpo Alert",
        "category": "lifestyle",
        "categoryLabel": "🐾 ペットライフ",
        "status": "published",
        "pkg": "com.kawanova.wanpo_alert",
        "catch": "【愛犬の熱中症・足裏火傷を防ぐ】お散歩安全アラート＆ケア",
        "benefit": "気温ではなく「アスファルトの地表温度」を推定し、危険な時間帯を避けて安心してお散歩できる時間を教えてくれる愛犬家必須のアプリ。",
        "tags": ["愛犬ケア", "熱中症予防", "地表温度予測", "散歩アラート", "完全無料"],
        "featureImage": "assets/features/feature_004.jpg",
        "fallbackEmoji": "🐕",
        "formType": "lifestyle"
    },
    {
        "id": "008",
        "slug": "novusarcade",
        "nameJa": "Novus Arcade",
        "nameEn": "Novus Arcade",
        "category": "lifestyle",
        "categoryLabel": "🎮 レトロゲーム",
        "status": "published",
        "pkg": "com.kawanova.arcade",
        "catch": "【電波がなくても遊べる】大人の脳トレ＆レトロパズルゲーム集",
        "benefit": "リバーシ、ブロック崩し、記憶力パズルなど飽きずに楽しめる名作ミニゲームを集約。通信制限中や地下鉄でもストレスゼロで遊べます。",
        "tags": ["ミニゲーム", "完全オフライン", "脳トレ", "通信不要", "完全無料"],
        "featureImage": "assets/features/feature_008.png",
        "fallbackEmoji": "🕹️",
        "formType": "lifestyle"
    },
    {
        "id": "010",
        "slug": "Python3-DataAnalysis",
        "nameJa": "Python3 データ分析認定ドリル",
        "nameEn": "Python3 Data Analysis",
        "category": "devtools",
        "categoryLabel": "🛠️ Python・データ分析",
        "status": "published",
        "pkg": "com.kawadev.python3basicdata",
        "catch": "【pandas / NumPy / scikit-learn特訓】データ分析認定試験 模擬問題集",
        "benefit": "データサイエンスの登竜門。実務コードを見ながら四択クイズで直感的に文法とライブラリ操作をマスターできる学習ドリル。",
        "tags": ["Python3", "データ分析", "pandas/NumPy", "模擬試験280問", "完全無料"],
        "featureImage": "assets/features/feature_010.png",
        "fallbackEmoji": "🐍",
        "formType": "dev"
    },
    {
        "id": "012",
        "slug": "Python3-Practical",
        "nameJa": "Python3 実践エンジニア特訓",
        "nameEn": "Python3 Practical Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ 実践プログラミング",
        "status": "published",
        "pkg": "com.kawanova.python3practical",
        "catch": "【現場で使える実践コード】スクレイピング・非同期処理・API連携特訓",
        "benefit": "文法を覚えた次のステップへ。実務でよくあるエラーや標準ライブラリの正しい使い方を実践問題で深く学べる中級者向けドリル。",
        "tags": ["Python3実務", "スクレイピング", "非同期処理", "202問収録", "完全無料"],
        "featureImage": "assets/features/feature_012.png",
        "fallbackEmoji": "⚙️",
        "formType": "dev"
    },

    # ==================== 🧪 クローズドベータテスト中 (7本) ====================
    {
        "id": "015",
        "slug": "fe-drill",
        "nameJa": "基本情報 科目B アルゴリズム特訓",
        "nameEn": "FE Drill - Subject B",
        "category": "exam",
        "categoryLabel": "🎓 国家試験",
        "status": "beta",
        "pkg": "com.kawanova.fedrill",
        "catch": "【擬似言語で挫折した人専用】コードの動きが1行ずつ見えるトレース特訓",
        "benefit": "基本情報の最大の難関「科目B」。変数の変化やループ処理をステップ実行で視覚化し、文系・初学者でもアルゴリズムを直感的に理解できます。",
        "tags": ["基本情報技術者", "科目B", "アルゴリズム", "ステップ実行", "効果音つき"],
        "featureImage": "assets/features/feature_015.png",
        "fallbackEmoji": "🎯",
        "formType": "exam"
    },
    {
        "id": "001",
        "slug": "boki-journal",
        "nameJa": "日商簿記3級 仕訳ミニドリル",
        "nameEn": "Boki Journal 3",
        "category": "exam",
        "categoryLabel": "🎓 ビジネス・簿記",
        "status": "beta",
        "pkg": "com.kawanova.bokijournal",
        "catch": "【借方・貸方を体で覚える】簿記3級の仕訳サクサク反復ドリル",
        "benefit": "勘定科目の分類から決算整理仕訳まで、タップ操作でサクサク反復練習。仕訳のルールが感覚的に身につきます。",
        "tags": ["簿記3級", "仕訳練習", "勘定科目", "一問一答", "オフライン"],
        "featureImage": "assets/features/feature_001.png",
        "fallbackEmoji": "📊",
        "formType": "exam"
    },
    {
        "id": "006",
        "slug": "mimitore",
        "nameJa": "耳トレ AuraPitch",
        "nameEn": "AuraPitch",
        "category": "lifestyle",
        "categoryLabel": "🎵 音楽・音感",
        "status": "beta",
        "pkg": "com.kawanova.aurapitch",
        "catch": "【音感を育てる】絶対音感・ピッチ判定トレーニング",
        "benefit": "単音当てクイズや和音聞き分けで、楽しみながら日常的に音感をトレーニングできる音楽アプリ。",
        "tags": ["音感トレーニング", "絶対音感", "ピアノ音源", "ゲーム感覚", "無料"],
        "featureImage": "assets/features/feature_006.png",
        "fallbackEmoji": "🎶",
        "formType": "lifestyle"
    },
    {
        "id": "007",
        "slug": "sql-query-drill",
        "nameJa": "データ分析SQL基礎ドリル",
        "nameEn": "SQL Query Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ データベース",
        "status": "beta",
        "pkg": "com.kawanova.sql_query_drill",
        "catch": "【手を動かして学ぶ】SELECT/JOIN実務クエリ構文特訓",
        "benefit": "穴埋め形式でSQLの基本構文を反復学習。文系エンジニアやデータ分析初心者が実務で使えるクエリ力を養います。",
        "tags": ["SQL", "SELECT/JOIN", "データベース", "構文特訓", "実務直結"],
        "featureImage": "assets/features/feature_007.png",
        "fallbackEmoji": "🗄️",
        "formType": "dev"
    },
    {
        "id": "013",
        "slug": "offmoji",
        "nameJa": "オフモジ - オフライン文字装飾",
        "nameEn": "OffMoji",
        "category": "lifestyle",
        "categoryLabel": "🎨 ユーティリティ",
        "status": "beta",
        "pkg": "com.kawanova.talktext",
        "catch": "【電波いらずの間接メモ】SNS映えするアスキーアート＆装飾テキスト生成",
        "benefit": "完全オフラインで動作するスタイリッシュな文字装飾ツール。コピペで使えるかわいいAAや吹き出しが作れます。",
        "tags": ["文字装飾", "アスキーアート", "オフライン", "SNS用", "簡単コピペ"],
        "featureImage": "assets/features/feature_013.png",
        "fallbackEmoji": "💬",
        "formType": "lifestyle"
    },
    {
        "id": "003",
        "slug": "rakuphotoai",
        "nameJa": "らくフォトAI - 背景切り抜き・顔ぼかし",
        "nameEn": "RakuPhoto AI",
        "category": "lifestyle",
        "categoryLabel": "🎨 画像編集・AI",
        "status": "beta",
        "pkg": "com.kawanova.rakuphotoai",
        "catch": "【完全オンデバイスAI】写真をサーバーに送らず安心！ワンタップ背景透過",
        "benefit": "プライベートな写真を外部に一切送信せず、スマホ端末内のAIだけで人物の切り抜きや顔のぼかし加工が完了します。",
        "tags": ["オンデバイスAI", "背景透過", "顔ぼかし", "プライバシー保護", "安全"],
        "featureImage": "assets/features/feature_003.png",
        "fallbackEmoji": "✂️",
        "formType": "lifestyle"
    },
    {
        "id": "014",
        "slug": "tatenaga-screenshot",
        "nameJa": "たてながスクショ - Web縦長キャプチャ",
        "nameEn": "Tatenaga Screenshot",
        "category": "lifestyle",
        "categoryLabel": "🎨 ユーティリティ",
        "status": "beta",
        "pkg": "com.kawanova.tatenaga",
        "catch": "【スクロールページを丸ごと1枚に】Web長尺スクショ＆画像結合",
        "benefit": "長いWebページやチャットのやりとりを途切れず1枚のきれいな画像として保存・共有できる便利ツール。",
        "tags": ["縦長スクショ", "Webキャプチャ", "画像結合", "高画質保存", "簡単操作"],
        "featureImage": "assets/features/feature_014.png",
        "fallbackEmoji": "📱",
        "formType": "lifestyle"
    },

    # ==================== 🚀 開発中・近日公開ラインナップ (23本) ====================
    {
        "id": "024",
        "slug": "aws-clf-drill",
        "nameJa": "AWS クラウド超入門 - CLF-C02 突破",
        "nameEn": "AWS Drill - CLF-C02",
        "category": "exam",
        "categoryLabel": "🎓 クラウド資格",
        "status": "coming_soon",
        "pkg": "com.kawanova.awsclfdrill",
        "catch": "【構成図シミュレータ搭載】CLF-C02最新シラバス対応30問特訓",
        "benefit": "EC2やS3、VPCなどの重要サービスを視覚的なアーキテクチャ図で理解できるクラウド学習アプリ。",
        "tags": ["AWS CLF", "クラウド入門", "構成図シミュレータ", "合格のツボ", "一問一答"],
        "featureImage": "assets/features/feature_024.png",
        "fallbackEmoji": "☁️",
        "formType": "exam"
    },
    {
        "id": "028",
        "slug": "takken-drill",
        "nameJa": "宅建士 突破特訓 - 権利関係・宅建業法",
        "nameEn": "Takken Drill",
        "category": "exam",
        "categoryLabel": "🎓 国家資格・不動産",
        "status": "coming_soon",
        "pkg": "com.kawanova.takkendrill",
        "catch": "【毎年25万人が挑む最難関へ】権利関係・宅建業法の頻出過去問対策",
        "benefit": "民法のひっかけ条文や宅建業法の重要ルールを図解と一問一答で徹底整理。初学者でも合格ラインを突破。",
        "tags": ["宅建士", "権利関係", "宅建業法", "過去問特訓", "オフライン対応"],
        "featureImage": "assets/features/feature_028.png",
        "fallbackEmoji": "🏠",
        "formType": "exam"
    },
    {
        "id": "017",
        "slug": "fe-kamoku-a",
        "nameJa": "基本情報技術者 科目A 突破",
        "nameEn": "FE Kamoku A",
        "category": "exam",
        "categoryLabel": "🎓 国家試験",
        "status": "coming_soon",
        "pkg": "com.kawanova.fekamokua",
        "catch": "【通年CBT試験対応】新シラバス・生成AI含む頻出問題ドリル",
        "benefit": "テクノロジ・マネジメント・ストラテジの全肢解説付き。科目Bアプリと組み合わせることで完全合格を目指せます。",
        "tags": ["基本情報 科目A", "通年CBT", "新シラバス", "全問解説", "オフライン"],
        "featureImage": "assets/features/feature_017.png",
        "fallbackEmoji": "💻",
        "formType": "exam"
    },
    {
        "id": "016",
        "slug": "ap-drill",
        "nameJa": "応用情報 午後プログラミング問3特訓",
        "nameEn": "AP Drill",
        "category": "exam",
        "categoryLabel": "🎓 高度国家試験",
        "status": "coming_soon",
        "pkg": "com.kawanova.apdrill",
        "catch": "【問3完全攻略】木構造・動的計画法・グラフ探索の解法特訓",
        "benefit": "応用情報の午後プログラミング問題に特化。アルゴリズムの思考プロセスをスマホで着実に鍛えます。",
        "tags": ["応用情報", "午後プログラミング", "動的計画法", "木構造", "完全解説"],
        "featureImage": "assets/features/feature_016.png",
        "fallbackEmoji": "📊",
        "formType": "exam"
    },
    {
        "id": "026",
        "slug": "sg-drill",
        "nameJa": "情報セキュリティマネジメント超入門",
        "nameEn": "SG Drill",
        "category": "exam",
        "categoryLabel": "🎓 セキュリティ国家資格",
        "status": "coming_soon",
        "pkg": "com.kawanova.sgdrill",
        "catch": "【DX時代の必須スキル】サイバー攻撃防御フロー＆SG過去問特訓",
        "benefit": "フィッシング、ランサムウェア、認証技術などを図解で理解。ITパスポートからのステップアップに最適。",
        "tags": ["セキマネ", "情報セキュリティ", "サイバー防御", "CBT試験対応", "無料"],
        "featureImage": "assets/features/feature_026.png",
        "fallbackEmoji": "🛡️",
        "formType": "exam"
    },
    {
        "id": "036",
        "slug": "curl-converter",
        "nameJa": "cURLコードジェネレータ (CurlForge)",
        "nameEn": "CurlForge",
        "category": "devtools",
        "categoryLabel": "🛠️ 開発者ツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.curlforge",
        "catch": "【APIリクエストを瞬時にコード化】Python/JS/Go/Kotlin/PHP即時変換",
        "benefit": "cURLコマンドを貼り付けるだけで各言語の実行コードを完全オンデバイスで生成。認証トークンも漏洩ゼロで安心。",
        "tags": ["cURL変換", "Python requests", "Fetch API", "10言語対応", "100%安全"],
        "featureImage": "assets/features/feature_036.png",
        "fallbackEmoji": "⚡",
        "formType": "dev"
    },
    {
        "id": "035",
        "slug": "dns-inspector",
        "nameJa": "DNSレコード設定ガイド (DNSCraft)",
        "nameEn": "DNSCraft",
        "category": "devtools",
        "categoryLabel": "🛠️ インフラ・DNS",
        "status": "coming_soon",
        "pkg": "com.kawanova.dnscraft",
        "catch": "【メール不達・ドメイン設定の悩みを解決】SPF/DMARC監査＆ゾーン生成",
        "benefit": "Google/Yahooの新送信ドメイン要件に完全適合したSPF・DMARC設定をウィザード形式で自動生成。",
        "tags": ["DNS設定", "SPF / DMARC", "Route 53", "BIND Zone", "設定診断"],
        "featureImage": "assets/features/feature_035.png",
        "fallbackEmoji": "🌐",
        "formType": "dev"
    },
    {
        "id": "034",
        "slug": "http-headers",
        "nameJa": "HTTPヘッダー設定ガイド (HeaderCraft)",
        "nameEn": "HeaderCraft",
        "category": "devtools",
        "categoryLabel": "🛠️ 開発者ツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.headercraft",
        "catch": "【CORSエラーやキャッシュ設定で迷わない】セキュリティヘッダー診断",
        "benefit": "直感的なGUIでCORSやCache-Control、HSTS/CSP設定を組み立て、NginxやApache設定ファイルを即座に出力。",
        "tags": ["HTTPヘッダー", "CORS対策", "Cache-Control", "Nginx設定", "セキュリティA+"],
        "featureImage": "assets/features/feature_034.png",
        "fallbackEmoji": "📑",
        "formType": "dev"
    },
    {
        "id": "033",
        "slug": "jwt-inspector",
        "nameJa": "JWTインスペクター",
        "nameEn": "JWT Inspector",
        "category": "devtools",
        "categoryLabel": "🛠️ セキュリティツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.jwtinspector",
        "catch": "【秘密鍵やトークンをネットに送らない】完全ローカルJWTデコーダ",
        "benefit": "Base64URLデコード、有効期限判定、クレーム検証を端末内だけで実行。機密トークンを外部送信しない安心設計。",
        "tags": ["JWTデコード", "トークン検証", "完全オフライン", "セキュリティ", "プライバシー保証"],
        "featureImage": "assets/features/feature_033.png",
        "fallbackEmoji": "🔐",
        "formType": "dev"
    },
    {
        "id": "032",
        "slug": "cron-generator",
        "nameJa": "Cron式ビルダー (CronGen)",
        "nameEn": "CronGen",
        "category": "devtools",
        "categoryLabel": "🛠️ 開発者ツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.crongen",
        "catch": "【Cronの書き方ミスをゼロに】次回実行日時シミュレータ付きCron生成",
        "benefit": "日本語UIでスケジュールを選ぶだけで正確なCron式を生成。次回5回の実行予定日時をその場でシミュレーション確認。",
        "tags": ["Cron式", "定期実行", "スケジュール", "Crontab", "実行シミュレータ"],
        "featureImage": "assets/features/feature_032.png",
        "fallbackEmoji": "⏱️",
        "formType": "dev"
    },
    {
        "id": "031",
        "slug": "font-preview",
        "nameJa": "フォントスタイラー (FontStyler)",
        "nameEn": "FontStyler",
        "category": "devtools",
        "categoryLabel": "🎨 デザイン・フォント",
        "status": "coming_soon",
        "pkg": "com.kawanova.fontstyler",
        "catch": "【文字サイズや行間の悩みを解決】タイポグラフィ検証＆CSS生成",
        "benefit": "日本語フォントの見え方や行間（line-height）、文字詰めをスマホ実機でリアルタイム検証。CSSコードをワンタップコピー。",
        "tags": ["フォント検証", "タイポグラフィ", "CSS生成", "行間調整", "Webデザイン"],
        "featureImage": "assets/features/feature_031.png",
        "fallbackEmoji": "🔤",
        "formType": "lifestyle"
    },
    {
        "id": "030",
        "slug": "markdown-editor",
        "nameJa": "MarkNote - Markdownエディタ",
        "nameEn": "MarkNote",
        "category": "devtools",
        "categoryLabel": "📝 テキスト編集",
        "status": "coming_soon",
        "pkg": "com.kawanova.marknote",
        "catch": "【リアルタイムプレビュー】表・数式・コードブロック対応Markdownメモ",
        "benefit": "スマホでも軽快に入力できる専用ツールバー付き。完全ローカル保存で大切なアイデアを外部に漏らしません。",
        "tags": ["Markdown", "リアルタイムプレビュー", "KaTeX数式", "完全ローカル", "高速動作"],
        "featureImage": "assets/features/feature_030.png",
        "fallbackEmoji": "📝",
        "formType": "dev"
    },
    {
        "id": "029",
        "slug": "color-palette",
        "nameJa": "カラーパレット (ColorPalette)",
        "nameEn": "ColorPalette",
        "category": "devtools",
        "categoryLabel": "🎨 デザイン・配色",
        "status": "coming_soon",
        "pkg": "com.kawanova.colorpalette",
        "catch": "【見やすい配色がすぐ見つかる】調和色生成 ＆ WCAG視認性判定",
        "benefit": "写真からの配色抽出や、補色・類似色の自動生成。文字と背景のコントラスト比がアクセシビリティ基準を満たすか瞬時に判定。",
        "tags": ["カラーパレット", "配色支援", "WCAGコントラスト比", "HEX/RGB", "デザインツール"],
        "featureImage": "assets/features/feature_029.png",
        "fallbackEmoji": "🎨",
        "formType": "lifestyle"
    },
    {
        "id": "027",
        "slug": "api-tester",
        "nameJa": "モバイルAPIテスター (API Tester)",
        "nameEn": "API Tester",
        "category": "devtools",
        "categoryLabel": "🛠️ 開発者ツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.apitester",
        "catch": "【スマホでREST API疎通確認】JSON整形＆ヘッダー検証クライアント",
        "benefit": "外出先でもスマホからAPIの疎通やレスポンス確認が可能。JSONのシンタックスハイライトと整形表示に対応。",
        "tags": ["APIテスト", "REST Client", "JSON整形", "ヘッダー検証", "外出先デバッグ"],
        "featureImage": "assets/features/feature_027.png",
        "fallbackEmoji": "🚀",
        "formType": "dev"
    },
    {
        "id": "025",
        "slug": "k8s-drill",
        "nameJa": "Kubernetes超入門 - クラウド特訓",
        "nameEn": "K8s Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ インフラ・コンテナ",
        "status": "coming_soon",
        "pkg": "com.kawanova.k8sdrill",
        "catch": "【Pod/Service/Ingressの構造がわかる】コンテナ運用特訓ドリル",
        "benefit": "難解なK8sの概念を図解で分解。マニフェスト（YAML）の読み方やトラブルシューティングコマンドを演習形式で習得。",
        "tags": ["Kubernetes", "コンテナオーケストレーション", "Pod/Service", "YAML図解", "実践ドリル"],
        "featureImage": "assets/features/feature_025.png",
        "fallbackEmoji": "☸️",
        "formType": "dev"
    },
    {
        "id": "023",
        "slug": "regex-drill",
        "nameJa": "正規表現超入門 - 実務パターン逆引き",
        "nameEn": "Regex Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ プログラミング",
        "status": "coming_soon",
        "pkg": "com.kawanova.regexdrill",
        "catch": "【リアルタイムハイライト判定】実務正規表現テスター＆特訓ドリル",
        "benefit": "メールアドレス、URL、郵便番号などの頻出正規表現を逆引き検索。スマホ上でパターンを入力すると一致箇所が黄色く光るテスター付き。",
        "tags": ["正規表現", "リアルタイムテスター", "パターン逆引き", "チートシート", "初心者歓迎"],
        "featureImage": "assets/features/feature_023.png",
        "fallbackEmoji": "🔍",
        "formType": "dev"
    },
    {
        "id": "022",
        "slug": "network-drill",
        "nameJa": "ネットワーク超入門 - Webプロトコル",
        "nameEn": "Network Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ ネットワーク",
        "status": "coming_soon",
        "pkg": "com.kawanova.networkdrill",
        "catch": "【HTTPステータス・DNS・TCP/IP】Webの仕組みが直感的にわかる特訓",
        "benefit": "「403と401の違いは？」「TCPの3ウェイハンドシェイクとは？」Web開発で必須となる通信の基礎知識を一問一答でサクサク理解。",
        "tags": ["ネットワーク基礎", "HTTPステータス", "TCP/IP", "DNSの仕組み", "一問一答"],
        "featureImage": "assets/features/feature_022.png",
        "fallbackEmoji": "🌐",
        "formType": "dev"
    },
    {
        "id": "021",
        "slug": "docker-drill",
        "nameJa": "Docker & コンテナ超入門",
        "nameEn": "Docker Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ 開発者ツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.dockerdrill",
        "catch": "【Dockerfile・Composeの書き方がわかる】コンテナ基礎特訓",
        "benefit": "コンテナ作成、ポートフォワーディング、ボリュームマウントなどの必須コマンドとベストプラクティスをクイズ形式でマスター。",
        "tags": ["Docker入門", "Dockerfile", "docker-compose", "コンテナ基礎", "実務特訓"],
        "featureImage": "assets/features/feature_021.png",
        "fallbackEmoji": "🐳",
        "formType": "dev"
    },
    {
        "id": "020",
        "slug": "seo-analyzer",
        "nameJa": "SEOアナライザー - Web健全性診断",
        "nameEn": "SEO Analyzer",
        "category": "devtools",
        "categoryLabel": "📈 Webマーケティング",
        "status": "coming_soon",
        "pkg": "com.kawanova.seoanalyzer",
        "catch": "【自サイトのSEOスコアをチェック】OGPプレビュー＆メタタグ診断",
        "benefit": "URLを入れるだけでmetaタイトル・ディスクリプション・OGP画像・見出し構造を瞬時に分析。SNSシェア時の見え方もシミュレート。",
        "tags": ["SEO診断", "OGPプレビュー", "メタタグ検査", "Webサイト分析", "完全無料"],
        "featureImage": "assets/features/feature_020.png",
        "fallbackEmoji": "📈",
        "formType": "dev"
    },
    {
        "id": "019",
        "slug": "linux-drill",
        "nameJa": "Linuxコマンド超入門 - シェル特訓",
        "nameEn": "Linux Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ サーバー・Linux",
        "status": "coming_soon",
        "pkg": "com.kawanova.linuxdrill",
        "catch": "【chmod・パイプ・grepを攻略】現場で迷わない実務Linux特訓",
        "benefit": "ファイルパーミッション計算、パイプライン、リダイレクト、プロセス管理など、新米エンジニアが一番最初に知るべきコマンドを徹底特訓。",
        "tags": ["Linuxコマンド", "Bashシェル", "パーミッション計算", "サーバー管理", "初学者向け"],
        "featureImage": "assets/features/feature_019.png",
        "fallbackEmoji": "🐧",
        "formType": "dev"
    },
    {
        "id": "018",
        "slug": "git-drill",
        "nameJa": "Gitコマンド超入門 - トラブル脱出",
        "nameEn": "Git Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ 開発者ツール",
        "status": "coming_soon",
        "pkg": "com.kawanova.gitdrill",
        "catch": "【間違えたコミットを取り消したい！】ブランチツリー可視化＆Git特訓",
        "benefit": "ブランチの分岐、マージコンフリクトの解決、git reset / rebase の使い分けを図解で理解。現場の「やらかし」を未然に防ぎます。",
        "tags": ["Gitコマンド", "GitHub入門", "ブランチ図解", "コンフリクト解決", "脱出コマンド"],
        "featureImage": "assets/features/feature_018.png",
        "fallbackEmoji": "🐙",
        "formType": "dev"
    },
    {
        "id": "005",
        "slug": "lazyfitnessai",
        "nameJa": "LazyFit AI - ズボラ筋トレ自動カウント",
        "nameEn": "LazyFit AI",
        "category": "lifestyle",
        "categoryLabel": "💪 ヘルスケア",
        "status": "coming_soon",
        "pkg": "com.kawanova.lazyfitnessai",
        "catch": "【三日坊主を防ぐ】置くだけで自動レップカウント＆習慣化",
        "benefit": "スマホのカメラやセンサーで運動回数を自動カウント。無理のない短時間トレーニングで運動習慣をサポート。",
        "tags": ["筋トレ習慣化", "自動カウント", "ズボラ歓迎", "ヘルスケア", "完全無料"],
        "featureImage": "assets/features/feature_005.png",
        "fallbackEmoji": "💪",
        "formType": "lifestyle"
    },
    {
        "id": "011",
        "slug": "Python3-Basic",
        "nameJa": "Python3 基礎認定ドリル",
        "nameEn": "Python3 Basic Drill",
        "category": "devtools",
        "categoryLabel": "🛠️ プログラミング基礎",
        "status": "coming_soon",
        "pkg": "com.kawanova.python3basic",
        "catch": "【文法ゼロからスラスラ解ける】Python3 基礎認定試験 模擬問題集",
        "benefit": "変数、リスト、辞書、ループ、関数の定義などPythonの根幹を300問の丁寧な一問一答で徹底マスター。",
        "tags": ["Python3基礎", "模擬試験300問", "初心者特訓", "プログラミング入門", "無料"],
        "featureImage": "assets/features/feature_011.png",
        "fallbackEmoji": "🐍",
        "formType": "dev"
    }
]

def generate_html():
    apps_json = json.dumps(APPS, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="ja" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>KawaNova 公式ポータル | 通勤・スキマ時間で受かる資格対策 ＆ 完全オフライン開発者ツール</title>
  
  <!-- Primary Meta Tags -->
  <meta name="title" content="KawaNova 公式ポータル | 通勤・スキマ時間で受かる資格対策 ＆ 完全オフライン開発者ツール" />
  <meta name="description" content="完全無料で安心のオンデバイスAndroidアプリシリーズ。基本情報技術者、ITパスポート、FP3級、宅建、AWS、Docker、cURL変換、DNS設定など全36作品。電車内やオフラインでもサクサク学べる初心者フレンドリーな設計。" />
  <meta name="keywords" content="KawaNova, 基本情報技術者 科目B アプリ, ITパスポート 独学, FP3級 過去問, 宅建 アプリ おすすめ, AWS CLF-C02, cURL 変換, DNS SPF 設定, 完全オフライン, Androidアプリ 無料" />
  <meta name="author" content="KawaNova" />
  <link rel="canonical" href="https://kawanova.github.io/" />
  <meta name="google-site-verification" content="7Cmy6fM2i0lHoOxS4KuKYxa0OxgVa8MvxO7ceKS2ULY" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://kawanova.github.io/" />
  <meta property="og:title" content="KawaNova 公式ポータル | スキマ時間で受かる資格対策 ＆ 開発者ツール" />
  <meta property="og:description" content="完全オンデバイス・プライバシー保護のAndroidアプリシリーズ。基本情報、ITパスポート、FP3級、AWS、cURL変換など全36作品。" />
  <meta property="og:image" content="https://kawanova.github.io/assets/features/feature_015.png" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="KawaNova 公式アプリポータル" />
  <meta name="twitter:description" content="完全オンデバイス・安心の無料Androidアプリシリーズ全36作品。" />
  <meta name="twitter:image" content="https://kawanova.github.io/assets/features/feature_015.png" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              slate: '#0F172A',
              card: '#1E293B',
              border: '#334155',
              cyan: '#06B6D4',
              sky: '#38BDF8',
              emerald: '#10B981',
              amber: '#F59E0B'
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700;900&display=swap');
    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: #0B1120;
    }}
    .font-mono-code {{
      font-family: 'JetBrains Mono', monospace;
    }}
  </style>

  <!-- Schema.org Structured Data (JSON-LD) for SEO Rich Results -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "KawaNova",
    "url": "https://kawanova.github.io/",
    "logo": "https://kawanova.github.io/assets/features/feature_015.png",
    "description": "完全オンデバイス・プライバシー保護のAndroid資格対策＆実務ツールアプリデベロッパー",
    "sameAs": [
      "https://github.com/KawaNova",
      "https://play.google.com/store/apps/developer?id=KawaNova"
    ]
  }}
  </script>
</head>
<body class="text-slate-100 min-h-screen flex flex-col antialiased selection:bg-cyan-500 selection:text-slate-900">

  <!-- Header -->
  <header class="sticky top-0 z-50 backdrop-blur-md bg-slate-950/90 border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <a href="#" class="flex items-center space-x-3 group">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-sky-400 flex items-center justify-center font-bold text-slate-950 text-xl shadow-lg shadow-cyan-500/20 group-hover:scale-105 transition-transform">
          ⚡
        </div>
        <div>
          <span class="font-bold text-lg tracking-tight text-white group-hover:text-cyan-400 transition-colors">KawaNova <span class="text-cyan-400">Apps</span></span>
          <span class="hidden sm:inline-block ml-2 text-xs font-semibold px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700">全36作品</span>
        </div>
      </a>

      <nav class="flex items-center space-x-3 sm:space-x-5 text-sm font-medium">
        <a href="#apps" class="text-slate-300 hover:text-cyan-400 transition-colors">アプリ一覧</a>
        <a href="#betalab" class="text-amber-400 hover:text-amber-300 transition-colors flex items-center space-x-1">
          <span>🧪 ベータテスト</span>
        </a>
        <a href="#faq" class="text-slate-300 hover:text-cyan-400 transition-colors hidden md:inline-block">よくある質問</a>
        <a href="https://kawanova.github.io/privacy-policy/android-common.html" target="_blank" rel="noopener" class="text-slate-300 hover:text-cyan-400 transition-colors hidden lg:inline-block">プライバシーポリシー</a>
        <a href="https://github.com/KawaNova" target="_blank" rel="noopener" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 flex items-center space-x-1.5 transition-all text-xs sm:text-sm">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          <span>GitHub</span>
        </a>
      </nav>
    </div>
  </header>

  <!-- Hero Section (SEO & Benefit Focused) -->
  <section class="relative overflow-hidden pt-12 pb-16 border-b border-slate-800/80 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950">
    <div class="absolute inset-0 bg-[radial-gradient(#06b6d4_1px,transparent_1px)] [background-size:24px_24px] opacity-15 pointer-events-none"></div>
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Trust Badges -->
      <div class="inline-flex flex-wrap justify-center items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-800/90 border border-cyan-500/30 text-cyan-400 text-xs font-semibold mb-6 shadow-inner">
        <span>✨ 完全無料</span>
        <span class="w-1 h-1 rounded-full bg-slate-600"></span>
        <span>📶 完全オフライン対応（通信量ゼロ）</span>
        <span class="w-1 h-1 rounded-full bg-slate-600"></span>
        <span>🛡️ 個人情報送信ゼロ</span>
        <span class="w-1 h-1 rounded-full bg-slate-600"></span>
        <span>⚡ 広告ひかえめ</span>
      </div>

      <!-- Main Catchphrase -->
      <h1 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight mb-5">
        スキマ時間で受かる、現場で役立つ。<br />
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400">
          初心者にやさしい Android アプリシリーズ
        </span>
      </h1>

      <p class="text-sm sm:text-base text-slate-300 max-w-3xl mx-auto mb-8 leading-relaxed">
        通勤電車やカフェのスキマ時間5分でサクサク学べる「国家試験・資格対策ドリル」から、<br class="hidden sm:inline" />
        秘密情報をネットに送信しない「完全オフライン開発者ツール」まで。<br class="hidden sm:inline" />
        見やすさと使いやすさに徹底的にこだわったAndroidアプリを公開しています。
      </p>

      <!-- CTA Buttons -->
      <div class="flex flex-wrap items-center justify-center gap-4">
        <a href="#apps" onclick="filterStatus('published')" class="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-bold text-sm shadow-lg shadow-emerald-500/20 transition-all flex items-center space-x-2">
          <span>🟢 今すぐ使える公開中アプリ (6本)</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </a>
        <a href="#betalab" class="px-5 py-3 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-sm transition-all flex items-center space-x-2">
          <span>🧪 先行体験（ベータテスト参加）</span>
        </a>
      </div>

    </div>
  </section>

  <!-- KawaNova Beta Lab Section -->
  <section id="betalab" class="bg-gradient-to-r from-slate-950 via-slate-900 to-slate-950 border-b border-amber-500/30 py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-5xl mx-auto rounded-2xl bg-amber-500/5 border border-amber-500/30 p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="space-y-2 text-center md:text-left">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 text-xs font-bold border border-amber-500/30">
          <span>🧪 KawaNova Beta Lab</span>
          <span>・</span>
          <span>クローズドテスター募集中</span>
        </div>
        <h2 class="text-xl sm:text-2xl font-bold text-white">開発中の最新アプリを、一般公開前に先行体験！</h2>
        <p class="text-xs sm:text-sm text-slate-300 max-w-2xl leading-relaxed">
          Google Play 公式のクローズドテストに参加して、基本情報科目Bや日商簿記3級などの最新作をいち早くプレイできます。<br />
          Google グループに登録するだけで、迷惑メールは一切届きません。いつでもワンクリックで退会できます。
        </p>
        <div class="text-[11px] text-slate-400 pt-1">
          参加ステップ: ① 下のボタンからGoogleグループに参加 ➔ ② ストアのテスト版URLからインストール
        </div>
      </div>
      <div class="flex-shrink-0 flex flex-col sm:flex-row gap-3">
        <a href="https://groups.google.com/g/kawanova-beta-lab" target="_blank" rel="noopener" class="px-5 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-sm shadow-lg shadow-amber-500/20 transition-all text-center flex items-center justify-center space-x-1.5">
          <span>👥 Google グループに参加する</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
        </a>
      </div>
    </div>
  </section>

  <!-- Main Showcase Container -->
  <main id="apps" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-1 w-full">

    <!-- Top Status Filter Tabs (Zero Dead Links Architecture) -->
    <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-8">
      <button id="status-tab-published" onclick="filterStatus('published')" class="status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20 transition-all flex items-center space-x-1.5">
        <span>🟢 今すぐ使える公開中</span>
        <span class="px-1.5 py-0.5 rounded-full bg-slate-950/20 text-[11px]">6本</span>
      </button>
      <button id="status-tab-beta" onclick="filterStatus('beta')" class="status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all flex items-center space-x-1.5">
        <span>🧪 ベータテスト中</span>
        <span class="px-1.5 py-0.5 rounded-full bg-slate-700 text-slate-300 text-[11px]">7本</span>
      </button>
      <button id="status-tab-coming_soon" onclick="filterStatus('coming_soon')" class="status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all flex items-center space-x-1.5">
        <span>🚀 近日公開ラインナップ</span>
        <span class="px-1.5 py-0.5 rounded-full bg-slate-700 text-slate-300 text-[11px]">23本</span>
      </button>
      <button id="status-tab-all" onclick="filterStatus('all')" class="status-tab px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-400 border border-slate-700 hover:border-slate-600 transition-all">
        <span>すべて表示 (36)</span>
      </button>
    </div>

    <!-- Search & Category Filters -->
    <div class="bg-slate-900/80 rounded-2xl border border-slate-800 p-4 sm:p-6 mb-10 shadow-xl backdrop-blur-sm">
      <div class="flex flex-col md:flex-row items-center justify-between gap-4">
        
        <!-- Search Bar -->
        <div class="relative w-full md:w-96">
          <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          </div>
          <input 
            type="text" 
            id="searchInput"
            placeholder="アプリ名、キーワード（例: 基本情報, FP3, cURL）" 
            class="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-950 border border-slate-700 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 transition-all"
          />
        </div>

        <!-- Category Pills -->
        <div class="flex flex-wrap items-center gap-2 w-full md:w-auto">
          <button id="cat-tab-all" onclick="filterCategory('all')" class="cat-pill px-3 py-1.5 rounded-lg text-xs font-semibold bg-cyan-500 text-slate-950 transition-all">すべて</button>
          <button id="cat-tab-exam" onclick="filterCategory('exam')" class="cat-pill px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all">🎓 国家試験・資格</button>
          <button id="cat-tab-devtools" onclick="filterCategory('devtools')" class="cat-pill px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all">🛠️ 開発者・インフラ</button>
          <button id="cat-tab-lifestyle" onclick="filterCategory('lifestyle')" class="cat-pill px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all">🎨 ライフスタイル・ツール</button>
        </div>

      </div>

      <!-- Live Count Display -->
      <div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
        <span id="resultsCount">表示中: 6 件 (全36作品)</span>
        <span id="statusDescription" class="text-emerald-400 font-medium">現在「🟢 今すぐ使える公開中アプリ」を表示しています</span>
      </div>
    </div>

    <!-- Cards Grid -->
    <div id="appsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
      <!-- Injected via JavaScript -->
    </div>

    <!-- No Results Fallback -->
    <div id="noResults" class="hidden text-center py-20">
      <div class="text-4xl mb-3">🔍</div>
      <h3 class="text-base font-bold text-white mb-1">該当するアプリが見つかりませんでした</h3>
      <p class="text-xs text-slate-400">別のキーワードで検索するか、カテゴリの絞り込みを解除してみてください。</p>
    </div>

  </main>

  <!-- FAQ Section (SEO & Beginner Assurance) -->
  <section id="faq" class="bg-slate-950 border-t border-slate-800/80 py-16 px-4 sm:px-6 lg:px-8">
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-12">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">安心してお使いいただくために</span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-white">よくあるご質問（FAQ）</h2>
      </div>

      <div class="space-y-4">
        
        <div class="rounded-xl bg-slate-900 border border-slate-800 p-5">
          <h3 class="font-bold text-white text-sm sm:text-base mb-2 flex items-center space-x-2">
            <span class="text-cyan-400">Q.</span>
            <span>アプリは完全無料で使えますか？</span>
          </h3>
          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed pl-6">
            はい、KawaNovaのアプリはすべて無料でダウンロードしてご利用いただけます。途中で課金が発生することはありません。
          </p>
        </div>

        <div class="rounded-xl bg-slate-900 border border-slate-800 p-5">
          <h3 class="font-bold text-white text-sm sm:text-base mb-2 flex items-center space-x-2">
            <span class="text-cyan-400">Q.</span>
            <span>インターネット（通信）がない場所でも使えますか？</span>
          </h3>
          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed pl-6">
            はい、すべてのアプリが完全オンデバイス（端末内完結）で動作します。地下鉄の中や飛行機内、通信制限がかかっている状態でもサクサク問題演習やツール機能を利用できます。
          </p>
        </div>

        <div class="rounded-xl bg-slate-900 border border-slate-800 p-5">
          <h3 class="font-bold text-white text-sm sm:text-base mb-2 flex items-center space-x-2">
            <span class="text-cyan-400">Q.</span>
            <span>個人情報や写真・データが外部サーバーに送信されることはありますか？</span>
          </h3>
          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed pl-6">
            一切ありません。クイズの回答データ、編集中の画像、cURLやJWTトークンなどの秘密情報はすべてスマートフォン内部でのみ暗号化・処理され、外部の外部サーバーへ送信されることは100%ありません。プライバシーを最優先に設計しています。
          </p>
        </div>

        <div class="rounded-xl bg-slate-900 border border-slate-800 p-5">
          <h3 class="font-bold text-white text-sm sm:text-base mb-2 flex items-center space-x-2">
            <span class="text-cyan-400">Q.</span>
            <span>「ベータテスト」には誰でも参加できますか？</span>
          </h3>
          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed pl-6">
            はい、どなたでも歓迎です！上部の「Google グループに参加する」ボタンから参加していただくだけで、開発中の最新作（基本情報科目Bや簿記3級など）をGoogle Play公式から安全にインストールできます。
          </p>
        </div>

      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-slate-950 border-t border-slate-900 py-12 text-slate-400 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-10">
        
        <div>
          <div class="flex items-center space-x-2.5 mb-3">
            <span class="text-2xl">⚡</span>
            <span class="font-bold text-white text-base">KawaNova Apps</span>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed mb-4">
            「オフラインで安心して使える高速な実務・学習ツール」をテーマに、Kotlin 2.0 / Jetpack Compose による高品質なAndroidネイティブアプリを開発しています。
          </p>
          <a href="app-ads.txt" class="text-xs text-slate-500 hover:text-slate-400 font-mono">app-ads.txt（AdMob認定）</a>
        </div>

        <div>
          <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">プライバシーポリシー</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="https://kawanova.github.io/privacy-policy/android-common.html" target="_blank" rel="noopener" class="hover:text-cyan-400 transition-colors">📄 総合プライバシーポリシー</a></li>
            <li><a href="https://kawanova.github.io/privacy-policy/" target="_blank" rel="noopener" class="hover:text-cyan-400 transition-colors">📑 全36アプリ個別目録</a></li>
            <li><span class="text-slate-500">外部送信ゼロ・端末内処理保証</span></li>
          </ul>
        </div>

        <div>
          <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">お問い合わせ・フィードバック</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="https://forms.gle/b5uKjXdsNx3BfyiZ7" target="_blank" rel="noopener" class="hover:text-cyan-400 transition-colors">🛠️ 開発者ツール ご意見フォーム</a></li>
            <li><a href="https://forms.gle/kY282TgyFQhc5GCp8" target="_blank" rel="noopener" class="hover:text-cyan-400 transition-colors">🎓 資格対策ドリル ご意見フォーム</a></li>
            <li><a href="https://forms.gle/gWghJ9VtXTc9METz8" target="_blank" rel="noopener" class="hover:text-cyan-400 transition-colors">🎨 ライフスタイル ご意見フォーム</a></li>
          </ul>
        </div>

      </div>

      <div class="pt-8 border-t border-slate-900 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500">
        <p>&copy; 2026 KawaNova. All rights reserved.</p>
        <p class="mt-2 sm:mt-0">Built with Clean Architecture, Kotlin 2.0 & Jetpack Compose</p>
      </div>
    </div>
  </footer>

  <!-- Interactive Logic -->
  <script>
    const apps = {apps_json};
    let currentStatus = 'published'; // Default: Only show 100% working live apps!
    let currentCategory = 'all';
    let currentQuery = '';

    const grid = document.getElementById('appsGrid');
    const noResults = document.getElementById('noResults');
    const countDisplay = document.getElementById('resultsCount');
    const statusDesc = document.getElementById('statusDescription');
    const searchInput = document.getElementById('searchInput');

    function renderApps() {{
      const filtered = apps.filter(app => {{
        const matchesStatus = (currentStatus === 'all' || app.status === currentStatus);
        const matchesCategory = (currentCategory === 'all' || app.category === currentCategory);
        const query = currentQuery.toLowerCase();
        const matchesQuery = !query || 
          app.nameJa.toLowerCase().includes(query) ||
          app.nameEn.toLowerCase().includes(query) ||
          app.catch.toLowerCase().includes(query) ||
          app.benefit.toLowerCase().includes(query) ||
          app.tags.some(t => t.toLowerCase().includes(query));
        return matchesStatus && matchesCategory && matchesQuery;
      }});

      countDisplay.textContent = `表示中: ${{filtered.length}} 件 (全${{apps.length}}作品)`;

      if (filtered.length === 0) {{
        grid.innerHTML = '';
        noResults.classList.remove('hidden');
        return;
      }}

      noResults.classList.add('hidden');
      grid.innerHTML = filtered.map(app => {{
        // Feature Graphic (1024x500 banner)
        const featureImgHtml = app.featureImage
          ? `<div class="w-full h-44 overflow-hidden rounded-t-2xl relative bg-slate-950">
               <img src="${{app.featureImage}}" alt="${{app.nameJa}} フィーチャーグラフィック" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
               <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent opacity-80"></div>
             </div>`
          : `<div class="w-full h-44 bg-gradient-to-r from-slate-900 to-slate-800 rounded-t-2xl flex items-center justify-center text-4xl">
               ${{app.fallbackEmoji}}
             </div>`;

        // Status Badge & Action Button
        let statusBadge = '';
        let actionButton = '';

        if (app.status === 'published') {{
          statusBadge = `<span class="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center space-x-1">
                           <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                           <span>🟢 製品版 公開中</span>
                         </span>`;
          actionButton = `<a href="https://play.google.com/store/apps/details?id=${{app.pkg}}" target="_blank" rel="noopener" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-sky-500 hover:from-cyan-400 hover:to-sky-400 text-slate-950 font-bold text-xs flex items-center justify-center space-x-1.5 shadow-md shadow-cyan-500/20 transition-all">
                            <span>Google Play でインストール ↗</span>
                          </a>`;
        }} else if (app.status === 'beta') {{
          statusBadge = `<span class="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-500/10 text-amber-400 border border-amber-500/30 flex items-center space-x-1">
                           <span>🧪 クローズドテスト中</span>
                         </span>`;
          actionButton = `<a href="#betalab" class="w-full py-2.5 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 border border-amber-500/40 font-bold text-xs flex items-center justify-center space-x-1.5 transition-all">
                            <span>🧪 先行ベータ版を試す（案内へ）</span>
                          </a>`;
        }} else {{
          statusBadge = `<span class="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-slate-800 text-slate-400 border border-slate-700">
                           <span>🚀 開発完了・近日公開</span>
                         </span>`;
          actionButton = `<div class="w-full py-2.5 rounded-xl bg-slate-800/80 text-slate-400 text-center font-medium text-xs border border-slate-700/60 select-none">
                            <span>ストア審査準備中 (Coming Soon)</span>
                          </div>`;
        }}

        const privacyLink = `https://kawanova.github.io/privacy-policy/android-${{app.slug}}.html`;
        const feedbackLink = getFeedbackLink(app);

        const tagsHtml = app.tags.slice(0, 4).map(t => 
          `<span class="px-2 py-0.5 rounded text-[11px] font-medium bg-slate-800 text-slate-300 border border-slate-700/60">${{t}}</span>`
        ).join('');

        return `
          <div class="bg-slate-900/90 rounded-2xl border border-slate-800 hover:border-slate-700 flex flex-col justify-between transition-all hover:-translate-y-1 hover:shadow-2xl hover:shadow-cyan-500/5 group">
            
            <!-- Top Feature Graphic -->
            ${{featureImgHtml}}

            <!-- Content Body -->
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between gap-2 mb-2.5">
                  <span class="text-xs font-semibold text-cyan-400">${{app.categoryLabel}}</span>
                  ${{statusBadge}}
                </div>

                <h3 class="font-bold text-white text-base leading-snug group-hover:text-cyan-300 transition-colors mb-1">
                  ${{app.nameJa}}
                </h3>
                <p class="text-xs text-slate-400 font-mono mb-3">${{app.nameEn}}</p>

                <div class="bg-slate-950/60 rounded-xl p-3 border border-slate-800/80 mb-4">
                  <p class="text-xs font-semibold text-cyan-300 mb-1 leading-snug">
                    ${{app.catch}}
                  </p>
                  <p class="text-xs text-slate-300 leading-relaxed">
                    ${{app.benefit}}
                  </p>
                </div>

                <div class="flex flex-wrap gap-1.5 mb-5">
                  ${{tagsHtml}}
                </div>
              </div>

              <!-- Bottom Actions -->
              <div>
                <div class="mb-3">
                  ${{actionButton}}
                </div>

                <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
                  <a href="${{privacyLink}}" target="_blank" rel="noopener" class="hover:text-slate-200 transition-colors">
                    📄 プライバシーポリシー
                  </a>
                  <a href="${{feedbackLink}}" target="_blank" rel="noopener" class="hover:text-cyan-400 transition-colors">
                    ✍️ 要望・報告
                  </a>
                </div>
              </div>

            </div>

          </div>
        `;
      }}).join('');
    }}

    function getFeedbackLink(app) {{
      const enc = encodeURIComponent;
      if (app.formType === 'dev') {{
        return `https://docs.google.com/forms/d/e/1FAIpQLSeAKUuGOlBBI4bR7DwF0Ji6xPk20A19-asM1VWQG1pcAG4BLg/viewform?usp=pp_url&entry.447629162=${{enc(app.nameEn + ' (' + app.nameJa + ')')}}`;
      }} else if (app.formType === 'exam') {{
        return `https://docs.google.com/forms/d/e/1FAIpQLSeiqpItf9qamM89uDsmM15ERo4xl5RDqrVD6IHE2ZqXDs2rxA/viewform?usp=pp_url&entry.661639264=${{enc(app.nameJa)}}`;
      }} else {{
        return `https://docs.google.com/forms/d/e/1FAIpQLSe0rmuJ5IW3UGm72ax_q1gBPgxmYM5kNV9zDAqzNLyqyFqKog/viewform?usp=pp_url&entry.355175170=${{enc(app.nameEn + ' (' + app.nameJa + ')')}}`;
      }}
    }}

    function filterStatus(status) {{
      currentStatus = status;
      document.querySelectorAll('.status-tab').forEach(t => {{
        t.className = 'status-tab px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all flex items-center space-x-1.5';
      }});
      const activeTab = document.getElementById(`status-tab-${{status}}`);
      if (activeTab) {{
        if (status === 'published') {{
          activeTab.className = 'status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20 transition-all flex items-center space-x-1.5';
          statusDesc.textContent = '現在「🟢 今すぐ使える公開中アプリ」を表示しています';
          statusDesc.className = 'text-emerald-400 font-medium';
        }} else if (status === 'beta') {{
          activeTab.className = 'status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-amber-500 text-slate-950 shadow-md shadow-amber-500/20 transition-all flex items-center space-x-1.5';
          statusDesc.textContent = '現在「🧪 ベータテスト中アプリ（先行体験）」を表示しています';
          statusDesc.className = 'text-amber-400 font-medium';
        }} else if (status === 'coming_soon') {{
          activeTab.className = 'status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-sky-500 text-slate-950 shadow-md shadow-sky-500/20 transition-all flex items-center space-x-1.5';
          statusDesc.textContent = '現在「🚀 開発中・近日公開ラインナップ」を表示しています';
          statusDesc.className = 'text-sky-400 font-medium';
        }} else {{
          activeTab.className = 'status-tab px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-cyan-500 text-slate-950 shadow-md shadow-cyan-500/20 transition-all flex items-center space-x-1.5';
          statusDesc.textContent = '全36作品を表示しています';
          statusDesc.className = 'text-cyan-400 font-medium';
        }}
      }}
      renderApps();
    }}

    function filterCategory(cat) {{
      currentCategory = cat;
      document.querySelectorAll('.cat-pill').forEach(t => {{
        t.className = 'cat-pill px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700 hover:border-slate-600 transition-all';
      }});
      const active = document.getElementById(`cat-tab-${{cat}}`);
      if (active) {{
        active.className = 'cat-pill px-3 py-1.5 rounded-lg text-xs font-bold bg-cyan-500 text-slate-950 transition-all';
      }}
      renderApps();
    }}

    searchInput.addEventListener('input', (e) => {{
      currentQuery = e.target.value.trim();
      renderApps();
    }});

    // Initial render (defaults to published 6 apps!)
    renderApps();
  </script>
</body>
</html>
"""

    out_file = os.path.join(ROOT_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated index.html at {out_file}")

if __name__ == "__main__":
    generate_html()
