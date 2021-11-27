# import sys, os
from pieces import Pawn, Knight, Bishop, Rook, Queen, King #don't import * because isinstance() doesn't work properly
from utils import empty_board
import numpy as np
import matplotlib.pyplot as plt

TEAMS = 'wb'

class Chess:
    def __init__(self):
        self.pieces = []

        for piece, iters in zip([Pawn, Rook, Knight, Bishop, Queen, King], 
                                [range(8), (0,7), (1,6), (2,5), (3,), (4,)]):
            if piece == Pawn:
                row_w, row_b = 1, 6
            else:
                row_w, row_b = 0, 7

            for i in iters:
                self.pieces.append(piece(team='w', position=(i, row_w)))
                self.pieces.append(piece(team='b', position=(i, row_b)))

    def teams(self):
        """show live pieces for each team, useful for random walk"""
        return {c: [str(p) for p in self.pieces if p.team==c and p.alive] for c in TEAMS}
    
    def pick(self, pc):
        """Piece str --> Piece object"""
        return {str(p):p for p in self.pieces}[pc]
    
    def board(self):
        """Return matrix representation of board"""
        board = [[0 for i in range(8)] for i in range(8)]
        for pc in self.pieces:
            if pc.alive:
                x, y = pc.position
                board[y][x] = pc
        return board
    
    def move(self, piece, in_):
        piece = self.pick(piece)
        piece.move(self, in_)
        
    def show(self):
        empty_board()
        for p in self.pieces:
            if p.alive:
                y,x = p.position
                plt.annotate(str(p), (y-0.25,x), c=p.team, weight='bold')        
    
    def __repr__(self): # deprecated
        return str(np.array(self.board())) # for matrix format