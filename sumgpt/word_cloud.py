#wordcloud用pythonファイル
#実用版。
#画像を除くWordCloud_mのフィールドの要素を貰い、その中のテキスト（origin）からワードクラウドを作成。
#その後、貰った要素と合わせてWordCloud_mのモデルのインスタンスを作成し、保存。そのidを返す。

from .models import WordCloud_m#model保存のため
from django.core.files import File #上に同じ

import os 
from django.conf import settings

from janome.tokenizer import Tokenizer #文字の分解（品詞）
import re #文字の分解
from wordcloud import WordCloud #wordcloud


#静的ファイルをviewsで直接指定する場合にのみ必要
from django.contrib.staticfiles import finders

def WC(user, origin, sum, exclusion = []):# WordCloud_mのと、除外ワードを指定してWordCloudを作成する関数

    #exclusion で除外ワードを作成し、品詞分解
    token = Tokenizer().tokenize(origin)
    word = []
    
    for line in token:
        tkn = re.split('\t|,', str(line))
        # 名詞のみ対象 tkn[0]に単語そのもの、tkn[1], tkn[2]が一般的な”名詞”の条件
        if tkn[0] not in exclusion and tkn[1] in ['名詞'] and tkn[2] in ['一般', '固有名詞'] :
            word.append(tkn[0])
    
    words = ' ' . join(word)#引数のリストを' 'でつないで文字列にする。

    font_path = finders.find('fonts/NotoSerifJP-Regular.otf') 
    w = WordCloud(font_path, width=800, height=600, background_color='white', min_font_size = 15)
    w.generate(words)

    new_instance = WordCloud_m.objects.create(user=user, origin=origin, sum=sum);
    id = new_instance.id #WordCloud固有のidを取得→画像url作成に活用。
    
    # ワードクラウド画像をファイルに保存
    path = f'{settings.MEDIA_ROOT}/word_cloud/{id}_wordcloud.png'
    w.to_file(path)
    
    # モデルに保存
    with open(path, 'rb') as file:
        new_instance.image.save(f'no_{id}.png', File(file), save=True)
        
    os.remove(path)
        
    return id
