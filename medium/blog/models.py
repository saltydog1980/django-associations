from django.db import models

# Create your models here.


class User(models.Model):
    pass

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="posts")

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="comments")
