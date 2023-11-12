#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int sum = nums[0] + nums[1] + nums[2] - target;
        int newSum;
        for (int i = 0; i < nums.size(); i++)
        {
            int front = i + 1;
            int back = nums.size() - 1;
            while (front < back)
            {
                newSum = nums[i] + nums[front] + nums[back] - target;
                if (newSum == 0)
                {
                    return 0;
                }
                if (abs(newSum) < abs(sum))
                {
                    sum = newSum;
                }
                if (newSum < 0)
                {
                    front++;
                }
                else
                {
                    back--;
                }
            }
        }
        return sum + target;
    }
};