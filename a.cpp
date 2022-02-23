#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll mod = 1e9 + 7;
const ll _ = 1e6 + 11;
const ll N = 1e6 + 11;
ll PowerMod(ll a, ll n, ll m = mod)
{
    if (!n || a == 1)
        return 1ll;
    ll s = PowerMod(a, n >> 1, m);
    s = s * s % m;
    return n & 1 ? s * a % m : s;
}

// factorials, fact-inverses, unbounded
ll fact[_], finv[_];
void init(int N)
{
    int i;
    for (*fact = i = 1; i < N; ++i)
        fact[i] = (ll)fact[i - 1] * i % mod;
    --i, finv[i] = PowerMod(fact[i], mod - 2);
    for (; i; --i)
        finv[i - 1] = (ll)finv[i] * i % mod;
}

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
//
int pn = 0, c[N], p[78540];
void sieve(int n)
{
    int i, j, v;
    memset(c, -1, sizeof c);
    for (i = 2; i <= n; ++i)
    {
        if (!~c[i])
            p[pn] = i, c[i] = pn++;
        for (j = 0; (v = i * p[j]) <= n && j <= c[i]; ++j)
            c[v] = j;
    }
}


int32_t main()
{
}