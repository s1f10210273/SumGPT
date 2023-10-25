#wordcloud用pythonファイル

import codecs #ファイルを開く
from janome.tokenizer import Tokenizer #文字の分解（品詞）
import re #文字の分解
from wordcloud import WordCloud #wordcloud

exclude = [] #変更箇所。除くワード
filename = ()

def WC(filename, export, exclusion = []):# 入力ファイル、出力ファイル、除外ワードを指定してWordCloudを作成する関数
    with codecs.open(filename,'r','utf-8','ignore') as f:
        text = f.read()
    print("file readed")

    #exclusion で除外ワードを作成し、品詞分解
    token = Tokenizer().tokenize(text)
    word = []
    
    for line in token:
        tkn = re.split('\t|,', str(line))
        # 名詞のみ対象 tkn[0]に単語そのもの、tkn[1], tkn[2]が一般的な”名詞”の条件
        if tkn[0] not in exclusion and tkn[1] in ['名詞'] and tkn[2] in ['一般', '固有名詞'] :
            word.append(tkn[0])
    
    words = ' ' . join(word)#引数のリストを' 'でつないで文字列にする。
    print("text")

    w = WordCloud(font_path='.\\static\\fonts\\NotoSerifJP-Regular.otf', width=800, height=600, background_color='white', min_font_size = 15)#fontファイル
    w.generate(words)
    w.to_file(export)
    print("img")