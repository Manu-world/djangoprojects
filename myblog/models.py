from django.conf import settings
from django.db import models
from django.utils import timezone

# class Post(models.Model):
#   author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#   title = models.CharField(max_length=200)
#   text = models.TextFie
    
#   def __str__(self):
#     return self.title

class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=120)
    detail = models.TextField()

    def __str__(self) -> str:
        return self.task