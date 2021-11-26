import random

COLUMNS = 'abcdefgh'
COLOR_DIRECTION = {'w':1, 'b':-1} # see Piece.N

class Piece:
    def __init__(self, team, position, name, points):
        """
        team: 'b' or 'w' 
        position: (col, row)
        declared with default arguments in child __init__():
            name: piece notation
            points: 
        every Piece has a valid_moves() method in its child class
            takes an input move in_, which is defaulted to random
        """
        self.team = team 
        self.position = position
        self.name = name 
        self.points = points
        self.id_ = hash(random.random())
        self.alive = True
        self.had_first_move = False
        self.N = COLOR_DIRECTION[self.team] #in what direction the piece "sees" North. Mostly used by pawn
    
    def move(self, board, in_='random'):
        moves = self.valid_moves(board)
        if in_ == 'random':
            move = random.choice(moves)
        else:
            if in_ in moves:
                move = in_
            else:
                print('Not a valid move')
                return
        self.position = move
        
    def str_position(self):
        p = self.position
        return f'{COLUMNS[p[0]]}{p[1]+1}'

    def __repr__(self):
        return f'{self.name}{self.str_position()}'
        
from utils import straight_search, straight_neighbors # avoid circular dependent import

class Pawn(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='', points=1)
        self.promoted = False
        if self.promoted:
            #change class instance?
            pass
        
    def valid_moves(self, board):
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
                                        #check nobody in way
        if not self.had_first_move and board[r+N*2][c] == 0 and board[r+N*1][c] == 0: #2 spaces
            valid_moves.append((c,r+N*2))
        try:
            if board[r+N*1][c] == 0: # 1 space
                valid_moves.append((c,r+N*1))
        except IndexError:
            pass
            
        return valid_moves
    
class Knight(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='N', points=3)

    def valid_moves(self, board):
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        try:
            pass
        except IndexError:
            pass

        return valid_moves
    
class Bishop(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='B', points=3)

    def valid_moves(self, board):
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        try:
            pass
        except IndexError:
            pass

        return valid_moves

class Rook(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='R', points=5)
    
    def valid_moves(self, board):
        c, r = self.position #column, row
        valid_moves = []
        if not self.had_first_move:
            pass #castle --> needs to affect king too
        enc_r=enc_l=enc_u=enc_d = False # piece encountered on r, l, u d direction
        for i in range(1,8):
            try:
                #current item on tile, move towards that tile
                i_r, m_r, i_l, m_l, i_u, m_u, i_d, m_d = straight_neighbors(board, r, c, i)
                print('curri',i, i_r, m_r, i_l, m_l, i_u, m_u, i_d, m_d)
                valid_moves, enc_r = straight_search(self, i_r, m_r, enc_r, valid_moves)
                valid_moves, enc_l = straight_search(self, i_l, m_l, enc_l, valid_moves)
                valid_moves, enc_u = straight_search(self, i_u, m_u, enc_u, valid_moves)
                valid_moves, enc_d = straight_search(self, i_d, m_d, enc_d, valid_moves)
            except IndexError:
                pass
        print(valid_moves)
        return valid_moves   

class Queen(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='Q', points=9)
        
    def valid_moves(self, board):
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        try:
            pass
        except IndexError:
            pass

        return valid_moves
    
class King(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='K', points=None)
        self.check = False
        self.mate = False
        
    def valid_moves(self, board):
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        try:
            pass
        except IndexError:
            pass

        return valid_moves

