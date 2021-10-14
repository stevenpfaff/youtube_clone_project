from django.urls import path
from . import views

urlpatterns = [
    path('youtube/comment/', views.CommentList.as_view()),          # Post
    path('youtube/comment/<int:pk>/', views.CommentDetail.as_view()), # Get all by video
    path('youtube/comment/reply/', views.ReplyDetail.as_view()),               # GET one and Post      # get all by comment
]
