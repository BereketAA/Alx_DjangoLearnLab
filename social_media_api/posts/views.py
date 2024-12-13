from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment , Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

CustomUser = get_user_model()

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        
        feed_data = [
            {
                "id": post.id,
                "author": post.author.username,
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at,
            }
            for post in posts
        ]
        return Response(feed_data)
        
        
        
class LikeView(APIView):
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            like, created = Like.objects.get_or_create(post=post, user=request.user)
            if created:
                # Create a notification for the post author
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post,
                )
                return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'Post already liked'}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            like = Like.objects.filter(post=post, user=request.user).first()
            if like:
                like.delete()
                return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'message': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)