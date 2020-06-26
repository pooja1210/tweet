from django.urls import path
from django import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    UserPostListView,
    FollowsListView,
    FollowersListView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),
    # path('detail/<int:id>/', post_detail, name='detail'),
    
    
]