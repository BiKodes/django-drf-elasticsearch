from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from blog.models import Category, Article
from blog.serializers import (
    CategorySerializer,
    ArticleSerializer,
    UserSerializer,
    CategoryHayStackSerializer,
    ArticleHayStackSerializer,
    UserHayStackSerializer,
)
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['get'], serializer_class=UserHayStackSerializer)
    def search_index_user(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=True, methods=['get'], serializer_class=CategoryHayStackSerializer)
    def search_index_category(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


    @action(detail=True, methods=['get'], serializer_class=ArticleHayStackSerializer)
    def search_index_article(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

