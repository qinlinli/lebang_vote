#!coding:utf8
# create by  @
from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Voter(Base):
    user = models.OneToOneField(User)
    staff_id = models.CharField(max_length=32)
    mobile = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    nickname = models.CharField(max_length=16)
    avatar_url = models.CharField(max_length=1024, default="", blank=True)
