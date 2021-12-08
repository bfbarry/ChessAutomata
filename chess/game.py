# import sys, os
from pieces import Pawn, Knight, Bishop, Rook, Queen, King #don't import * because isinstance() doesn't work properly
from utils import empty_board
import numpy as np
import matplotlib.pyplot as plt
from copy import copy

TEAMS = 'wb'
COLORS = {'w':'gray', 'b':'black'}

class Chess:
    def __init__(self):
        self.pieces = []
        self.check = {t:False for t in TEAMS}
        self.mate = {t:False for t in TEAMS}
        ## initialize board
        for piece, iters in zip([Pawn, Rook, Knight, Bishop, Queen, King], 
                                [range(8), (0,7), (1,6), (2,5), (3,), (4,)]):
            if piece == Pawn:
                row_w, row_b = 1, 6
            else:
                row_w, row_b = 0, 7

            for i in iters:
                self.pieces.append(piece(team='w', position=(i, row_w)))
                self.pieces.append(piece(team='b', position=(i, row_b)))

        self.history = [] # array to keep snapshots at each step

    def teams(self, with_moves=False):
        """show live pieces for each team, useful for random walk
        with_moves: bool, filter only pieces that have moves left"""
        if with_moves:
            return {c: [str(p) for p in self.pieces if p.alive and len(p.valid_moves(self)) > 0 and p.team==c] for c in TEAMS}
        else:
            return {c: [str(p) for p in self.pieces if p.alive and p.team==c] for c in TEAMS}
    
    def pick(self, pc):
        """Piece str --> Piece object"""
        return {str(p):p for p in self.pieces if p.alive}[pc]
 

    def board(self):
        """
        Return matrix representation of board
        Empty tiles are filled with 0
        """
        board = [[0 for i in range(8)] for i in range(8)]
        for pc in self.pieces:
            if pc.alive:
                x, y = pc.position
                board[y][x] = pc
        return board
    
    def move(self, piece, in_, history=False):
        """
        Move piece to input location
        piece: str representation of piece, e.g. Ne5
        in_: tuple of form (col, row). Must be a valid move,
            as checked by piece.move()
        """
        if history:
            self.history.append(copy(self.pieces))
        try: #DEUG
            piece = self.pick(piece)
        except:
            print(f'{piece} not found in:', self.pieces)
            return
        piece.move(self, in_)
        
    def show(self, pieces=None, title=None):
        """Show graphical representation of current game on board"""
        empty_board(title)
        pieces = pieces if pieces else self.pieces
        for p in pieces:
            if p.alive:
                y,x = p.position
                plt.annotate(str(p), (y-0.25,x), c=COLORS[p.team], weight='bold')
    
    def __repr__(self): # deprecated
        return str(np.array(self.board())) # for matrix format