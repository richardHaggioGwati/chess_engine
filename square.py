class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_pieces(self):
        return self.piece is not None

    def is_empty(self):
        return not self.has_pieces()

    def has_team_piece(self, color):
        return self.has_pieces() and self.piece.color == color

    def has_rival_piece(self, color):
        return self.has_pieces() and self.piece.color != color

    def is_empty_or_rival(self, color):
        return self.is_empty() or self.has_rival_piece(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False

        return True
