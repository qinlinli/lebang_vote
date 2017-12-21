#!coding:utf8
# create by  @
import logging
import re
from .exceptions import VoteError
from django.http import JsonResponse
from .services import CounterService

REGEX = re.compile(r'^/game/api/(options/\d+|games/\d+)')


class VoteErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, VoteError):
            return JsonResponse({"code": 1, "error": exception.message})
        return None


class VisitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        ret = REGEX.findall(request.path)
        if ret:
            cs = CounterService(ret[0])
            cs.add()
        return self.get_response(request)
