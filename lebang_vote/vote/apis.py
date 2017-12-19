#!coding:utf8
# create by  @
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, routers
from .models import Game, Option
from .serializers import GameSerializer, OptionSerializer
from .services import vote_service


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class OptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


@csrf_exempt
@login_required
def user_vote(request):
    if vote_service.user_vote(request.user, request.POST.get("option_id")):
        return JsonResponse({"code": 0})
    else:
        return JsonResponse({"code": 1})



router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'options', OptionViewSet)
