from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions
from .serializers import PostSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from rest_framework import generics
from .models import Post

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        return generics.get_object_or_404(Post, pk=pk)

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # 1. Get the post or return 404
        post = get_object_or_404(Post, pk=pk)

        # 2. Like or get existing like
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # 3. Send a notification to the post owner (if not the same user)
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post
                )
            return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Already liked"}, status=status.HTTP_200_OK)

class FollowingPostsView(generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # get all the users the current user follows
        following_users = request.user.following.all()

        # filter posts by those users and order them (latest first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
