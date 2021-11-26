import matplotlib.pyplot as plt
from pieces import Piece

def empty_board():
    """MPL board display"""
    board_mat = []
    for i in range(4):
        board_mat.append([0,1]*4)
        board_mat.append([1,0]*4)
    plt.imshow(board_mat, cmap='cool')
    
def _has_neg(l):
    """helper func to prevent wormholes on board"""
    return sum([1 if i<0 else 0 for i in l]) > 0
    
def straight_search(self, it, m, enc, valid_moves):
    """
    MIGHT GENERALIZE TO ALL OTHER RANGED PIECES
    used in Queen and Rook
        it: item at tile (an int or Piece)
        m: move to tile (tuple)
        enc: piece encounter (bool)
        valid_moves: list
    """
    if _has_neg(m):
        return valid_moves, enc

    if not enc and isinstance(it, Piece):
        if it.team != self.team:
            valid_moves.append(m)
            enc = True
        else:
            enc = True
    if not enc and it == 0:
        valid_moves.append(m)
    return valid_moves, enc

def straight_neighbors(board, r, c, i):
    """
    returns neighbors and move position of piece in '+' shape
        r: row
        c: col
        i: offset
    """
    #current item on tile, move towards that tile
    # return board[r][c+i], (c+i, r),\
        #    board[r][c-i], (c-i, r),\
        #    board[r-i][c], (c, r-i),\
        #    board[r+i][c], (c, r+i),

