#include <iostream>
#include <array>
#include <bitset>
#include <vector>
using std::cout;
using std::cin;
using std::endl;

std::bitset<9> values_in_row(std::array<std::array<int, 9>, 9> board, int row) {
    std::bitset<9> values;
    for (int col = 0; col < 9; col++) {
        if (board[row][col] - 1 >= 0) {
            values[board[row][col] - 1] = true;
        }
    }
    return values;
}

std::bitset<9> values_in_col(std::array<std::array<int, 9>, 9> board, int col) {
    std::bitset<9> values;
    for (int row = 0; row < 9; row++) {
        if (board[row][col] - 1 >= 0) {
            values[board[row][col] - 1] = true;
        }
    }
    return values;
}

int get_cell(int row, int col) {
    return (row / 3) * 3 + (col / 3);
}

std::bitset<9> values_in_cell(std::array<std::array<int, 9>, 9> board, int cell_x, int cell_y) {
    std::bitset<9> values;
    for (int x = cell_x * 3; x < cell_x * 3 + 3; x++) {
        for (int y = cell_y * 3; y < cell_y * 3 + 3; y++) {
            if (board[x][y] - 1 >= 0) {   
                values[board[x][y]-1] = true;
            }
        }
    }
    return values;
}


int get_next_row(int row, int col){
    return row + (col + 1) / 9;
}

int get_next_col(int col){
    return (col + 1) % 9;
}

std::pair<int, int> next_empty_square(std::array<std::array<int, 9>, 9> &board, int row, int col) {
    while (row < 9) {
        if (board[row][col] == 0) {
            return std::pair<int, int>(row, col);
        }
        row = get_next_row(row, col);
        col = get_next_col(col);
    }
    return std::pair<int, int> (9, 0);
}

bool solve(
    std::array<std::array<int, 9>,9> &board, int row_start, int col_start,
    std::array<std::bitset<9>, 9> row_values,
    std::array<std::bitset<9>, 9> col_values,
    std::array<std::bitset<9>, 9> cell_values) {
    // get next empty square
    auto [row, col] = next_empty_square(board, row_start, col_start);

    if (row == 9) {
        return true;
    }

    int cell = get_cell(row, col);
    std::bitset<9> values = row_values[row] | col_values[col] | cell_values[cell];
    if (values.all()) {
        return false;
    }

    for (int i = 0; i < 9; ++i) {
        if (!values[i]) {
            board[row][col] = i + 1;
            row_values[row][i] = true;
            col_values[col][i] = true;
            cell_values[cell][i] = true;
            if (solve(board, row, col, row_values, col_values, cell_values)) {
                return true;
            }
            row_values[row][i] = false;
            col_values[col][i] = false;
            cell_values[cell][i] = false;
        }
    }
    board[row][col] = 0;
    return false;
}

int solver(std::array<std::array<int, 9>, 9> &board) {
    std::array<std::bitset<9>, 9> row_values = {0,0,0,0,0,0,0,0,0};
    std::array<std::bitset<9>, 9> col_values = {0,0,0,0,0,0,0,0,0};
    std::array<std::bitset<9>, 9> cell_values = {0,0,0,0,0,0,0,0,0};

    for (int row = 0; row < 9; ++row) {
        for (int col = 0; col < 9; ++col) {
            int value = board[row][col];
            if (value != 0) {
                value--;
                row_values[row][value] = true;
                col_values[col][value] = true;
                int cell = get_cell(row, col);
                cell_values[cell][value] = true;
            }
        }
    }
    return solve(board, 0, 0, row_values, col_values, cell_values);
}

// converts flat array board to 2d array
std::array<std::array<int, 9>, 9> flat_to_array2d(std::array<int, 81> flat_board) {
    std::array<std::array<int, 9>, 9> array2d;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            array2d[i][j] = flat_board[i*9 + j];
        }
    }
    return array2d;
}

/**
 * Prompts the user to input a sudoku board represented by integers.
 *\
 *\returns integer array of length 81 with values from 0-9
 */
std::array<int, 81> prompt() {
    std::array<int, 81> flat_board = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,};
    cout << "Enter an unsolved sudoku: " << endl;
    for (int i = 0; i < 81; i++) {
        cin >> flat_board[i];
    }
    return flat_board;
}

// prints a 2d array board
void print_board(std::array<std::array<int, 9>, 9> board) {
    cout << "    0  1  2  3  4  5  6  7  8 " << endl;
    cout << " -|---------------------------" << endl;
    for (int i = 0; i < 9; i++) {
        cout << i << " | ";
        for (int j = 0; j < 9; j++) {
            cout << board[i][j];
            if (j < 8) {
                cout << "  ";
            }
        }
        cout << endl;
    }
}

int main() {
    std::array<int, 81> flat_board = prompt();
    std::array<std::array<int, 9>, 9> board = flat_to_array2d(flat_board);
    print_board(board);
    bool solution = solver(board);
    if (solution) {
        cout << "Solution found!" << endl;
        print_board(board);
    } else {
        cout << "Board has no solution!" << endl;
    }
    return 0;
}