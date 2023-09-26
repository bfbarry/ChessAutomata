#include <string>
#ifndef PIECES_H

#define PIECES_H
class Piece {
    public:
        virtual  ~Piece() = default; //virutal destructor for proper cleanup
        explicit Piece(const std::string& name);
        std::string name;
};
#endif