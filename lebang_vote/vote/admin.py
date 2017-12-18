#!coding:utf8
# create by  @
from django.contrib import admin
from .models import Game, Option, VoteLog, Counter


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionsAdmin(admin.ModelAdmin):
    list_filter = ["game", ]
    pass


@admin.register(VoteLog)
class VoteLogAdmin(admin.ModelAdmin):
    pass


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    pass
