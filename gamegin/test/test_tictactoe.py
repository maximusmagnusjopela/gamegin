#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nose
import copy

from gamegin.player import RandomPlayer
from gamegin.tictactoe import TicTacToeState

class TestTicTacToeState:

    def setUp(self):
        player_X = RandomPlayer('X')
        player_O = RandomPlayer('O')

        players = [player_X, player_O]

        self.tictactoe_state = TicTacToeState(players)
        return

    def teatDown(self):
        pass

    def test_initstate_tictactoe_sucessors(self):

        computed_successors = self.tictactoe_state.succ()
        expected_sucessors = []
        for i in range(TicTacToeState.board_size):
            state = copy.deepcopy(self.tictactoe_state)
            symbol = state.current_player().symbol()
            state.board[i] = symbol
            state.current_player_idx = (state.current_player_idx + 1) % len(state.players)
            expected_sucessors.append(state)

        assert expected_sucessors == self.tictactoe_state.succ()


