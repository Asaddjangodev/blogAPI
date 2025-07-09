from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from rest_framework.permissions import IsAdminUser

from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer, UserSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


#class PostList(generics.ListCreateAPIView):
#    permission_classes = (IsAuthorOrReadOnly,) # new
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer


#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#    permission_classes = (IsAuthorOrReadOnly,) # new
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

#class UserList(generics.ListCreateAPIView):
#    queryset = get_user_model().objects.all()
#    serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = get_user_model().objects.all()
#    serializer_class = UserSerializer