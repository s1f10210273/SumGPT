#wordcloud実行用テストファイル
from . import word_cloud

print("test")
word_cloud.WC(".\static\sumgpt\text\sample.txt", ".\static\sumgpt\img\sample.png") #入力ファイル名、出力ファイル名
