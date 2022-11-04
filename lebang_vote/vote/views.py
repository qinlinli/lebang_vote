#!coding:utf8
from django.views.generic import View
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TplView(View):
    @method_decorator(login_required)
    def get(self, request, tpl_name):
        tpl_name = "vote/%s.html" % tpl_name
        return render_to_response(tpl_name)
print(111)
