#!coding:utf8
# create by  @
import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, routers
from .models import Game, Option
from .serializers import GameSerializer, OptionSerializer
from .services import vote_service, VisterCounterService
from .exceptions import VoteError


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.filter(end__gte=datetime.now())
    serializer_class = GameSerializer


class OptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Option.objects.filter()
    serializer_class = OptionSerializer


@csrf_exempt
@login_required
def user_vote(request):
    try:
        data = json.loads(request.body)
    except Exception, e:
        raise VoteError(e.message)

    if vote_service.user_vote(request.user, data.get("id")):
        return JsonResponse({"code": 0})
    else:
        return JsonResponse({"code": 1, "error": "投票失败"})



router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'options', OptionViewSet)
