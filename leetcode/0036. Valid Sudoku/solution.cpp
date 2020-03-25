#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        // Rows
        if (std::any_of(board.begin(), board.end(), hasDuplicates))
            return false;

        // Columns
        for (size_t i = 0; i < 9; i++)
        {
            vector<char> column;
            for (size_t j = 0; j < 9; j++)
            {
                column.push_back(board[j][i]);
            }
            if (hasDuplicates(column))
                return false;
        }

        // Boxes
        for (size_t i = 0; i < 3; i++)
        {
            for (size_t j = 0; j < 3; j++)
            {
                vector<char> box;
                for (size_t k = 0; k < 9; k++)
                {
                    int lineInSquare = k / 3;
                    int x = 3 * i + (k - 3 * lineInSquare);
                    int y = 3 * j + lineInSquare;
                    box.push_back(board[x][y]);
                }

                if (hasDuplicates(box))
                    return false;
            }
        }

        return true;
    }

    static bool hasDuplicates(vector<char> &group)
    {
        set<char> seen;
        for (char c : group)
        {
            if (c != '.' && seen.count(c) > 0)
            {
                return true;
            }
            seen.insert(c);
        }
        return false;
    }
};

int main()
{
    vector<vector<char>> board{{'.', '.', '4', '.', '.', '.', '6', '3', '.'},
                               {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
                               {'5', '.', '.', '.', '.', '.', '.', '9', '.'},
                               {'.', '.', '.', '5', '6', '.', '.', '.', '.'},
                               {'4', '.', '3', '.', '.', '.', '.', '.', '1'},
                               {'.', '.', '.', '7', '.', '.', '.', '.', '.'},
                               {'.', '.', '.', '5', '.', '.', '.', '.', '.'},
                               {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
                               {'.', '.', '.', '.', '.', '.', '.', '.', '.'}};

    Solution solution;

    cout << solution.isValidSudoku(board) << endl;

    return 0;
}