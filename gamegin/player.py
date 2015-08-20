#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base
import random

class RandomPlayer(base.Player):
    """ Player that give random values to all the possible states """

    def __init__(self,player_symbol):
        super().__init__(player_symbol)
        return

    def __eq__(self,other):
        return self.player_symbol == other.player_symbol

    def score(self,state):
        return random.random()

