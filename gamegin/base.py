#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
base.py
~~~~~~~

This module contains the base classes for the game engine

:copyright:  (c) 2015 by Jonathan Pelletier.

"""

class State:

    def __init__(self,players,*args,**kvargs):

        self.player_symbols = set({})

        for p in players:
            self.register_player
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

    def register_player(self, player):
        """ Adds the player symbol to the list of symbols for the game state """
        self.player_symbols.add(player.symbol())
        return

    def next_player(self,

class Player:

    def __init__(self,symboly, *args,**kvargs):
        self.symbol = symbol
        return

    def symbol(self):
        """ Returns the symbol associated with the current player. """
        return self.symbol

    def play(self, state):
        """ Returns the best state from the according to the score function. """
        sucessors = state.succ()
        new_state = max(sucessors, key=self.score)
        return new_state

    def score(self,state):
        """ Returns a real number representing to value of a given state. """
        raise NotImplementedError()

class Game:

    def __init__(self,state_cls,players,*args,**kvargs):

        self.state = state_cls()
        self.players = players

        # Register all the players with the state
        for p in self.players:
            self.state.register(p)

        return


    def start(self):

        while not self.state.






