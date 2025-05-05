import numpy as np
import pygame
import sys
from board import Board
from player import HumanPlayer, RandomPlayer
from constants import *

# Game constants
ROW_COUNT = 6
COLUMN_COUNT = 7

SCREENWIDTH = SQUARESIZE * COLUMN_COUNT
SCREENHEIGHT = SQUARESIZE * (ROW_COUNT+1)
SIZE = (SCREENWIDTH, SCREENHEIGHT)

pygame.init()
screen = pygame.display.set_mode(SIZE)
myfont = pygame.font.SysFont("monospace", 75)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.board = Board(COLUMN_COUNT, ROW_COUNT)
        self.players = {
            1: HumanPlayer(1, RED),
            2: RandomPlayer(2, YELLOW)
        }
        self.current_turn = 0
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.board.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, SCREENWIDTH, SQUARESIZE))
            posx = event.pos[0]
            if self.current_turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, SCREENWIDTH, SQUARESIZE))
            # Player 1
            if self.current_turn == 0:

                posx = event.pos[0]
                col = int(posx / SQUARESIZE)

                if self.board.is_valid_col(col):
                    row = self.board.get_next_open_row(col)
                    self.board.drop_piece(row, col, 1)

                    if self.board.is_winning_move(1):
                        print("Player 1 wins")
                        # game_over = True
                        self.running = False

                    # get player 2's move
                    move = self.players[2].get_move(self.board)
                    if self.running and self.board.is_valid_col(move):
                        row = self.board.get_next_open_row(move)
                        self.board.drop_piece(row, move, 2)
                        if self.board.is_winning_move(2):
                            print("Player 2 wins")
                            # game_over = True
                            self.running = False
                        self.current_turn += 1

            # Player 2
            else:
                posx = event.pos[0]
                col = int(posx / SQUARESIZE)

                if self.board.is_valid_col(col):
                    row = self.board.get_next_open_row(col)
                    self.board.drop_piece(row, col, 2)

                    if self.board.is_winning_move(2):
                        print("Player 2 wins")
                        self.running = False

            self.board.draw(self.screen)

            self.current_turn += 1
            self.current_turn %= 2

            if not self.running:
                pygame.time.wait(3000)
                return
