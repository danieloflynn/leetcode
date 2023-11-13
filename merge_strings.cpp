#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string newstr = "";
        int i = 0;
        while (i < word1.size() && i < word2.size())
        {
            newstr += word1[i];
            newstr += word2[i];
            i++;
        }
        while (i < word1.size())
        {
            newstr += word1[i];
            i++;
        }
        while (i < word2.size())
        {
            newstr += word2[i];
            i++;
        }

        return newstr;
    }
};

int main()
{
    string w1 = "word1";
    string w2 = "word2";
    Solution s;
    cout << s.mergeAlternately(w1, w2);
}