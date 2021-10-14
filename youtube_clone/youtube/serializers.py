from rest_framework import serializers
from .models import Comment
from .models import Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["comment_text", "likes", "dislikes", "video_id"]

class ReplySerializer(serializers.ModelSerializer):
    class Meta :
        model = Reply
        fields = ["reply_text", "comment_id"]