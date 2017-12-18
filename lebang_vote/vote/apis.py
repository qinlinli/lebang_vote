#!coding:utf8
# create by  @
from rest_framework import viewsets, routers
from .models import Game, Option
from .serializers import GameSerializer, OptionSerializer


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class OptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'options', OptionViewSet)
