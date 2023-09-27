#include <string>
#include "pieces.h"


Piece::Piece(char& team, const std::string& name) 
: team(team), name(name) // member initialization list
{

}

Pawn::Pawn(char& team) 
: team(team) {

}