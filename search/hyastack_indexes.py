"""This brings in the implementation of DRF Haystack.

Elastic search will be able to index and query the data 
based the index classes.
 """
from haystack import indexes

from django.contrib.auth.models import User
import datetime
from ..blog.models import Article, Category

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """Article indexing setup."""

    title = indexes.CharField(model_attr="title")
    type = indexes.CharField(model_attr="type")
    author = indexes.CharField(model_attr="author")
    categories = indexes.CharField(model_attr="categories__name")
    content = indexes.CharField(model_attr="description")
    created_datetime = indexes.DateTimeField(model_attr="created_datetime")
    updated_datetime = indexes.DateTimeField(model_attr="updated_datetime")

    def prepare_author(self, obj):
        return obj.author.username
    
    def get_model(self):
        return Article
    
    def index_queryset(self, using=None):
        """Used when the entire index for Article is updated."""
        return self.get_model().objects.filter(
            created_datetime__lte=datetime.datetime.now()
        )

class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    """Category indexing setup."""
    id = indexes.IntegerField(model_attr="id")
    description = indexes.CharField(model_attr="id")

    def get_model(self):
        return Category
    
    def index_queryset(self, using=None):
        """Used when the entire index for Category is updated."""
        return self.get_model().objects.all()

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    """User indexing setup."""
    first_name = indexes.CharField(model_attr="first_name")
    last_name = indexes.CharField(model_attr="last_name")
    username = indexes.CharField(model_attr="username")

    def get_model(self):
        return User
    
    def index_queryset(self, using=None):
        """Used when the entire index for User is updated."""
        return self.get_model().objects.all()

