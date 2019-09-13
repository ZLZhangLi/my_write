#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <math.h>

using namespace std;

/**
* Welcome to vivo !
*/

#define MAX_NUM 9

int helper(vector<int> &boxs, int i, int j, int k, int dp[100][100][100]){
	if (j < i) return 0;
	if (dp[i][j][k] > 0) return dp[i][j][k];
	int res = (1 + k) * (1 + k) + helper(boxs, i + 1, j, 0, dp);
	for (int m = i + 1; m <= j; ++m){
		if (boxs[m] == boxs[i]){
			if (helper(boxs, i + 1, m - 1, 0, dp) > helper(boxs, m, j, k + 1, dp)){
				res = helper(boxs, i + 1, m - 1, 0, dp);
			}
			else res = helper(boxs, m, j, k + 1, dp);
			//res = max(res, helper(boxs, i + 1, m - 1, 0, dp) + helper(boxs, m, j, k + 1, dp));
		}
	}
	return dp[i][j][k] = res;
}

int DFS(vector<int>& boxes, int l, int r, int k) {
	if (l > r) {
		return 0;
	}
	if (dp[l][r][k]) {
		return dp[l][r][k];
	}
	dp[l][r][k] = DFS(boxes, l, r - 1, 0) + (k + 1) * (k + 1); // box[l][r] result is box[l][r-1]+(k+1)^2
	for (int i = l; i < r; ++i) {
		if (boxes[i] == boxes[r]) {
			dp[l][r][k] = max(dp[l][r][k], DFS(boxes, l, i, k + 1) + DFS(boxes, i + 1, r - 1, 0));
		}
	}
	return dp[l][r][k];
}
int dp[100][100][100];


int removeBoxes(vector<int>& boxes) {
	return DFS(boxes, 0, boxes.size() - 1, 0);
}

int solution(vector<int> &boxs)
{
	// TODO Write your code here
	int n = boxs.size();
	int dp[100][100][100] = { 0 };
	return helper(boxs, 0, n - 1, 0, dp);
	return 1;
}


int main()
{
	int i = 0;
	vector<int> data(MAX_NUM);
	while (cin >> i){
		data.push_back(i);
		if (cin.get() != '\n')
			break;
	}
	int num = removeBoxes(data);
	//int num = solution(data);
	cout << num << endl;
	return 0;
}