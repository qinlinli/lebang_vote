#!coding:utf8
# create by  @
from .exceptions import VoteError
from django.http import JsonResponse


class VoteErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self.get_response(request)


    def process_exception(self, request, exception):
        if isinstance(exception, VoteError):
            return JsonResponse({"code": 1, "message": exception.message})
        return None
