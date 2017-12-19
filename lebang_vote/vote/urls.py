#!coding:utf8
# create by  @
from django.conf.urls import url, include
from .apis import router, user_vote
from .views import TplView


urlpatterns = [
    url(r'^vote$', user_vote),
    url(r'^tpl/(\w+)$', TplView.as_view(), name="tpl"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]