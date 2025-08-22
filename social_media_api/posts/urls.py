from django.urls import path
from .views import FollowingPostsView

urlpatterns = [
    path("feed/", FollowingPostsView.as_view(), name="feed"),
]
