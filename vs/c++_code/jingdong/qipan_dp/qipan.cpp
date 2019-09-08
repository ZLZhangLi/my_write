/*
#include<iostream>
#include<stack>
using namespace std;
const int Max = 10000;

struct Node
{
	int dist;
	int pre;
};

void Init(Node* gNode, int count)
{
	for (int i = 0; i < count; i++)
	{
		gNode[i].dist = Max;
		gNode[i].pre = -1;
	}
}
void Relax(Node* gNode, int** map, int u, int v, int node)
{
	if (gNode[v].dist > gNode[u].dist + map[v / node][v % node])
	{
		gNode[v].dist = gNode[u].dist + map[v / node][v % node];
		gNode[v].pre = u;
	}
}
int main(void)
{
	int hang, lie, i, j;
	cin >> hang >> lie;//hang:������lie������

	//��ԭʼ����
	int **map = new int*[lie];
	for (i = 0; i < hang; i++)
		map[i] = new int[lie];


	for (i = 0; i < hang; i++)
	for (j = 0; j < lie; j++)
		cin >> map[i][j];

	for (i = 0; i < hang; i++)
	{
		for (j = 0; j < lie; j++)
			cout << map[i][j] << " ";
		cout << endl;
	}

	int count = hang*lie;
	Node * gNode = new Node[count];
	int *S = new int[count];//����S�����汻�ҵ����·���Ľ����1��������0������QΪ����S�Ĳ���
	//S[i]��Ϊ��
	for (i = 0; i < count; i++)
		S[i] = 0;

	//Initial
	Init(gNode, count);
	gNode[0].dist = 0;
	gNode[0].pre = -1;
	int flag = 0;//���Q�Ƿ�Ϊ��
	while (flag < count)//ѭ���ڵ������
	{
		//find min
		int min = Max;
		int index = -1;
		for (i = 0; i < count; i++)
		{
			if (S[i] == 0 && gNode[i].dist < min)//S[i]δ�����뼯����
			{
				min = gNode[i].dist;
				index = i;
			}
		}
		S[index] = 1;
		flag++;
		int col = index / lie;
		int row = index % lie;
		//��ÿ���ڵ㷢����ÿ�������ɳڲ���
		if ((col - 1) >= 0)
		{
			Relax(gNode, map, index, index - lie, lie);
			if ((row - 1) >= 0)
				Relax(gNode, map, index, index - lie - 1, lie);
			if ((row + 1)<lie)
				Relax(gNode, map, index, index - lie + 1, lie);
		}
		if (col >= 0 && col < hang)
		{
			if ((row - 1) >= 0)
				Relax(gNode, map, index, index - 1, lie);
			if ((row + 1)<lie)
				Relax(gNode, map, index, index + 1, lie);
		}
		if ((col + 1) < hang)
		{
			Relax(gNode, map, index, index + lie, lie);
			if ((row - 1) >= 0)
				Relax(gNode, map, index, index + lie - 1, lie);
			if ((row + 1)<lie)
				Relax(gNode, map, index, index + lie + 1, lie);
		}

	}
	int cost = gNode[count - 1].dist + map[0][0];//��Ϊ��ʼ��Ҳ��Ȩ��
	cout << "Min cost is " << cost << endl;
	int path = count - 1;
	stack<int> stackPath;

	while (path != 0)
	{
		stackPath.push(path);
		path = gNode[path].pre;
	}
	stackPath.push(0);
	while (!stackPath.empty())
	{
		cout << stackPath.top() << " ";
		stackPath.pop();
	}

}
*/

#include<iostream>
using namespace std;

int main()
{
	int n, m, k; int x, y;
	cin >> n >> m >> k;
	int dp[100][100];
	int grid[100][100];
	for (int i = 0; i < k; i++)
	{
		cin >> x >> y;
		grid[x][y] = 1;
	}
	if (grid[0][0] == 1)
		cout << 0;
	for (int i = 1; i < n; i++)
		dp[i][0] = grid[i][0] == 1 ? 0 : dp[i - 1][0];//�������һ���߲�ͨ����һ��һ���߲�ͨ
	for (int i = 1; i < m; i++)
		dp[0][i] = grid[0][i] == 1 ? 0 : dp[0][i - 1];
	for (int i = 1; i < n; i++)
	for (int j = 1; j < m; j++)
		dp[i][j] = grid[i][j] == 1 ? 0 : dp[i - 1][j] + dp[i][j - 1];
	cout << dp[n - 1][m - 1];
	return 0;
}