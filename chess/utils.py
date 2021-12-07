import matplotlib.pyplot as plt
from pieces import Piece
from itertools import permutations

OPTEAM = {'w':'b', 'b':'w'} #to find opposing team

def empty_board(title):
    """MPL board display"""
    board_mat = []
    for i in range(4):
        board_mat.append([0,1]*4)
        board_mat.append([1,0]*4)
    plt.imshow(board_mat, cmap='cool')
    if title:
        plt.title(title)
    plt.locator_params(tight=True, nbins=8) #n ticks
    
def _has_neg(l):
    """helper func to prevent wormholes on board"""
    return sum([1 if i<0 else 0 for i in l]) > 0
    
def _absmult(x):
    """Helper func to filter moves from permutations"""
    return abs(x[0]*x[1])
    
def tile_test(self, it, m, enc, e, valid_moves, test_empty=True):
    """
    checks if piece can move to a tile given current item there (empty or piece) and 
    current value of encounter boolean
    to be used by Bishop, Knight, Rook, Queen, King
        it: item at tile (an int or Piece)
        m: move to tile (tuple)
        enc: dict piece encounter (values are bool)
        e: key for the above
        valid_moves: list
    if Knight, pass enc as empty dict and arbitrary key to ignore boolean

    returns: list of possible moves, each of form (x,y). 
    If a move would 'take' the king (i.e., the CURRENT position puts K in check), then move is of form (x,y,'K')

    valid moves are not final and are verified if they put the King in check. (in self.valid_moves() ?)
    """

    if _has_neg(m):
        return valid_moves, enc

    if not enc.get(e) and isinstance(it, Piece):
        if it.team != self.team:
            if it.name == 'K': # verify if this puts other team in check
                m += ('K',)
            valid_moves.append(m)
            enc[e] = True
        else:
            enc[e] = True
    if test_empty and not enc.get(e) and it == 0: # True most of the time except for pawn
        valid_moves.append(m)
    return valid_moves, enc

def makes_check(game, t):
    """
    used to see if a piece's new move allows team t to put the piece's team in check,
    e.g., to see if a king can move to a tile without going in check
    When checking if 'A' king can move to tile, game board is copied, move is made, and call makes_check(game, 'B') 
    """

    has3 = lambda l: sum([1 for i in l if len(i) == 3]) == 1 #check if a piece has a move of form (x,y,'K')
    for piece in game.teams()[t]:
        piece = game.pick(piece) # extract object 
        if has3(piece.valid_moves(game, check_filt=False)): #False avoids recursion
            return True

def neighbors(directions):
    """
    returns offsets to move piece in directions' shape
    used by Knight, Bishop, Rook, Queen and  King
        directions: iterable or string with directions
    """
    neighbors = []
    if 'straight' in directions:
        neighbors.extend([i for i in permutations([-1,0,1], 2) if _absmult(i) != 1]) # if filters diagonals
    if 'diag' in directions:
        neighbors.extend(list(set([i for i in permutations([1,1,-1,-1], 2) ])))
    if 'knight' in directions:
        neighbors.extend([i for i in permutations([-2,-1,1,2], 2) if _absmult(i) not in (1,4)])
    return neighbors


