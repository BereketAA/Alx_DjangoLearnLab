from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        data = [
            {
                'actor': notification.actor.username,
                'verb': notification.verb,
                'timestamp': notification.timestamp,
                'is_read': notification.is_read,
                'target': str(notification.target),
            }
            for notification in notifications
        ]
        return Response(data)

    def post(self, request):
        # Mark all notifications as read
        Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return Response({'message': 'All notifications marked as read'})
