#include <bits/stdc++.h>

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

// Co

#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FOR2(i, a, b) for (ll i = a; i <= b; ++i)

// Get values

// Clear containers

// Customize containers

#define SORT(C) sort(C.begin(), C.end())
#define SORTD(C, x) sort(C.begin(), C.end(), greater<x>())


// Containers

#define vec(x) vector<x>

// System

#define faster()                      \
	ios_base::sync_with_stdio(false); \
	cin.tie(0);                       \
	cout.tie(0);

// Namespaces

using namespace std;

// 5^26, 3^38, 2^64

ll powerOf2[64], powerOf3[39], powerOf5[27];

vec(ll) factor;

void ready()
{
	factor.clear();
	factor.pb(1);
	powerOf2[0] = 1;
	powerOf3[0] = 1;
	powerOf5[0] = 1;
	FOR(i, 1, 62)
	{
		powerOf2[i] = powerOf2[i - 1] * 2;
		factor.pb(powerOf2[i]);
	}
	FOR(i, 1, 38)
	{
		powerOf3[i] = powerOf3[i - 1] * 3;
		factor.pb(powerOf3[i]);
	}
	FOR(i, 1, 27)
	{
		powerOf5[i] = powerOf5[i - 1] * 5;
		factor.pb(powerOf5[i]);
	}
}

void factory()
{
	ready();
	FOR(i, 1, 62)
	{
		FOR(j, 1, 38)
		{
			if (powerOf2[i] > 1e18 / powerOf3[j])
				break;
			factor.pb(powerOf2[i] * powerOf3[j]);
			// cout<<powerOf2[i] * powerOf3[j]<<endl;
			FOR(k, 1, 27)
			{
				if (powerOf2[i] * powerOf3[j] > 1e18 / powerOf5[k])
					break;
				factor.pb(powerOf2[i] * powerOf3[j] * powerOf5[k]);
			}
		}
	}
	FOR(j, 1, 38)
	{
		FOR(k, 1, 27)
		{
			if (powerOf3[j] > 1e18 / powerOf5[k])
				break;
			factor.pb(powerOf3[j] * powerOf5[k]);
			// cout<<powerOf3[j] * powerOf5[k]<<endl;
		}
	}
	FOR(i, 1, 62)
	{
		FOR(k, 1, 27)
		{
			if (powerOf2[i] > 1e18 / powerOf5[k])
				break;
			factor.pb(powerOf2[i] * powerOf5[k]);
		}
	}
	SORT(factor);
	// cout<<factor[0]<<endl;
}

int main()
{
	factory();
	faster();
	Begin()
	{
		ll a;
		cin >> a;
		ll x = lower_bound(all(factor), a) - factor.begin();
		if (factor[x] == a)
			cout << x + 1 << endl;
		else
			cout << "Not in sequence" << endl;
	}
}
