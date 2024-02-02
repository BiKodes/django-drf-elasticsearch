from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from blog.models import Category, Article
from blog.serializers import (
    CategorySerializer,
    ArticleSerializer,
    UserSerializer,
    # CategoryHayStackSerializer,
    # ArticleHayStackSerializer,
    # UserHayStackSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from elasticsearch_dsl import Q
from search.base import BaseElasticSearchAPIView
from search.documents import (
    UserDocument,
    CategoryDocument,
    ArticleDocument,
)


class UserViewSet(viewsets.ModelViewSet, BaseElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument
    queryset = User.objects.all()

    # @action(detail=True, methods=['get'], serializer_class=UserHayStackSerializer)
    # def search_index_user(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def generate_q_expression(self, query):
        return Q("bool",
                 should=[
                    Q("match", username=query),
                    Q("match", first_name=query),
                    Q("match", last_name=query)
                 ], minimum_should_match=1
        )
    


class CategoryViewSet(viewsets.ModelViewSet, BaseElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument
    queryset = Category.objects.all()

    # @action(detail=True, methods=['get'], serializer_class=CategoryHayStackSerializer)
    # def search_index_category(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def generate_q_expression(self, query):
        return Q(
            "multi_match", query=query,
            fields=[
                "name",
                "description",
            ], fuzziness="auto")

class ArticleViewSet(viewsets.ModelViewSet, BaseElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument
    queryset = Article.objects.all()


    # @action(detail=True, methods=['get'], serializer_class=ArticleHayStackSerializer)
    # def search_index_article(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    def generate_q_expression(self, query):
        return Q(
            "multi_match", query=query,
            fields=[
                "title",
                "author",
                "type",
                "content"
            ], fuzziness="auto")
