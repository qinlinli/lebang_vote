#!coding:utf8
# create by  @
import requests
import logging
from urllib import urlencode
from uuid import uuid1
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.db.transaction import atomic
from .models import Settings, Voter
from .exceptions import UserError



class SettingService:
    @staticmethod
    def get(name):
        try:
            return Settings.objects.get(name=name).value
        except Settings.DoesNotExist:
            return None


class OauthClientService:
    base_url = SettingService.get("base_url")
    code_path = SettingService.get("code_path")
    token_path = SettingService.get("token_path")
    app_id = SettingService.get("app_id")
    app_secret = SettingService.get("app_secret")
    redirect_url = SettingService.get("redirect_url")

    @property
    def oauth_url(self):
        url = "%s%s?%s" % (self.base_url, self.code_path, urlencode({
            "scopes": "r-staff", "state": str(uuid1()), "redirect_uri": self.redirect_url,
            "response_type": "code", "client_id": self.app_id
        }))
        return url

    def fetch_token(self, code):
        """
        :param code:
        :return:  {"access_token": xx, "refresh_token": xx, "token_type": xx, "score": xx}
        """
        req = requests.post("%s%s" %(self.base_url, self.token_path), data=dict(
            client_id=self.app_id, client_secret=self.app_secret, grant_type="authorization_code",
            code=code, redirect_uri=self.redirect_url
        ))
        try:
            data = req.json()
            return data
        except Exception, e:
            raise UserError("%s - - %s", e.message, req.content)


oauth_client_service = OauthClientService()


class LebangUserService:
    def __init__(self, access_token):
        self.access_token = access_token

    def fetch_user_info(self):
        url = "%s%s" % (SettingService.get("base_url"), SettingService.get("staff_info_path"))
        req = requests.get(url, params={"access_token": self.access_token})
        try:
            res = req.json()
        except Exception, e:
            raise UserError("获取身份信息失败：%s", req.content)
        if res.get("code") == 0:
            return res.get("result")
        raise UserError("获取身份信息失败：%s", res.get("error"))


    @method_decorator(atomic)
    def bind_user(self, request):
        user_info = self.fetch_user_info()
        try:
            voter = Voter.objects.get(staff_id=int(user_info.get("id")))
            login(request, voter.user)
            return
        except Voter.DoesNotExist:
            pass

        user = User.objects.create_user(str(user_info.get("mobile")), None, str(uuid1()))
        user.save()
        voter = Voter.objects.create(staff_id=user_info.get("id"),
                                    mobile=user_info.get("mobile"),
                                    name=user_info.get("fullname") or user_info.get("nick_name"),
                                    nickname=user_info.get("nickname"),
                                    avatar_url=user_info.get("avatar_url") or "",
                                    user=user)
        voter.save()
        login(request, user)
