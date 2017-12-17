#!coding:utf8
# create by  @
from rest_framework import serializers, viewsets, routers
from .models import Game, Option


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'title', 'content']

class GameSerializer(serializers.HyperlinkedModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        exclude = []


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class OptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
