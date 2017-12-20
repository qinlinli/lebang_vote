#!coding:utf8
# create by  @
from django.views.generic import View
from django.shortcuts import redirect
from .services import oauth_client_service, LebangUserService


class UserAutoSignView(View):
    """
    auto signin with lebang Oauth2
    """
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("/game/tpl/index")
        if not request.GET.get("code"):
            # 初次访问, 当然这样干是不对的
            return redirect(oauth_client_service.oauth_url)

        tokens = oauth_client_service.fetch_token(request.GET.get("code"))
        lebang_service = LebangUserService(tokens.get("access_token"))
        lebang_service.bind_user()
        return redirect("/game/tpl/index")
