from django.urls import path
from . import views

urlpatterns = [
    path('youtube/comment/', views.CommentList.as_view()),
    path('youtube/reply/', views.ReplyList.as_view())
]
