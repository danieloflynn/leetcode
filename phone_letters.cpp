#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

class Solution
{
public:
    vector<string> letterCombinations(string digits)
    {
        unordered_map<char, vector<char>> numbers = {
            {'2', {'a', 'b', 'c'}},
            {'3', {'d', 'e', 'f'}},
            {'4', {'g', 'h', 'i'}},
            {'5', {'j', 'k', 'l'}},
            {'6', {'m', 'n', 'o'}},
            {'7', {'p', 'q', 'r', 's'}},
            {'8', {'t', 'u', 'v'}},
            {'9', {'w', 'x', 'y', 'z'}}};
        char d = digits[0];
        digits.erase(0, 1);
        vector<string> digitCombo = {};
        vector<string> newDigitCombo;

        for (char l : numbers[d])
        {
            string l1;
            l1 = l;
            digitCombo.push_back(l1);
        }
        for (char digit : digits)
        {
            for (string s : digitCombo)
            {
                for (char l : numbers[digit])
                {

                    newDigitCombo.push_back(s + l);
                }
            }
            digitCombo = newDigitCombo;
            newDigitCombo = {};
        }
        return digitCombo;
    }
};

int main()
{
    string str = "23";
    Solution s;
    vector<string> el = s.letterCombinations(str);
    for (auto el2 : el)
        cout << el2 << " ";
    return 0;
}