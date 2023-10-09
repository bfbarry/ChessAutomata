#include <string>
#include <map>
#include <array>
#include <vector>
#include <memory>
#include "pieces.h"


static const char TEAMS[2] = {'w', 'b'}; // TODO extern define in globals h/cpp

class Chess {
    std::array<std::unique_ptr<Piece>, 40> pieces;
    // Piece piece;
    std::map<char, int> check;
    std::map<char, int> mate;
    std::map<std::string, std::vector<int>> piece_to_col_positions;

    public:
        Chess() {
            int arr_i = 0;
            for (auto t: TEAMS) {
                check[t] = false;
                mate[t] = false;
            };
            piece_to_col_positions["Pawn"] = {0,1,2,3,4,5,6,7};
            piece_to_col_positions["Rook"] = {0,7};
            piece_to_col_positions["Knight"] = {1,6};
            piece_to_col_positions["Bishop"] = {2,5};
            piece_to_col_positions["Queen"] = {2};
            piece_to_col_positions["King"] = {4};
            
            // can also do it this way if more complex https://stackoverflow.com/questions/4007382/how-to-create-class-objects-dynamically
            for (const auto &kv: piece_to_col_positions) {
                // also for(std::map<std::string, std::vector<int>>::iterator iter = piece_to_col_positions.begin(); iter != piece_to_col_positions.end(); ++iter)
                std::string piece_type = kv.first;
                int row_w;
                int row_b;
                std::map<char, int> team_to_rowi;
                if (piece_type == "Pawn") {
                    team_to_rowi['w'] = 1;
                    team_to_rowi['b'] = 6;
                }
                else {
                    team_to_rowi['w'] = 0;
                    team_to_rowi['b'] = 7;
                }
                for (auto t: TEAMS) { 
                    if (piece_type == "Pawn") {
                        for (auto col_i: kv.second) {
                            Position pos = {col_i, team_to_rowi[t]};
                            pieces[arr_i++] = std::make_unique<Pawn>(t, pos);
                        }
                    if (piece_type == "") {

                    }
                }
                }
            };
        };
};

int main() {
    // Chess game = Chess();
    char x= 'w';
    // Position p2 = {0,1};
    // Pawn p(x, Position({0,1}));

    return 0;

}