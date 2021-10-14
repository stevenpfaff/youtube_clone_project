from django.urls import path
from . import views

urlpatterns = [
    path('youtube/comment/', views.CommentList.as_view()),          # Post
    path('youtube/comment/<int:video_id>/', views.CommentList.as_view()), # Get all by video
    path('youtube/reply/', views.ReplyList.as_view()),               # GET one and Post
    path('youtube/reply/<int:comment_id>/', views.ReplyList.as_view())      # get all by comment
]
