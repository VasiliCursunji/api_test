from rest_framework import pagination


class PaginationProduct(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 1000
