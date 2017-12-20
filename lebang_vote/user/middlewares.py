#!coding:utf8
# create by  @
from .exceptions import UserException
from django.http import JsonResponse


class VoteErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self.get_response(request)


    def process_exception(self, request, exception):
        if isinstance(exception, UserException):
            return JsonResponse({"code": exception.error_code, "error": exception.message})
        return None
