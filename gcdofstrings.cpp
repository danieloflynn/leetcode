#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    string gcdOfStrings(string str1, string str2)
    {
        int str1Size = str1.size();
        int str2Size = str2.size();
        int minstr = min(str1Size, str2Size);
        string substr;

        for (int i = minstr; i > 0; i--)
        {
            if (str1Size % i == 0 && str2Size % i == 0)
            {
                substr = str1.substr(0, i);
                string s1;
                for (int j = 0; j < (str1Size / i); j++)
                {
                    s1 += substr;
                }
                if (s1 != str1)
                {
                    continue;
                }
                string s2;
                for (int j = 0; j < (str2Size / i); j++)
                {
                    s2 += substr;
                }

                if (s2 == str2)
                {
                    return substr;
                }
            }
        }

        return "";
    }
};

int main()
{
    Solution s;
    string str1 = "ABAB";
    string str2 = "ABABABAB";

    cout << s.gcdOfStrings(str1, str2);
}