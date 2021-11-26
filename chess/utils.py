import matplotlib.pyplot as plt
from pieces import Piece
from itertools import permutations

def empty_board():
    """MPL board display"""
    board_mat = []
    for i in range(4):
        board_mat.append([0,1]*4)
        board_mat.append([1,0]*4)
    plt.imshow(board_mat, cmap='cool')
    plt.locator_params(tight=True, nbins=8) #n ticks
    
def _has_neg(l):
    """helper func to prevent wormholes on board"""
    return sum([1 if i<0 else 0 for i in l]) > 0
    
def _absmult(x):
    """Helper func to filter moves from permutations"""
    return abs(x[0]*x[1])

def tile_check(self, it, m, enc, e, valid_moves):
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
    """
    if _has_neg(m):
        return valid_moves, enc
    # if m == (0,7):
    #     print('07', enc)
    if not enc.get(e) and isinstance(it, Piece):
        if it.team != self.team and it.name != 'K':
            valid_moves.append(m)
            enc[e] = True
        else:
            enc[e] = True
    if not enc.get(e) and it == 0:
        valid_moves.append(m)
    return valid_moves, enc

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


