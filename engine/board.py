import numpy as np
import pygame
from constants import *

class Board():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width))
        print(self.board)

    def drop_piece(self, row, col, piece):
        print(f'dropping piece at row {row}, col {col}')
        self.board[row][col] = piece

    def is_valid_col(self, col):
        """Check if a piece can be placed in the given column"""
        return self.board[self.height-1][col] == 0
    
    def get_next_open_row(self, col):
        """Check where a piece would land if it is dropped in the given column"""
        for r in range(self.height):
            if self.board[r][col] == 0:
                return r
            
    def is_winning_move(self, piece):
        # Check horizontal
        for c in range(self.width - 3):
            for r in range(self.height):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True

        # Check vertical
        for c in range(self.width):
            for r in range(self.height - 3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True

        # Positive diagonal
        for c in range(self.width - 3):
            for r in range(self.height - 3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True

        # Negative diagonal
        for c in range(self.width - 3):
            for r in range(3, self.height):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True

        return False

    def draw(self, screen):
        for c in range(self.width):
            for r in range(self.height):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(self.width):
            for r in range(self.height):
                if self.board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), self.height*SQUARESIZE - int((r-1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), self.height*SQUARESIZE - int((r-1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)
        pygame.display.update()
