from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    default_limit = 4
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 3


class PartnerResultsSetPagination(PageNumberPagination):
    default_limit = 100
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 100
