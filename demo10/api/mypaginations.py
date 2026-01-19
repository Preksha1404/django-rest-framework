from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'p'
#     page_size_query_param = 'records'
#     max_page_size = 10

# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'records'
#     offset_query_param = 'start'
#     max_limit = 10

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'roll_number'
    cursor_query_param = 'record_cursor'