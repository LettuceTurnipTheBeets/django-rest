from rest_framework.pagination import LimitOffsetPagination, BasePagination
from rest_framework.response import Response

class CustomListPagination(LimitOffsetPagination):
    """Force pagination on List views"""
    def get_paginated_response(self, data):
        return Response({
            'status': "OK",
            'list': data,
        })

class CustomDetailPagination(BasePagination):
    """Force pagination on Detail views"""
    def get_paginated_response(self, data):
        return Response({
            'status': "OK",
            'animal': data,
        })
