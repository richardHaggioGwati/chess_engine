import pygame

from const import *
from board import *


class Game:
    def __init__(self):
        self.board = Board()

    # Show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if(row + col) % 2 == 0:
                    color = (234, 235, 200) # light green
                else:
                    color = (119, 154, 88) # dark green

                rectangle = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rectangle)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # PIECES ?
                if self.board.squares[row][col].has_pieces():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    image_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece_texture_rect = img.get_rect(center=image_center)
                    surface.blit(img, piece_texture_rect)