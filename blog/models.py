from django.db import models
from django.contrib.auth.models import User
from blog.constants import ARTICLE_TYPES

class Category(models.Model):
    """ Represents an article category.
    e.g., programming, Linux, testing.
    """
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def type_to_string(self):
        if self.type == "UN":
            return "Unspecified"
        if self.type == "TU":
            return "Tutorial"
        if self.type == "RS":
            return "Research"
        if self.type == "RW":
            return "Review"

    def __str__(self) -> str:
        """Represent a category with a name."""
        return f"{self.name}"
    
class Article(models.Model):
    """Represents an individual article. Each article can have multiple categories. 
    Articles have a specific type -- Tutorial, Research, Review, or Unspecified.
    """
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default="UN")
    categories = models.ManyToManyField(to=Category, blank=True, related_name="categories")
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Represent an article with authoe name and date."""
        return f"{self.author}: {self.title} ({self.created_datetime.date()})"
