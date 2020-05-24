// FIXME Wrong Answer on Test Set 2

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solve(int n, vector<int> &nums) {
    int maxNeg = 0, maxPos = 0, curNeg = 0, curPos = 0;
    for (int num : nums) {
        curNeg = min(curNeg, 0) + num;
        curPos = max(curPos, 0) + num;
        maxNeg = min(maxNeg, curNeg);
        maxPos = max(maxPos, curPos);
    }
    int absMax = max(abs(maxPos), abs(maxNeg));
    int maxRoot = floor(sqrt(absMax));

    // count[0] = count of -absMax
    // count[absMax] = count of 0
    // count[2*absMax] = count of +absMax
    vector<int> count(absMax * 2 + 1);
    count[absMax]++;
    int prefixSum = 0, answer = 0;
    for (int i = 0; i < n; i++) {
        prefixSum += nums[i];
        for (int j = 0; j <= maxRoot; j++) {
            int target = prefixSum - j * j;
            if (-absMax <= target && target <= absMax)
                answer += count[absMax + target];
        }
        count[absMax + prefixSum]++;
    }

    return answer;
}

int ti;

int main() {
    int t;
    cin >> t;
    for (ti = 1; ti <= t; ti++) {
        int n;
        cin >> n;
        vector<int> nums(n);
        for (size_t i = 0; i < n; i++) {
            cin >> nums[i];
        }
        int result = solve(n, nums);
        cout << "Case #" << ti << ": " << result << endl;
    }
}