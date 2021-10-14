from .models import Comment
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Reply

class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.filter(Comment.video_id)
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ReplyList(APIView):
    def get(self, request):
        reply = Reply.objects.filter(Reply.comment_id)
        serializer = ReplySerializer(reply, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)