#!coding:utf8
# create by  @
from rest_framework import serializers
from .models import Option, Game


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'title', 'content', 'count_visit', 'count_vote']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        exclude = ['created', 'updated']
