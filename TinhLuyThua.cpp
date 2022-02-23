#include <bits/stdc++.h>

// Typedefs

#define ll long long
#define ull unsigned long long
#define pb push_back
#define eb emplace_back
#define cl(C) C.clear()
#define cint cpp_int
#define all(C) C.begin(), C.end()
#define Begin()   \
    int N;        \
    cin >> N;     \
    cin.ignore(); \
    while (N--)

// Commands

// Loops

#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FORD(i, a, b) for (int i = a; i >= b; i--)
#define FORA(x, C) for (auto x : C)
#define WHILE(x, y) while (cin >> x >> y)
#define WHILEF(x, y, f) while (f >> x >> y)
#define WHILE2(x) while (cin >> x)
#define WHILEGL(a) while (getline(cin, a))
#define WHILEGLF(a, f) while (getline(f, a))

#define faster()                      \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);
#define pause() system("pause");

// Namespaces

using namespace std;

ll M;

ll power(ll a, ll b, ll mod)
{
    if (b == 0)
        return 1 % mod;
    if (b == 1)
        return a % mod;
    ll k = power(a, b / 2, mod) % mod;
    if (b & 1)
        return (((k % mod) * (k % mod)) % mod * (a % mod)) % mod;
    return ((k % mod) * (k % mod)) % mod;
}

ll totient(ll n)
{
    ll result = 1;
    ll p = 3;
    if (n % 2 == 0)
    {
        n /= 2;
    }
    while (n % 2 == 0)
    {
        result *= 2;
        n /= 2;
    }
    while (p * p <= n)
    {
        if (n % p == 0)
        {
            result *= (p - 1);
            n /= p;
        }
        while (n % p == 0)
        {
            result *= p;
            n /= p;
        }
        p += 2;
    }
    if (n >= 2)
        result *= (n - 1);
    return result;
}

ll power2(ll a, ll b)
{
    if (b == 0)
        return 1 % M;
    if (b == 1)
        return a % M;
    ll k = power2(a, b / 2) % M;
    if (b & 1)
        return (((k % M) * (k % M)) % M * (a % M)) % M;
    return (k % M) * (k % M) % M;
}

ll modpow(ll p, ll z, ll b, ll c, ll m) // : # (p^z)^(b^c) mod m
{
    ll cp = 0;
    while (m % p == 0 && cp < z)
    {
        cp += 1;
        m /= p;
    }
    //	vec(p(ll,ll)) C = totient(m);
    //	ll t = 1;
    //	FOR(i,0,C.size()-1)
    //	{
    //		t = t*power2(C[i].first,C[i].second-1)*(C[i].first-1);
    //	}
    ll t = totient(m);
    ll exponent = ((power(b, c, t) * z) % t + t - (cp % t)) % t;
    //    cout << p << " " << z << " " << b << " " << c << " " << exponent << endl;
    return power2(p, cp) * power(p, exponent, m);
}

int main()
{
    //	vec(p(ll,ll)) C;
    faster();
    Begin()
    {
        ll a, b, c, d;
        cin >> a >> b >> c >> d >> M;
        a %= M;
        ll N = totient(M);
        b %= N;
        c %= N;
        ll K = totient(N);
        d %= K;
        if (M == 1)
        {
            cout << 0 << endl;
            continue;
        }
        if (b == 0)
        {
            cout << 1 % M << endl;
            continue;
        }
        if (d == 0)
        {
            c = 1;
            d = 1;
        }
        if (c == 0)
        {
            cout << 1 % M << endl;
            continue;
        }
        if (a == 0)
        {
            cout << 0 << endl;
            continue;
        }
        ll result = 1;
        ll p = 3;
        ll cp = 0;
        while (a % 2 == 0)
        {
            a /= 2;
            cp++;
        }
        if (cp != 0)
        {
            ll temp = modpow(2, cp, c, d, M);
            result *= temp;
            result %= M;
        }
        while (p * p <= a)
        {
            cp = 0;
            while (a % p == 0)
            {
                a /= p;
                cp++;
            }
            if (cp != 0)
            {
                ll temp = modpow(p, cp, c, d, M);
                result *= temp;
                result %= M;
            }
            p += 2;
        }
        if (a >= 2)
        {
            result *= modpow(a, 1, c, d, M);
        }
        ll RESULT = power(result, b, M);
        cout << RESULT % M << endl;
    }
}
