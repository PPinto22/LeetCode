#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

class Solution
{
public:
    // Board dimension: 3x3
    const int d = 3;
    const int D = pow(d, 2); // 9

    struct SolverData
    {
        vector<vector<char>> board;
        vector<vector<set<char>>> possibilities;
        set<pair<int, int>> unfilled;
        queue<pair<int, int>> fillQueue;
    };

    struct Guess
    {
        pair<int, int> position;
        char value;
    };

    void solveSudoku(vector<vector<char>> &board)
    {
        SolverData data = initSolverData(board);
        _solveSudoku(data);
        board = data.board;
    }

    SolverData initSolverData(vector<vector<char>> board)
    {
        SolverData data;
        data.board = board;
        for (int i = 0; i < D; i++)
        {
            data.possibilities.push_back(vector<set<char>>());
            for (int j = 0; j < D; j++)
            {
                auto position = make_pair(i, j);
                char value = board[i][j];
                set<char> possibilities;
                if (value == '.')
                {
                    for (int n = 1; n <= D; n++)
                        possibilities.insert('0' + n);
                }
                else
                {
                    possibilities.insert(value);
                    data.fillQueue.push(position);
                }
                data.possibilities[i].push_back(possibilities);
                data.unfilled.insert(position);
            }
        }
        return data;
    }

    bool _solveSudoku(SolverData &data)
    {
        while (!data.unfilled.empty())
        {
            // No more numbers to fill -- we'll have to make a guess
            // TODO: We could check each row, column, and square to see
            // if there are any numbers that can only be filled in one position.
            if (data.fillQueue.empty())
            {
                SolverData backup = data;
                Guess guess = getGuess(data);
                fillPosition(data, guess.position, guess.value);
                if (!_solveSudoku(data))
                {
                    // Bad guess: Rollback and remove guess from possible values
                    data = backup;
                    removePossibility(data, guess.position, guess.value);
                }
            }
            // There's a number in the fillQueue -- put it on the board
            else
            {
                auto &position = data.fillQueue.front();
                char value = *(data.possibilities[position.first][position.second].begin());
                // If there are no possible numbers to fill in, there is a mistake in the solution
                if (value == 0)
                {
                    return false;
                }
                fillPosition(data, position, value);
                data.fillQueue.pop();
            }
        }
        return true;
    }

    // Pick a position with the least possibilities and a random possible value
    Guess getGuess(SolverData &data)
    {
        int minPossibilities = D + 1;
        pair<int, int> minPosition;
        for (auto &position : data.unfilled)
        {
            int possibilities = data.possibilities[position.first][position.second].size();
            if (possibilities < minPossibilities)
            {
                minPossibilities = possibilities;
                minPosition = position;
                // If there are only two possibilities, we won't find anything better
                if (possibilities == 2)
                {
                    break;
                }
            }
        }
        char value = *(data.possibilities[minPosition.first][minPosition.second].begin());
        return Guess{minPosition, value};
    }

    void fillPosition(SolverData &data, pair<int, int> &position, char value)
    {
        auto [row, col] = position;

        data.board[row][col] = value;
        data.possibilities[row][col].clear();
        data.unfilled.erase(position);

        updateRow(data, position, value);
        updateColumn(data, position, value);
        updateSquare(data, position, value);
    }

    void updateRow(SolverData &data, pair<int, int> &position, char value)
    {
        auto [row, _] = position;
        for (int j = 0; j < D; j++)
        {
            removePossibility(data, make_pair(row, j), value);
        }
    }

    void updateColumn(SolverData &data, pair<int, int> &position, char value)
    {
        auto [_, col] = position;
        for (int i = 0; i < D; i++)
        {
            removePossibility(data, make_pair(i, col), value);
        }
    }

    void updateSquare(SolverData &data, pair<int, int> &position, char value)
    {
        int squareRow = position.first / d;
        int squareCol = position.second / d;
        for (int n = 0; n < D; n++)
        {
            int rowInSquare = n / d;
            int colInSquare = n - d * rowInSquare;
            int row = squareRow * d + rowInSquare;
            int col = squareCol * d + colInSquare;

            removePossibility(data, make_pair(row, col), value);
        }
    }

    void removePossibility(SolverData &data, pair<int, int> position, char value)
    {
        auto &possibilities = data.possibilities[position.first][position.second];
        int erased = possibilities.erase(value);

        if (erased == 1 && possibilities.size() == 1)
            data.fillQueue.push(position);
    }
};

void printBoard(vector<vector<char>> &board)
{
    for (int i = 0; i < board.size(); i++)
    {
        for (int j = 0; j < board[i].size(); j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    // This board is solvable without any guesses
    // vector<vector<char>> board{{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
    //                            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
    //                            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
    //                            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
    //                            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
    //                            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
    //                            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
    //                            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
    //                            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

    // This board needs some guessing
    vector<vector<char>> board{{'.', '.', '.', '.', '7', '.', '.', '.', '.'},
                               {'6', '.', '.', '1', '9', '.', '.', '.', '.'},
                               {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                               {'8', '.', '.', '.', '6', '.', '.', '.', '.'},
                               {'4', '.', '.', '8', '.', '.', '.', '.', '1'},
                               {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                               {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                               {'.', '.', '.', '4', '1', '9', '.', '.', '.'},
                               {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

    Solution solution;
    solution.solveSudoku(board);
    printBoard(board);

    return 0;
}