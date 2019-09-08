#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<sstream>
#define LL long long
#define OJ_DEBUG 0
#define READ_FILE 1
using namespace std;
const int NN_MAX = 17;
const int MM_MAX = 100010;
const int INF = 0x3f3f3f3f;
/**********************************************************/
int maps[NN_MAX][NN_MAX], dp[1 << NN_MAX][NN_MAX];
int t, n, m, ans;
/**********************************************************/
int min_2(int x, int y) { return x < y ? x : y; }
int max_2(int x, int y) { return x > y ? x : y; }
void floyd();
void hamiton();
int dfs(int s, int id);
/**********************************************************/
int main()
{
	t = 1;
	while (t--)
	{
		scanf("%d %d", &n, &m);
		memset(maps, 0x3f, sizeof(maps));
		for (int i = 0; i <= n; i++) maps[i][i] = 0;
		int a1, a2, a3;
		for (int i = 0; i < m; i++) {
			scanf("%d %d %d", &a1, &a2, &a3);
			if (maps[a1 + 1][a2 + 1] > a3)
				maps[a1 + 1][a2 + 1] = maps[a2 + 1][a1 + 1] = a3;
		}
		floyd();
		//hamiton();
		memset(dp, 0, sizeof(dp));
		int ans = dfs(1, 1);
		if (ans == INF) {
			printf("%d\n", -1);
		}
		else {
			printf("%d\n", ans);
		}
		
	}
	return 0;
}
void floyd()
{
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (maps[i][k] < INF && maps[k][j] < INF)
					maps[i][j] = min_2(maps[i][j], maps[i][k] + maps[k][j]);
}
void hamiton()
{
	memset(dp, 0x3f, sizeof(dp));
	dp[1][1] = 0;
	//枚举所有状态，二进制s每位按序代表一个城市，回路从1开始必须包含城市1
	for (int s = 3; s <= (1 << n) - 1; s++) if (s & 1) {
		for (int i = 2; i <= n; i++) if (s&(1 << (i - 1))) { //状态s经过城市i
			if (s == (1 << (i - 1))) //只过城市i，这是dp边界
				dp[s][i] = maps[1][i];
			else {
				for (int j = 1; j <= n; j++)
					//枚举不是城市i的在状态s中的其他城市j，并以j为中间点，求出最小的dp[s][i]，类似floyd思想
					if ((s&(1 << (j - 1))) && j != i)
						dp[s][i] = min_2(dp[s][i], dp[s ^ (1 << (i - 1))][j] + maps[j][i]);
			}
		}
	}
	ans = INF;
	for (int i = 2; i <= n; i++)
		ans = min_2(ans, dp[(1 << n) - 1][i] + maps[i][1]);
	if (ans == INF) ans = 0;//n=1
}
//dfs(s,id)当前已访问的城市状态为s，上一次递归访问城市id
//dp[s][id]表示从1到id(不包括s中的城市)的最短路径长度
int dfs(int s, int id)
{
	//printf("%d %d\n",s,id);
	if (dp[s][id] > 0) return dp[s][id];//如果dp[s][id]有值说明已最小
	int mi = INF;
	for (int i = 1; i <= n; i++) {
		if (i == 1 && s == (1 << n) - 1)//如果状态为11..1，说明到达递归边界
			mi = min_2(mi, maps[id][1]);
		if (s&(1 << (i - 1))) continue;
		//遍历所有未访问城市i，得到所有最短路中的最小值
		mi = min_2(mi, dfs(s | (1 << (i - 1)), i) + maps[i][id]);
	}
	//printf("-%d\n",mi);
	return dp[s][id] = mi;//dp[s][id]更新即最小
}