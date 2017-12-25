#!coding:utf8
# create by  @
from django.views.generic import View
from django.shortcuts import redirect
from .services import oauth_client_service, LebangUserService
from django.contrib.auth import logout


class UserAutoSignView(View):
    """
    auto signin with lebang Oauth2
    """
    def get(self, request):
        route = None
        route = route[0] if route else ""
        if request.user.is_authenticated():
            return redirect(request.GET.get("next") or "/game/tpl/index#"+route)
        if not request.GET.get("code"):
            # 初次访问, 当然这样干是不对的
            return redirect(oauth_client_service.oauth_url)

        tokens = oauth_client_service.fetch_token(request.GET.get("code"))
        lebang_service = LebangUserService(tokens.get("access_token"))
        lebang_service.bind_user(request)
        return redirect(request.GET.get("next") or "/game/tpl/index#"+route)


class UserSignoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/user/token")
