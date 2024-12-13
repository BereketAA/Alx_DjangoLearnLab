from django.urls import path
from .views import register_user, login_user, user_profile
from .views import FollowViewSet
from .views import FollowUserView, UnfollowUserView

follow_view = FollowViewSet.as_view({
    'post': 'follow_user',
    'delete': 'unfollow_user'
})

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', user_profile, name='profile'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]