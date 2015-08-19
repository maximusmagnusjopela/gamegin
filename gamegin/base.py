#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
base.py
~~~~~~~

This module contains the base classes for the game engine

:copyright:  (c) 2015 by Jonathan Pelletier.
"""

class State:

    def __init__(self, players, *args, **kvargs):

        self.players = players
        return

    def succ(self):
        """ Returns the sucessors of the current state as a generator. """
        raise NotImplementedError()

    def winner(self):
        """ Returns the symbol of the winning player for the current state, None if the state is a non terminal state
        or if there is no winner. """
        raise NotImplementedError()

    def is_terminal(self):
        """ Returns true is the state is a terminal state. False otherwise. """
        raise NotImplementedError()

    def active_player_symbol(self):
        """ Returns the symbol of the player that needs to make a move in the current state. """
        raise NotImplementedError()

    def next_player(self):
        """ Returns the player that will play next. """
        raise NotImplementedError()

    def current_player(self):
        """ Returns the current player. """
        raise NotImplementedError()

class Player:

    def __init__(self, symbol, *args,**kvargs):
        self.player_symbol = symbol
        return

    def symbol(self):
        """ Returns the symbol associated with the current player. """
        return self.player_symbol

    def play(self, state):
        """ Returns the best state from the according to the score function. """
        sucessors = state.succ()
        new_state = max(sucessors, key=self.score)
        return new_state

    def score(self, state):
        """ Returns a real number representing to value of a given state. """
        raise NotImplementedError()

class Game:

    def __init__(self, state, *args, **kvargs):

        self.state = state
        return

    def start(self):
        """ Main game loop. """

        ongoing = True
        while ongoing:
            for p in self.state.players:
                self.state = p.play(self.state)
                if self.state.is_terminal:
                    ongoing = False
                    break

        return self.state.winner()


