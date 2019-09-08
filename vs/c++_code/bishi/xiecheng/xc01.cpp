#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int main()
{
	string data;
	cin >> data;
	int size = data.size();
	vector<int> dp(size, -1);
	vector<int> dpMerge(size, -1);
	map<char, int> mp;
	for (int i = size - 1; i >= 0; --i) {
		if (!mp.count(data[i])) mp[data[i]] = i;
	}
	for (int i = 0; i < size; ++i) {
		dp[i] = mp[data[i]];
	}
	int left = 0, right = 0;
	for (int i = 0; i < size;) {
		left = i;
		right = mp[data[i]];
		while (*max_element(dp.begin() + left, dp.begin() + right) > dp[right]) {
			right = *max_element(dp.begin() + left, dp.begin() + right);
		}
		for (int j = i; j <= right; ++j) {
			dpMerge[j] = right;
		}
		i = right + 1;
	}
	vector<int> out;
	int pre = dpMerge[0];
	int cnt = 1;
	for (int i = 1; i < size; ++i) {
		if (dpMerge[i] == pre) {
			++cnt;
		}
		else {
			out.push_back(cnt);
			cnt = 1;
		}
		pre = dpMerge[i];
	}
	out.push_back(cnt);
	string res;
	for (int i = 0; i < out.size(); ++i) {
		res += to_string(out[i]);
		res += ",";
	}
	cout << res.substr(0, res.size() - 1) << endl;
	return 0;
}