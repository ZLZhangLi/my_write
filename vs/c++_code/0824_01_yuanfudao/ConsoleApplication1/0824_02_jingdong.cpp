#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	while (T)
	{
		int n, m;
		cin >> n >> m;
		vector<char> vec;
		vector<vector<char>> res;
		char str[300]; char c;
		int ticki, tickj;
		for (int i = 0; i<n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cin >> c;
				if (c == 'S')
				{
					ticki = i;
					tickj = j;
				}
				vec.push_back(c);
			}
			res.push_back(vec);
			vec.clear();
		}
		if (res[ticki][tickj + 1] == '#' && ticki == 0 && res[ticki + 1][tickj] == '#')
			cout << "NO";
		if (ticki == n - 1 && res[0][tickj] == '.')
			cout << "YES";
		res.clear();
		T--;
		if (T != 0)
			cout << endl;

	}
	system("pause");
	return 0;
}