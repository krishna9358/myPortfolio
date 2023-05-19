from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255, default="This is pre defined title")
    author = models.ForeignKey(User, on_delete=models.CASCADE) #cascade will remove all the post done by author if author is removed
    body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.author)
