class ChessGame:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.turn = 'white'
        self.game_over = False
        self.move_history = []

    def move_piece(self, start_pos, end_pos):
        """
        Move a piece on the chess board
        """
        x1, y1 = start_pos
        x2, y2 = end_pos

        piece = self.board[x1][y1]
        dest_piece = self.board[x2][y2]

        if piece == '.':
            return False

        if dest_piece != '.':
            if piece.isupper() == dest_piece.isupper():
                return False

        if piece.lower() == 'p':
            if y1 == y2:
                if dest_piece != '.':
                    return False
                if x2 == x1 - 2 and x1 == 6 and self.board[x1-1][y1] == '.':
                    pass
                elif x2 == x1 - 1:
                    pass
                else:
                    return False
            else:
                if dest_piece == '.' or piece.isupper() == dest_piece.isupper():
                    return False
                if x2 != x1 - 1 or abs(y2 - y1) != 1:
                    return False

        # TODO: Implement logic for other pieces

        self.board[x1][y1] = '.'
        self.board[x2][y2] = piece

        self.move_history.append((start_pos, end_pos))

        # Switch the turn to the other player
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

        return True