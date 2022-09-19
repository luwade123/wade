#include <iostream>
#include <vector>
using namespace std;

vector<int> two(int num)
{
    vector<int> ans;
    cout << num;
    for (int i = 0; i < 64; i++)
    {
        ans.push_back(num % 2);
        num = num / 2;
    }
    return ans;
}

int main()
{
    int n;
    int m;
    cin >> n >> m;
    long long in[200000];
    int process[2][64];
    vector<int> tmp;
    int pt = 0;
    int start;
    int sum = 0;
    for (int i = 0; i < m; i++)
    {
        cin >> in[i];
    }
    tmp = two(in[0]);

    for (int i = 0; i < m; i++)
    {
        if (tmp[i] == 1)
        {
            if (start != 0)
            {
                sum += i - start;
                start = i;
            }
            start = i;
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = start + 1; j < m; j++)
        {
            if (process[i][j] == 1)
            {
                sum += j - start;
                start = j;
            }
        }
    }
}