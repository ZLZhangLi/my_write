/*
#include<iostream>
#include<map>
#include <vector>
#include<stack>
using namespace std;
int GetStack(int(*d)[2], int i, int n, stack<int> &st)
{
	int j;
	for (j = i; j<n; j++)
	{
		if (d[i][j] == 1)
		{
			st.push(j);
		}
	}
	return st.size();
}

int GetChildGrape(int(*gid)[2], int n)
{
	stack<int> st;
	map<int, int> mapstor;
	int num = 0;
	int i;
	for (i = 0; i<n; i++)
	{
		if (mapstor.count(i) == 1) continue;
		else mapstor[i] = 1;
		int result = GetStack(gid, i, n, st);
		if (result == 0)
		{
			num++;
		}
		else
		{
			while (st.size() != 0)
			{
				int tmp = st.top();
				mapstor[tmp] = 1;
				st.pop();
				GetStack(gid, tmp, n, st);
			}
			num++;
		}
	}
	return num;
}
int main()
{
	int n, m, k;
	int res = 0;
	cin >> n >> m >> k;
	//vector<vector<int> > gid(k, vector<int>(2));
	int gid[100000][2];
	for (int i = 0; i < k; i++){
		cin >> gid[i][0] >> gid[i][1];
	}
	res = GetChildGrape(gid, n);
	cout << res - 1 << endl;
	return 0;
}
*/
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int n, m, x, y, k;
	int a = 12;
	a += a -= a*a;
	//int b = 1;
	cout << a << endl;

	return 0;
}
