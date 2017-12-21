#!coding:utf8
# create by  @
from rest_framework import serializers
from .models import Option, Game, VoteLog
from .services import CounterService


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    voted = serializers.SerializerMethodField()
    can_vote = serializers.SerializerMethodField()
    count_visit = serializers.SerializerMethodField()
    class Meta:
        model = Option
        fields = ['id', 'title', 'content', 'count_visit', 'count_vote', 'url', 'image_url', 'voted',
                  'can_vote', "count_visit"]

    def get_voted(self, obj):
        try:
            exist = VoteLog.objects.filter(option=obj, user=self.context['request'].user).first()
            return bool(exist)
        except VoteLog.DoesNotExist:
            return False

    def get_can_vote(self, obj):
        options = obj.game.options.all()
        exists = VoteLog.objects.filter(user=self.context['request'].user, option__in=options)
        if not exists:
            return True
        return bool(len(exists.all()) < obj.game.max_vote)

    def get_count_visit(self, obj):
        return obj.visited



class GameSerializer(serializers.HyperlinkedModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    visited = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'start', 'end', 'max_vote', 'visited', 'voted_person', 'voted_amount',
                  'title', 'content', 'options', 'url', 'visited']

    def get_visited(self, obj):
        return obj.visited
