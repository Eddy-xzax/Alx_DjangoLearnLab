from django.urls import path
from .views import UserListView, FollowUserView, UnfollowUserView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]
