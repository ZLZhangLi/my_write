
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_set>
using namespace std;


#define LOCAL
#ifdef LOCAL
#pragma warning(disable:4996)
#endif
void local_input()
{
#ifdef LOCAL
 freopen("input.txt", "r", stdin);
#endif
}

int longestCommonPrefix(string& str1, string& str2)
{
 int len1 = str1.size();
 int len2 = str2.size();
 int i = 0, j = 0;
 int res = 0;
 while (i < len1 && j < len2) {
  if (str1[i] == str2[j]) {
   ++res;
   ++i;
   ++j;
  }
  else break;
 }
 return res;
}

int main()
{
 //local_input();
 int k;
 cin >> k;
 vector<string> data(k);
 for (int i = 0; i < k; ++i) {
  cin >> data[i];
 }
 int m, n;
 while (cin >> m >> n) {
  cout << longestCommonPrefix(data[m-1], data[n-1]) << endl;
 }
 return 0;
}