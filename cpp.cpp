#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll sum[1000011];
void sieve(int N)
{
    memset(sum, 0, sizeof(sum));
    for (int i = 2; i <= N; i++)
    {
        for (int j = i * 2; j <= N; j += i)
        {
            sum[j] += i;
        }
    }
}

int main()
{
    sieve(1000000);
    int l, r;
    cin >> l;
    cin >> r;
    ll cnt = 0;
    for (int i = l; i <= r; i++)
    {
        ll x = sum[i] + 1;
        if (x < 1000000 && i == sum[x] + 1)
        {
            cnt += 1;
            if (i == x)
                cnt -= 1;
            cout << i << " " << x << endl;
        }
    }
    cout << cnt / 2;
}