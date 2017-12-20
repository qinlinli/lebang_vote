#!coding:utf8
# create by  @
import requests
from uuid import uuid1
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Settings, Voter
from .exceptions import UserException


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
        return "%s%s?scopes=r-staff&state=%s&redirect_url=%s&response_type=%s&client_id=%s" % (
            self.base_url, self.code_path, str(uuid1()), self.redirect_url, "code", self.app_id
        )

    def fetch_token(self, code):
        """
        :param code:
        :return:  {"access_token": xx, "refresh_token": xx, "token_type": xx, "score": xx}
        """
        req = requests.post("%s%s" %(self.base_url, self.token_path), data=dict(
            client_id=self.app_id, client_secret=self.app_secret, grant_type="authorization_code",
            code=code, redirect_url=self.redirect_url
        ))
        data = req.json()
        return data


oauth_client_service = OauthClientService()


class LebangUserService:
    def __init__(self, access_token):
        self.access_token = access_token

    def fetch_user_info(self):
        url = "%s%s" % (SettingService.get("base_url"), SettingService.get("staff_info_path"))
        req = requests.get(url, headers={"Authorization", "Bearer %s" % self.access_token})
        res = req.json()
        if res.get("code") == 0:
            return res.get("result")
        raise UserException("获取身份信息失败：%s", res.get("msg"))


    def bind_user(self, request):
        user_info = self.fetch_user_info()
        try:
            voter = Voter.objects.get(staff_id=int(user_info.get("staff_id")))
            login(request, voter.user)
            return
        except Voter.DoesNotExist:
            pass

        user = User.objects.create_user(user_info.get("mobile"), None, str(uuid1()))
        user.save()
        voter = Voter.objects.create(staff_id=user_info.get("staff_id"),
                                    mobile=user_info.get("mobile"),
                                    name=user_info.get("full_name"),
                                    nickname=user_info.get("nick_name"),
                                    avatar_url=user_info.get("avatar_url"),
                                    user=user)
        voter.save()
        login(request, user)
