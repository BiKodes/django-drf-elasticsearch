"""This brings in the implementation of DRF Haystack.

Elastic search will be able to index and query the data 
based the index classes.
 """
from haystack import indexes

from django.contrib.auth.models import User
from django.utils import timezone
from .models import Article, Category

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """Article indexing setup."""

    title = indexes.CharField(model_attr="title")
    type = indexes.CharField(model_attr="type")
    author = indexes.CharField(model_attr="author")
    categories = indexes.CharField(model_attr="categories__name")
    content = indexes.TextField(model_attr="description")
    created_datetime = indexes.DateTimeField(model_attr="created_datetime")
    updated_datetime = indexes.DateTimeField(model_attr="updated_datetime")

    def prepare_author(self, obj):
        return obj.author.username
    
    def get_model(self):
        return Article

class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    """Category indexing setup."""
    id = indexes.IntegerField(model_attr="id")
    description = indexes.CharField(model_attr="id")

    def get_model(self):
        return Category

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    """User indexing setup."""
    id = indexes.IntegerField(model_attr="id")
    first_name = indexes.CharField(model_attr="first_name")
    last_name = indexes.CharField(model_attr="last_name")
    username = indexes.CharField(model_attr="username")

    def get_model(self):
        return User

