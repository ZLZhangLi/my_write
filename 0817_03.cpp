#include<vector>
#include<stack>
#include<queue>
#include<unordered_map>
#include<unordered_set>
#include<cstring> //memset需要用
using namespace std;

const int N = 110;
long long v[N], w[N];
long long n, m;

long long max0 = 2*1e12;
bool check(long long x )
{
 long long sum=0;
 for (int i = 0; i < n; i++)
  if (v[i] < x) sum += w[i] * (x - v[i]);
 return sum <= m;

}
int main(){

 //FILE *fp1;
 //freopen_s(&fp1, "in.txt", "r", stdin);

 cin >> n >> m;

 for (int i = 0; i<n; i++) cin >> v[i];
 for (int i = 0; i < n; i++) cin >> w[i];

 long long  l = 0;
 long long r = max0;
 while (l < r)
 {
  long long mid = l + r >> 1;
  if (check(mid)) l = mid + 1;
  else r=mid;
 }
 cout << l-1;
 return 0;
}