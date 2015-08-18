#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base

class TicTactToeState(base.State):

    board_size = 9

    def __init__(self, players, *args):
        super().__init__(players)

        self.board = [None for _ in TicTactToeState.board_size]
        self.current_player_idx = 0
        return

    def succ(self):
        return []

