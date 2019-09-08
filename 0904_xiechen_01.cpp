#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int main()
{
 string m_data;
 cin >> m_data;
 int size = m_data.size();
 vector<int> dp1(size, -1);
 vector<int> dp2(size, -1);
 map<char, int> mp;
 for (int i = size - 1; i >= 0; --i) {
    if (!mp.count(m_data[i])) mp[m_data[i]] = i;
 }
 for (int i = 0; i < size;++i) {
    dp1[i] = mp[m_data[i]];
 }
 int left = 0, right = 0;
 for (int i = 0; i < size;) {
    left = i;
    right = mp[m_data[i]];
    while (*max_element(dp1.begin() + left, dp1.begin() + right) > dp1[right]) {
    right = *max_element(dp1.begin() + left, dp1.begin() + right);
  }
  for (int j = i; j <= right; ++j) {
    dp2[j] = right;
  }
    i = right + 1;
 }
 vector<int> output;
 int pro = dp2[0];
 int cnt = 1;
 for (int i = 1; i < size; ++i) {
    if (dp2[i] == pro) {
    ++cnt;
    }
    else {
    output.push_back(cnt);
    cnt = 1;
    }
    pro = dp2[i];
 }
 output.push_back(cnt);
 string result;
 for (int i = 0; i < output.size(); ++i) {
    result += to_string(output[i]);
    result += ",";
 }
 cout << result.substr(0, result.size() - 1) << endl;
 return 0;
}