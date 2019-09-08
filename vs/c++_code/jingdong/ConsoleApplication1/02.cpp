#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int c;
	cin >> c;
	while (c--) {
		int t;
		cin >> t;
		vector<int> data(t);
		for (int i = 0; i < t; ++i) {
			cin >> data[i];
		}
		int res = 0;
		sort(data.begin(), data.end(), [](int a, int b) {return a > b; });
		while (data[2] > 0) {
			int tmp = data[2];
			res += tmp;
			data[0] = data[0] - tmp;
			data[1] = data[1] - tmp;
			data[2] = 0;
			sort(data.begin(), data.end(), [](int a, int b) {return a > b; });
		}
		cout << res << endl;
	}
	return 0;
	system("pause");
}