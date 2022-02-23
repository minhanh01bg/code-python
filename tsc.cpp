#include <bits/stdc++.h>
using namespace std;

bool check(int n)
{
    int cnt = 0;
    while (n)
    {
        if (n % 10 == 6 || n % 10 == 8)
        {
            cnt += 1;
        }
        n /= 10;
    }
    return cnt;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int ans = 0;
        for (int i = 8; i <= n; i += 8)
        {
            ans += check(i);
        }
        cout << ans << endl;
    }
}