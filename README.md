# SumGPT
## 1. 仮想環境の作成
```
python -m venv venv
```

## 2. 仮想環境に入る
windowsだとコマンド違うかも
```
source venv/bin/activate
```

## 3. 必要なライブラリのインストール
音声文字起こし用のライブラリ
```
pip install SpeechRecognition
```

## 4. マイグレーション
```
python manage.py migrate
```

## 5. サーバー立ち上げ
```
python manage.py runserver
```
