
import math

from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = settings.REST_FRAMEWORK['PAGE_SIZE']


class CustomPagination(pagination.PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # if you want to show page size in resposne just add these 2 lines
        if self.request.query_params.get('page_size'):
            self.page_size = int(self.request.query_params.get('page_size'))

        # you can count total page from request by total and page_size
        total_page = math.ceil(self.page.paginator.count /  # type: ignore
                               self.page_size)

        return Response({
            'count': self.page.paginator.count,  # type: ignore
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_page': total_page,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })
