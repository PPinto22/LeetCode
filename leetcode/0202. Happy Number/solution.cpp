#include<unordered_set>

using namespace std;

class Solution
{
public:
    int digitSum(int n)
    {
        int sum = 0;
        while (n > 0)
        {
            int lastDigit = n % 10;
            n /= 10;
            sum += lastDigit * lastDigit;
        }
        return sum;
    }

    bool isHappy(int n)
    {
        unordered_set<int> seen;

        while (true)
        {
            if (n == 1)
                return true;
            if (seen.find(n) != seen.end())
                return false;

            seen.insert(n);
            n = digitSum(n);
        }
    }
};