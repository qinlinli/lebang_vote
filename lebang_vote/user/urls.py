#!coding:utf8

from django.conf.urls import url
from .views import UserAutoSignView


urlpatterns = [
    url(r'token', UserAutoSignView.as_view(), name='user.token'),
]