from django.db import models

class Comment(models.Model): 
    comment_text = models.CharField(max_length=300)
    likes = models.IntegerField(100)
    dislikes = models.IntegerField(100)
    video_id = models.CharField(max_length=300)

class Reply(models.Model):
    reply_text = models.CharField(max_length=300)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
