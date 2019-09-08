#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
#include<fstream>
#include<numeric>
#include<algorithm>
using namespace std;

#define LOCAL

#ifdef LOCAL
#pragma warning(disable:4996)
#endif

int main() {
 int n, k;
 cin >> n >> k;
 vector<int> data(n, 0);
 for (int i = 0; i < n; ++i){
  cin >> data[i];
 }
 long long minSum = 0;
 long long sum = 0;
 int res = 0;
 for (int i = 0; i < k; ++i){
  sum += data[i];
 }
 minSum = sum;
 for (int i = 1; i <= n - k; ++i){
  long long tmp = sum + data[i + k - 1];
  tmp = tmp - data[i - 1];
  if (tmp < minSum){
   minSum = tmp;
   res = i;
  }
  sum = tmp;
 }
 cout << res + 1 << endl;
 return 0;
}