#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){


	int m, n;
	cin >> n >> m;
	vector<vector<double>> d(n + 1, vector<double>(m + 1, 0));

	for (int i = 1; i <= n; i++){
		d[i][0] = 1;
		d[i][1] = (double)(i) / (i + 1);
	}


	for (int i = 2; i <= m; i++){
		d[1][i] = double(1) / (i + 1);
	}

	for (int i = 2; i <= n; i++){
		for (int j = 2; j <= m; j++){
			d[i][j] = double(i) / (i + j)
				+ double(j) / (i + j)*(j - 1) / (i + j - 1) * double(i) / (i + j - 2)*d[i - 1][j - 2];

			if (j - 2>0){
				d[i][j] += double(j) / (i + j)*(j - 1) / (i + j - 1) * double(j - 2) / (i + j - 2)*d[i][j - 3];
			}
		}
	}

	double ans = round(d[n][m] * 100000) / 100000;
	cout << ans << endl;
	return 0;
}