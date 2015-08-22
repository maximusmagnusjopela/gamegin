#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base
import copy

class TicTacToeState(base.State):

    board_size = 9

    def __init__(self, players, *args):
        super().__init__(players)

        self.board = [None for _ in range(TicTacToeState.board_size)]
        self.current_player_idx = 0
        return

    def __eq__(self,other):

        return self.board == other.board and self.current_player_idx == other.current_player_idx and self.players == other.players

    def __unicode__(self):

        print_board = [ i if i != None else " " for i in self.board ]
        board_template = \
     """*-*-*-*
|{}|{}|{}|
*-*-*-*
|{}|{}|{}|
*-*-*-*
|{}|{}|{}|
*-*-*-*"""
        return board_template.format(*print_board)

    def __repr__(self):
        return self.__unicode__()

    def current_player(self):
        return self.players[self.current_player_idx]

    def succ(self):

        next_player_idx = (self.current_player_idx + 1) %  len(self.players)
        symbol = self.players[self.current_player_idx].symbol()

        successors = []
        for i,sym in enumerate(self.board):
            if sym is None:
                successor = copy.deepcopy(self)
                successor.board[i] = symbol
                successor.current_player_idx = next_player_idx
                successors.append(successor)

        return successors

    def is_terminal(self):
        """ Returns true if the state is a terminal state. """


        # we have a terminal state if the game board is full
        free_position_cnt = self.board.count(None)
        if free_position_cnt == 0:
            return True


        return False

class TicTacToeGameFactory:

    def __init__(self,p1_cls,p2_cls):
        self.players = [p1_cls('X'), p2_cls('O')]
        return

    def factory(self):
        state = TicTacToeState(self.players)
        game = base.Game(state)
        return game

