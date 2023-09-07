from django.db import models
from django.contrib.auth.models import User

class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url