# paginations.py

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
            'limit': self.limit
        })
