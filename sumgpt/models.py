from django.db import models
from django.contrib.auth.models import User

#要約データ保存用
class Sum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.TextField()
    detail = models.CharField(max_length=10000, default="データなし")
    timestamp = models.DateTimeField(auto_now_add=True)

#GoogleDocument保存用
class Doc(models.Model):
    sum = models.OneToOneField(Sum, on_delete=models.CASCADE, default=1)
    url = models.URLField()

    def __str__(self):
        return self.url

#文字起こし用のテーブル作成
class Upload(models.Model):
    document = models.FileField(upload_to='media')
    uploaded_at = models.DateTimeField(auto_now_add=True)

#wordcloud用テーブル(文字起こしデータ、要約データから参照されるべき。どちらも元が消えると消える。)

class WordCloud_m(models.Model):
    #Userと紐づければ画像一覧でも表示できそう。そうでなくても、ユーザーが消えたら消すべきだから、入れる必要あり。
    #外部キーのフィールドはインスタンスそのものを入れなくてはいけない。そのインスタンスのidを数字として入れることはできない。
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    origin = models.TextField()#SpeechRecognition.pyのinput_dataを登録する。
    sum = models.ForeignKey(Sum, on_delete=models.CASCADE, related_name='word_cloud')#紐づけ用(Sum_instance.word_cloud.all() のように使用。)
    image = models.ImageField(upload_to='word_cloud')

    
#wordcloud用テーブル(画像とidのみ）後で消す。
class WordCloud_test(models.Model):
    image = models.ImageField(upload_to='word_cloud')