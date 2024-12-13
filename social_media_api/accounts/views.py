from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    """Handle user registration and return an authentication token."""
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username is already taken."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"message": "User registered successfully.", "token": token.key}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    """Handle user login and return an authentication token."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"message": "Login successful.", "token": token.key}, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_profile(request):
    """Return user profile details for authenticated users."""
    if not request.user.is_authenticated:
        return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({
        "username": request.user.username,
        "email": request.user.email,
        "date_joined": request.user.date_joined,
    }, status=status.HTTP_200_OK)


