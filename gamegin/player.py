#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base
import random

class RandomPlayer(base.Player):
    """ Player that give random values to all the possible states """

    def __init__(self,symbol):
        super().__init__(symbol)
        return

    def score(self,state):
        return random.random()





