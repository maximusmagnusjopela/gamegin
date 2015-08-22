#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import tictactoe
import player

def main():
    """ gamegin board games """

    parser = argparse.ArgumentParser()
    parser.add_argument(
            'game',
            help='selected board game',
            choices=['tictactoe']
            )

    args = parser.parse_args()

    # build the correct game
    if args.game == 'tictactoe':
        game = tictactoe.TicTacToeGameFactory(player.RandomPlayer, player.RandomPlayer).factory()
    else:
        return

    print('game over! The winner is: {}'.format(game.start()))
    return

if __name__ == '__main__':
    main()

