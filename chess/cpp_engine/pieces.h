#include <string>
#pragma once


typedef struct Position {
    int row;
    int column;
} Position;

class Piece {
    public:
        char team;
        std::string name;
        Position position;
        Piece() = default;
        Piece(char& team, Position& position, const std::string& name);
        virtual ~Piece() = default; //virutal destructor for proper cleanup
        // maybe don't need alive flag if you just delete
};

class Pawn : public Piece {
    // using Piece::Piece;
    const std::string name = "";
    public:
        Pawn(char& team, Position& position);
    
};