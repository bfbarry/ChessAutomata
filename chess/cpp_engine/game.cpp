#include <string>
#include <map>
#include <array> 
#include "pieces.h"
using namespace std;


static const char TEAMS[2] = {'w', 'b'};
// static const std::map<char, std::string> COLOR_MAP = {}

class Chess {
    array<string, 6> piece_names = {"Pawn", "Rook", "Knight", "Bishop", "Queen", "King"};
    array<Piece, 40> pieces;
    public:
        Chess() {
            // can also do it this way if more complex https://stackoverflow.com/questions/4007382/how-to-create-class-objects-dynamically
            for (auto i: piece_names) {
                pieces
            };
        }
};
