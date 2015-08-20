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


