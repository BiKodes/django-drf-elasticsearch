from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Article, Category
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import (
    CategoryIndex,
    ArticleIndex,
    UserIndex,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"

class UserHayStackSerializer(HaystackSerializer):
    class Meta:
        index_classes = [UserIndex]
        fields = [
            "first_name",
            "last_name",
            "username",
        ]

class CategoryHayStackSerializer(HaystackSerializer):
    class Meta:
        index_classes = [CategoryIndex]
        fields = ["id", "description"]

class ArticleHayStackSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ArticleIndex]
        fields = [
            "title",
            "type",
            "author",
            "categories",
            "content",
            "created_datetime",
            "updated_datetime",
        ]