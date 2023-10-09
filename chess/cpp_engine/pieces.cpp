#include <string>
#include "pieces.h"

// TODO use const for methods if they don't mod class vars, then prefix obj ref with const

Piece::Piece(char& team, Position& position, const std::string& name) 
: team(team), position(position), name(name) // member initialization list
{

};

Pawn::Pawn(char& team, Position& position) 
:  Piece(team, position, this->name) {

};