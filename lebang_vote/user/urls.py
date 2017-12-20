#!coding:utf8

from django.conf.urls import url
from .views import UserAutoSignView, UserSignoutView


urlpatterns = [
    url(r'token', UserAutoSignView.as_view(), name='user.token'),
    url(r'logout', UserSignoutView.as_view(), name='user.logout'),
]