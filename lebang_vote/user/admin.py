#!coding:utf8

from django.contrib import admin
from .models import Voter, Settings


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ["name", "nickname", "mobile"]
    pass


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
