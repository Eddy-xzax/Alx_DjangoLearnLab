from django.urls import path
from .views import FollowingPostsView

urlpatterns = [
    path("feed/", FollowingPostsView.as_view(), name="feed"),
    path('<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike-post'),
]
