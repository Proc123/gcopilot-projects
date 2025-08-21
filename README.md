# GCopilot Projects Collection 🚀

このリポジトリは、GitHub Copilotを使用して作成された様々なPythonプロジェクトのコレクションです。

## 🎯 プロジェクト概要

GitHub Copilotの学習と実践を通じて作成された、ゲーム、ユーティリティ、学習プログラムなどが含まれています。各プロジェクトは独立して動作し、学習目的や実用的なツールとして使用できます。

## 📁 プロジェクト構成

### 🎮 ゲーム (`games/`)
- **Blackjack** (`blackjack.py`) - ブラックジャックゲーム（日本語対応）
- **Number Guessing Game** (`number_guessing_game.py`) - 1-100の数字当てゲーム
- **Shiritori** (`shiritori.py`) - しりとりゲーム

### 🛠️ ユーティリティ (`utilities/`)
- **BMI Calculator** (`bmi.py`) - BMI計算と判定
- **Temperature Converter** (`temperature_converter.py`) - 摂氏⇔華氏変換
- **Password Generator** (`password_generator.py`) - セキュアなパスワード生成
- **Prime Checker** (`prime_checker.py`) - 素数判定と素因数分解
- **Basic Calculator** (`calculate.py`) - 基本計算機

### ⏰ タイマー・カウントダウン (`timers/`)
- **Countdown Timer** (`countdown_timer.py`) - コンソールベースのカウントダウン

### 🧮 アルゴリズム (`algorithms/`)
- **Quick Sort** (`quick_sort.py`) - クイックソートの実装

### 🌐 Web・API (`web/`)
- **Web Timer** (`web_timer/`) - HTML/CSS/JavaScript製のWebタイマー
- **Django Project** (`django_project/`) - Django Webアプリケーションの基本構造
- **Cat Image API** (`api_cat.py`) - 猫画像APIクライアント

### 📚 学習・サンプル (`learning/`)
- **Machine Learning** (`machine_learning.py`) - 線形回帰のサンプル

### 📋 検査仕様書 (`docs/`)
各プログラムの動作確認方法と期待される結果を記載した詳細な検査仕様書

## 🚀 使用方法

### 基本的な実行方法
```bash
# ゲームの実行例
python games/blackjack.py
python games/number_guessing_game.py

# ユーティリティの実行例
python utilities/bmi.py
python utilities/temperature_converter.py

# タイマーの実行例
python timers/countdown_timer.py
```

### Webアプリケーションの実行
```bash
# Djangoプロジェクト
cd web/django_project
pip install django
python manage.py runserver

# Webタイマー
# web/web_timer/index.html をブラウザで開く
```

### 必要な依存関係
```bash
pip install requests matplotlib scikit-learn numpy
```

## 📋 検査仕様書

各プログラムには詳細な検査仕様書が含まれており、以下の項目が記載されています：
- プログラムの概要
- 検査項目と期待される動作
- 具体的な検査手順
- エラー処理の確認方法

## 🛠️ 技術スタック

- **言語**: Python 3.x
- **フレームワーク**: Django
- **ライブラリ**: 
  - 標準ライブラリ: random, time, string, math
  - 外部ライブラリ: requests, matplotlib, scikit-learn, numpy
- **フロントエンド**: HTML5, CSS3, JavaScript (ES6+)
- **ツール**: GitHub Copilot

## 🎨 特徴

- **日本語対応**: 多くのプログラムが日本語で動作
- **教育目的**: 学習しやすい構造とコメント
- **実用性**: 実際に使用できるツール
- **包括性**: 様々な分野のプログラムを網羅

## 📝 ライセンス

このプロジェクトは学習目的で作成されています。

## 🤝 貢献

改善提案やバグ報告は歓迎します。IssueやPull Requestをお気軽にお送りください。

## 📞 連絡先

GitHub: [@Proc123](https://github.com/Proc123)

## 🔄 更新履歴

- **2025-08-21**: 初回リリース
  - ゲーム、ユーティリティ、Webアプリケーションを追加
  - 検査仕様書を追加
  - 包括的なREADMEを作成

---

*このリポジトリは、GitHub Copilotの学習成果として作成されました。各プログラムは独立して動作し、学習や実用に活用できます。*