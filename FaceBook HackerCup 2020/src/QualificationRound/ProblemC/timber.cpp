// ----- Problem C - Qualification Round FHC 2020 - Original Solution ---------------
// Timber
// Solution by Jacob Plachta

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=(n)-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x * x); }
string plural(string s) { return(Sz(s) && s[Sz(s) - 1] == 'x' ? s + "en" : s + "s"); }

const int INF = (int)1e9;
const LD EPS = 1e-12;
const LD PI = acos(-1.0);

#define GETCHAR getchar_unlocked

bool Read(int& x) {
  char c, r = 0, n = 0;
  x = 0;
  for (;;) {
    c = GETCHAR();
    if ((c < 0) && (!r))
      return(0);
    if ((c == '-') && (!r))
      n = 1;
    else if ((c >= '0') && (c <= '9'))
      x = x * 10 + c - '0', r = 1;
    else if (r)
      break;
  }
  if (n)
    x = -x;
  return(1);
}

#define LIM 800005

int N;
PR P[LIM];
unordered_map<int, int> M[2]; // [left-to-right, right-to-left]

int ProcessCase()
{
  int i, d, ans = 0;
  Read(N);
  for (i=0; i<N; i++) {
    Read(P[i].x), Read(P[i].y);
  }
  sort(P, P + N);
  for (d=0; d<2; d++) {
    M[d].clear();
  }
  for (d=0; d<2; d++) {
    if (d == 1)
      reverse(P, P + N);
    for (i=0; i<N; i++)
      Max(M[d][P[i].x + P[i].y * (d ? -1 : 1)], M[d][P[i].x] + P[i].y);
    for (auto I : M[d])
      Max(ans, I.y + M[1 - d][I.x]);
  }
  return(ans);
}

int main() {
  int T, t;
  Read(T);
  Fox1(t, T)
    printf("Case #%d: %d\n", t, ProcessCase());
  return(0);
}
