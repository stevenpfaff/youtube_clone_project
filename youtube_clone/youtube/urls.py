from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.CommentList.as_view())
]
