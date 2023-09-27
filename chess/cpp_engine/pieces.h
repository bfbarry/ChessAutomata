#include <string>
#ifndef PIECES_H

#define PIECES_H
class Piece {
    public:
        virtual ~Piece() = default; //virutal destructor for proper cleanup
        explicit Piece(char& team, const std::string& name);
        char team;
        std::string name;
};

class Pawn : Piece {
    public:
        explicit Pawn(char& team);
        char team;
    
};
#endif