#!coding:utf8
# create by  @
from rest_framework import serializers
from .models import Option


class OptionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)
