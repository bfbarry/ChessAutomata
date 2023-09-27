#include <string>
#include <map>
#include <array>
#include <vector>
#include <memory>
#include "pieces.h"


static const char TEAMS[2] = {'w', 'b'};

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
                std::string k = kv.first;
                int row_w;
                int row_b;
                if (k == "Pawn") {
                    row_w = 1;
                    row_b = 6;
                }
                else {
                    row_w = 0;
                    row_b = 7;
                }
                if (k == "Pawn") {
                    pieces[arr_i++] = std::make_unique<Pawn>('w');
                }
            };
        };
};

int main() {
    return 0;
}