#!coding:utf8


from django.views.generic import View
from django.shortcuts import render_to_response


class TplView(View):
    def get(self, request, tpl_name):
        tpl_name = "vote/%s.html" % tpl_name
        return render_to_response(tpl_name)
