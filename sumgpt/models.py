from django.db import models
from django.contrib.auth.models import User

#GoogleDocument保存用
class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url

#要約データ保存用
class Sum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.TextField()
    detail = models.CharField(max_length=10000, default="データなし")
    timestamp = models.DateTimeField(auto_now_add=True)

#文字起こし用のテーブル作成
class Upload(models.Model):
    document = models.FileField(upload_to='media')
    uploaded_at = models.DateTimeField(auto_now_add=True)