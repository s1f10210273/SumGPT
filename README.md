# SumGPT
会議の恋人を目指していきたい

## 立ち上げ方
### 1. 仮想環境の作成
```
python -m venv venv
```
### 2. 仮想環境に入る
mac
```
source venv/bin/activate
```
windows
```
./venv/Scripts/activate
```
### 3. 必要なライブラリのインストール
音声文字起こし用のライブラリ
```
pip install SpeechRecognition
```
ChatGPT用
```
pip install openai
```
.envの読み込み
```
pip install python-dotenv
```
### 4. 環境変数の設定
ルートディレクトリ直下に`.env`ファイルを作成し、以下の内容を記述
```
OPENAI_API_KEY=<自分のAPIkey>
```
### 5. マイグレーション
```
python manage.py makemigrations
python manage.py migrate
```
### 6. サーバー立ち上げ
```
python manage.py runserver
```
