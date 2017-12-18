#!coding:utf8
from .models import Game, VoteLog, Option, Counter
from django.contrib.auth.models import User


class VoteService():
    def __init__(self, game):
        self.game = game

    def can_vote(self):
        pass
