#!coding:utf8
from django.utils.decorators import method_decorator
from django.db.transaction import atomic
from .models import Game, VoteLog, Option, Counter
from .exceptions import VoteError


class VoteService():
    @method_decorator(atomic)
    def user_vote(self, user, option_id):
        try:
            option = Option.objects.get(pk=option_id)
        except Option.DoesNotExist:
            raise VoteError("选项不存在")
        game = option.game
        voted = VoteLog.objects.filter(user=user, option__in=game.options.all())
        if len(voted) >= game.max_vote:
            raise VoteError("您已经投过票了")
        log = VoteLog.objects.create(user=user, option_id=option_id)
        option.count_vote += 1
        game.voted_amount += 1
        if len(voted) == 0:
            game.voted_person += 1
        option.save()
        log.save()
        game.save()
        return True


vote_service = VoteService()
