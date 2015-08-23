#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base
import random
import copy
import sys

class RandomPlayer(base.Player):
    """ Player that give random values to all the possible states """

    def __init__(self,player_symbol):
        super().__init__(player_symbol)
        return

    def __eq__(self,other):
        return self.player_symbol == other.player_symbol

    def score(self,state):
        return random.random()

class HumanPlayer(base.Player):
    """ Ask a human to score the moves. """

    def __init__(self, player_symbol):
        super().__init__(player_symbol)
        return

    def __eq__(self, other):
        return self.player_symbol == other.player_symbol

    def play(self, state):
        """ Returns the state choosen by the user. """
        prompt = state.prompt_state_str()

        while True:
            raw_index = input(prompt)
            choosen_state = state.transition(raw_index)
            if choosen_state:
                return choosen_state
            else:
                print('invalid state transition. Please try again',file=sys.stderr)

