#include <iostream>
using std::vector;

// White pieces
int P = 1;
int N = 2;
int B = 3;
int R = 4;
int Q = 5;
int K = 6;

// Black pieces
int p = -1;
int n = -2;
int b = -3;
int r = -4;
int q = -5;
int k = -6;

const int tmp = NULL;
class Pawn {
    // list of moves -> local 2d space array [x][y]
    int color;
    std::vector<std::vector<std::vector<int>>> legal_moves = {{{1}}, {}};
    
};

class Bishop {

};

class King {
    std::vector<std::vector<std::vector<int>>> legal_moves = {{{}}};
};

int main() {
    std::vector<std::vector<int>> board = {{r,n,b,q,k,b,n,r},{}};


}




