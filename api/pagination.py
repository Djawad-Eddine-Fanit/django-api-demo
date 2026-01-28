from rest_framework.pagination import PageNumberPagination

class DynamicPagination(PageNumberPagination):
    page_size = 10  # The default
    page_size_query_param = 'page_size'  # The URL parameter name
    max_page_size = 100  # Security limit: don't let them ask for 1,000,000