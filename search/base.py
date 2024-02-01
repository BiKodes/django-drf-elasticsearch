import abc
from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action


class BaseElasticSearchAPIView(viewsets.ModelViewSet, LimitOffsetPagination):
    """Elastic Base Search View."""
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression.
        """

    @action(detail=False, methods=['get'])
    def search(self, request):
        try:
            params: dict = request.query_params
            query = params.get("search")

            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)

            response = search.execute()

            print(f"Found {response.hit.total.value} hit(s) for query: '{query}'")

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            
            return self.get_paginated_response(serializer.data)
        
        except Exception as e:
            return HttpResponse(e, status=500)