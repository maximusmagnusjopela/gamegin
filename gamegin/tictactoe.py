#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base
import copy
import util

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

    def next_player(self):
        next_player_idx = (self.current_player_idx + 1) %  len(self.players)
        return self.players[next_player_idx]

    def switch_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
        return

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

        lines = board_lines()

        for line_indexes in lines:
            line_items = [ self.board[i] for i in line_indexes ]

            if line_items.count(None) == 0 and util.is_unique(line_items):
                return line_items[0]

        return None

    def prompt_state_str(self):
        state_cp = copy.deepcopy(self)
        for i, symbol in enumerate(state_cp.board):
            if symbol is None:
                state_cp.board[i] = i

        prompt_str =  state_cp.__unicode__() + '\n' + "Select the index of your next move:"
        return prompt_str


    def transition(self,transition_str):

        valid_str_indexes = set("012345678")
        valid_board_indexes = { i for i, sym in enumerate(self.board) if sym is None }

        if transition_str in valid_str_indexes:
            index = int(transition_str)
            if index in valid_board_indexes:
                selected_state = copy.deepcopy(self)
                selected_state.board[index] = selected_state.current_player().symbol()
                selected_state.switch_player()
                return selected_state

        return None

    def winner(self):
        """ Returns the symbol of the winning player. None if not terminal state or draw. """
        return self.is_terminal()

class TicTacToeGameFactory:

    def __init__(self,p1_cls,p2_cls):
        self.players = [p1_cls('X'), p2_cls('O')]
        return

    def factory(self):
        state = TicTacToeState(self.players)
        game = base.Game(state)
        return game

def board_lines():
    """ Returns a collection of lines on the board """
    lines = []
    # horizontal lines
    for i in (0,3,6):
        lines.append(range(i,i+3))

    # vertical lines
    for i in (0,1,2):
        lines.append(range(i,i+7,3))

    # diagonal lines
    lines.append([0,4,8])
    lines.append([2,4,6])

    return lines

