#include <iostream>

using namespace std;

const int X = 0;
const int O = 1;

const int X_WINS = 0;
const int O_WINS = 3;

char board[3][3] = {{'*', '*', '*'}, 
                    {'*', '*', '*'}, 
                    {'*', '*', '*'}
                    };

void putX(int row, int col);
void putO(int row, int col);
void drawScene(char board[]);
int winner(char board[][3]);

void putX(int row, int col) {
    board[row][col] = 'X';
}

void putO(int row, int col) {
    board[row][col] = 'O';
}

void drawScene(char board[][3]) {
    cout << left << "  " << board[0][0] << "  | " << " " << board[0][1] << "  | " << " " << board[0][2] << endl;
    cout << "-----|-----|-----" << endl;
    cout << "  " << board[1][0] << "  | " << " " << board[1][1] << "  | " << " " << board[1][2] << endl;
    cout << "-----|-----|-----" << endl;
    cout << "  " << board[2][0] << "  | " << " " << board[2][1] << "  | " << " " << board[2][2] << endl;
}

int winner(char board[][3]) {
    int up_right_diag = 0;
    int up_left_diag = 0;

    for (int i = 0; i < 3; i++) {
        int row = 0;
        int col = 0;
        for (int j = 0; j < 3; j++) {
            row += board[i][j];
            col += board[j][i];
            if (i == j) {
                up_right_diag += board[i][j];
            }
            if (i + j == 2) {
                up_left_diag += board[i][j];
            }
        }
        if (row == X_WINS) {
            return X;
        }
        if (col == O_WINS) {
            return O;
        }
    }
    if (up_right_diag == X_WINS) {
        return X;
    } else if (up_right_diag == O_WINS) {
        return O;
    } else if (up_left_diag == X_WINS) {
        return X;
    } else if (up_left_diag == O_WINS) {
        return O;
    }
    return 10;
}

int main() {
    drawScene(board);
    while (true) {
        char piece;
        int x, y;
        cout << "Enter your move: ";
        cin >> piece >> x >> y;

        switch (piece) {
            case 'X':
                putX(x, y);
                break;
            case 'O':
                putO(x, y);
                break;
            default:
                break;
        }

        drawScene(board);

        if (winner(board) == X) {
            cout << "X Wins!" << endl;
            return 0;
        } else if (winner(board) == O) {
            cout << "O Wins!" << endl;
            return 0;
        }
    }
}