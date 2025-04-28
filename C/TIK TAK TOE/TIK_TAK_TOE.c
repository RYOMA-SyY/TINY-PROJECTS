#include <stdio.h>
#include <stdbool.h>

//display board
void SHOW(char board[3][3]) { 
    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf(" %c | %c | %c \n", board[i][0], board[i][1], board[i][2]);
        if (i < 2){ 
            printf("---|---|---\n");} // to separate the rows
    }
    printf("\n");
}

// Function WIN LOSE
bool checkWin(char board[3][3], char player) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true; // Rows
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true; // Columns
    }
    // Check diagonals
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;
    return false;
}

// TA3ADOL
bool checkDraw(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') return false; // CHEKING ALL CELLS IF EMPTY
        }
    }
    return true;
}

int main() {
    char board[3][3] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };
    int row, col;
    char Turn = 'X';
    bool gameOver = false;

    printf("Welcome to Tic-Tac-Toe!\n");

    while (!gameOver) {
        SHOW(board);

        printf("Player %c, enter row (0-2) and column (0-2): ", Turn); // move
        scanf("%d %d", &row, &col);

       //checking wrong move
        if (row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != ' ') {
            printf("Invalid move! Try again.\n");
            continue;
        }

        // Update the board
        board[row][col] = Turn;

        // Check if the current player has won
        if (checkWin(board, Turn)) {
            SHOW(board);
            printf("Player %c is A WINNER\n", Turn);
            gameOver = true;
        }
        // Check if the game is a draw
        else if (checkDraw(board)) {
            SHOW(board);
            printf("It's a draw!\n");
            gameOver = true;
        }
        // Switch players
        else {
            if (Turn == 'X') {
                Turn = 'O';
            } else {
                Turn = 'X';
            }
        }
    }

    return 0;
}