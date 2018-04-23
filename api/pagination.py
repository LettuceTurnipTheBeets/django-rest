from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomListPagination(LimitOffsetPagination):
    """Force pagination on List views"""
    def get_paginated_response(self, data):
        return Response({
            'status': "OK",
            'list': data,
        })

class CustomDetailPagination(LimitOffsetPagination):
    """Force pagination on Detail views"""
    def get_paginated_response(self, data):
        return Response({
            'status': "OK",
            'animal': data,
        })
