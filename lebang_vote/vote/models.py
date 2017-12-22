#!coding:utf8
# create by  @
from django.contrib.auth.models import User
from django.db import models
from lebang_vote.user.models import Voter
from ckeditor_uploader.fields import RichTextUploadingField


class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Game(Base):
    name = models.CharField(max_length=255)
    content = RichTextUploadingField(max_length=1024*10)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.IntegerField(default=0)  # online / offline
    image = models.ImageField(null=True, default=None)
    title = models.CharField(max_length=1024)  # display title
    sub_title = models.CharField(max_length=1024, default="", blank=True)
    max_vote = models.IntegerField(default=1)  # 最多
    vote_cicle_hour = models.IntegerField(default=1024)  # 多少小时内能投票
    voted_person = models.IntegerField(default=0)  # 人数
    visited = models.IntegerField(default=0)
    voted_amount = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s_%s" % (self.name, self.title)

    @property
    def page_visited(self):
        from .services import CounterService
        cs = CounterService("games/%s" % self.pk)
        return cs.value


class Option(Base):
    game = models.ForeignKey(Game, related_name='options')
    title = models.CharField(max_length=1024)
    content = RichTextUploadingField(max_length=1024*10)
    image_url = models.ImageField(null=True, default=None)
    count_vote = models.IntegerField(default=0)
    count_visit = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s_%s" % (self.game.name, self.title)

    @property
    def visited(self):
        from .services import CounterService
        cs = CounterService("options/%s" % self.pk)
        return cs.value


class VoteLog(Base):
    user = models.ForeignKey(User)
    option = models.ForeignKey(Option)
    value = models.IntegerField(default=1)


class Counter(Base):
    value = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default="")

    def __uuid__(self):
        return "%s_%s" % (self.__class__.name, self.pk)
