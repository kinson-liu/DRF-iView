from rest_framework.pagination import PageNumberPagination



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        return {
            'pages': self.page.paginator.count // self.page_size + 1,
            'results': data
        }