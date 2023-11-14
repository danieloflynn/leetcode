#include <string>
#include <iostream>

using namespace std;

// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        if (n == 0)
        {
            return true;
        }

        int prev = 0;
        int curr = flowerbed[0];
        int next;

        for (int i = 1; i < flowerbed.size(); i++)
        {
            next = flowerbed[i];
            if (prev == 0 && curr == 0 && next == 0)
            {
                n -= 1;
                curr = 1;
            }
            prev = curr;
            curr = next;
        }

        if (prev == 0 && curr == 0)
        {
            n -= 1;
        }
        return n <= 0;
    }
};

int main()
{
    Solution s;

    vector<int> flowerpot = {1, 0, 0, 0, 1};

    cout << s.canPlaceFlowers(flowerpot, 1);

    return 0;
}

// int repeatCount = 0;
// bool atStart = true;

// for (int flower : flowerbed)
// {
//     if (flower == 0)
//     {
//         repeatCount++;
//     }
//     else
//     {
//         if (repeatCount >=2 && atStart){
//             n -= (repeatCount - 1) / 2;
//         }
//         if (repeatCount > 2)
//         {
//             n -= (repeatCount - 1) / 2;
//             if (n <= 0)
//             {
//                 return true;
//             }
//         }
//         repeatCount = 0;
//     }
// }
// if (repeatCount >= 2)
// {
//     n -= repeatCount / 2;
// }
// if (n <= 0)
// {
//     return true;
// }

// return false;