#!coding:utf8
# create by  @
from django.contrib import admin
from .services import CounterService
from .models import Game, Option, VoteLog, Counter


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "voted_amount", "visited"]

    def visit_count(self, obj):
        cs = CounterService("games/%s" % obj.pk)
        return cs.value

@admin.register(Option)
class OptionsAdmin(admin.ModelAdmin):
    list_filter = ["game"]
    list_display = ["game", "title", "visited"]

    def visit_count(self, obj):
        cs = CounterService("options/%s" % obj.pk)
        return cs.value


@admin.register(VoteLog)
class VoteLogAdmin(admin.ModelAdmin):
    pass


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
