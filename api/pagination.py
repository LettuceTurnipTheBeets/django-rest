from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomPagination(LimitOffsetPagination):
    """Force pagination"""
    def get_paginated_response(self, data):
        return Response({
            'status': "OK",
            'list': data
        })
