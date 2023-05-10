from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForiegnKey(User, on_delete=models.CASCADE) #cascade will remove all the post done by author if author is removed
    body = models.TextField()

    def __str__(self):
        return title + "|" + self.author
