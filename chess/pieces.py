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
    
    def move(self, game, in_='random'):
        moves = self.valid_moves(game) #moves including self-check inducing ones
        if in_ == 'random':
            move = random.choice([m for m in moves if len(m) < 3]) #filter out king-taking moves
        else:
            if in_ in moves:
                move = in_
            else:
                print('Not a valid move')
                return
        c, r = move
        # taking a piece
        board = game.board()
        if isinstance(board[r][c], Piece):
            board[r][c].alive = False
    
        self.position = move
        
    def str_position(self):
        p = self.position
        return f'{COLUMNS[p[0]]}{p[1]+1}'

    def __repr__(self):
        return f'{self.name}{self.str_position()}'
        
from utils import tile_test, neighbors, check_test # avoid circular dependent import

class Pawn(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='', points=1)
        self.promoted = False
        if self.promoted:
            #change class instance?
            pass
        
    def valid_moves(self, game, check_filt=True):
        board = game.board()
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
            
        if check_filt:
            valid_moves = [m for m in valid_moves if not check_test(self, game, m)]
        return valid_moves
    
class Knight(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='N', points=3)

    def valid_moves(self, game, check_filt=True):
        board = game.board()
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        for (x,y) in neighbors('knight'):
            try:
                valid_moves, _ = tile_test(self, board[r+y][c+x], (c+x, r+y), {}, 0, valid_moves)
            except IndexError:
                pass
        if check_filt:
            valid_moves = [m for m in valid_moves if not check_test(self, game, m)]
        return valid_moves
    
class Bishop(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='B', points=3)

    def valid_moves(self, game, check_filt=True):
        board = game.board()
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        enc = {e:False for e in ['3', '2', '4', '1']} #conserving quadrant order in diag_neighbors() output for interpretability
        for i in range(1,8): #iterate over each possible distance
            for e, (x,y) in zip(enc.keys(), neighbors('diag')):
                try:
                    valid_moves, enc = tile_test(self, board[r+i*y][c+i*x], (c+i*x, r+i*y), enc, e, valid_moves)
                except IndexError:
                    pass
        if check_filt:
            valid_moves = [m for m in valid_moves if not check_test(self, game, m)]
        return valid_moves

class Rook(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='R', points=5)
    
    def valid_moves(self, game, check_filt=True):
        board = game.board()
        c, r = self.position #column, row
        valid_moves = []
        if not self.had_first_move:
            pass #castle --> needs to affect king too
        enc = {e:False for e in ['enc_l', 'enc_d', 'enc_u', 'enc_r']}
        for i in range(1,8): #iterate over each possible distance
            #iterate over bools and offsets
            for e, (x,y) in zip(enc.keys(), neighbors('straight')):
                try:
                    valid_moves, enc = tile_test(self, board[r+i*y][c+i*x], (c+i*x, r+i*y), enc, e, valid_moves)
                except IndexError:
                    pass
        if check_filt:
            valid_moves = [m for m in valid_moves if not check_test(self, game, m)]
        return valid_moves   

class Queen(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='Q', points=9)
        
    def valid_moves(self, game, check_filt=True):
        board = game.board()
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        enc = {e:False for e in ['enc_l', 'enc_d', 'enc_u', 'enc_r', '3', '2', '4', '1']}
        for i in range(1,8): #iterate over each possible distance
            #iterate over bools and offsets
            for e, (x,y) in zip(enc.keys(), neighbors('straight diag')):
                try:
                    valid_moves, enc = tile_test(self, board[r+i*y][c+i*x], (c+i*x, r+i*y), enc, e, valid_moves)
                except IndexError:
                    pass
        if check_filt:
            valid_moves = [m for m in valid_moves if not check_test(self, game, m)]
        return valid_moves
    
class King(Piece):
    def __init__(self, team, position):
        super().__init__(team, position, name='K', points=None)
        self.check = False
        self.mate = False
        
    def valid_moves(self, game, check_filt=True):
        board = game.board()
        N = self.N
        c, r = self.position #column, row
        valid_moves = []
        for (x,y) in neighbors('straight diag'):
            try:
                valid_moves, _ = tile_test(self, board[r+y][c+x], (c+x, r+y), {}, 0, valid_moves)
            except IndexError:
                pass
        if check_filt:
            valid_moves = [m for m in valid_moves if not check_test(self, game, m)]
        return valid_moves

