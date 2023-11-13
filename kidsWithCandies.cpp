#include <string>
#include <iostream>

using namespace std;

// There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

// Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

// Note that multiple kids can have the greatest number of candies.

class Solution
{
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies)
    {
        vector<bool> greatestCandies;
        int maxCandies = 0;
        for (int candy : candies)
        {
            if (candy > maxCandies)
            {
                maxCandies = candy;
            }
        }
        for (int i = 0; i < candies.size(); i++)
        {
            if (candies[i] + extraCandies >= maxCandies)
                greatestCandies.push_back(true);
            else
            {
                greatestCandies.push_back(false);
            }
        }

        return greatestCandies;
    }
};

int main()
{
    vector<int> candies = {4, 2, 1, 1, 2};
    Solution s;
    vector<bool> out = s.kidsWithCandies(candies, 1);
    for (auto o : out)
        cout << o;
}
