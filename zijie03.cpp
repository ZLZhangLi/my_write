#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <limits.h>
using namespace std;
#pragma warning(disable:4996)

std::vector<std::string> split(std::string str, std::string pattern)
{
	std::string::size_type pos;
	std::vector<std::string> result;

	str += pattern;
	int size = str.size();

	for (int i = 0; i < size; i++)
	{
		pos = str.find(pattern, i);
		if (pos < size)
		{
			std::string s = str.substr(i, pos - i);
			result.push_back(s);
			i = pos + pattern.size() - 1;
		}
	}
	return result;
}


#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <limits.h>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	int dir;
	cin >> dir;
	vector<vector<int>> data(4, vector<int>(4, 0));
	for (int i = 0; i < 4; ++i){
		for (int j = 0; j < 4; ++j){
			cin >> data[i][j];
		}
	}
	//1 上  2下  3左  4右
	if (dir == 1){
		vector<vector<int>> res;
		for (int i = 0; i < 4; ++i){ //列
			vector<int> tmp;
			for (int j = 0; j < 3;){
				if (data[j][i] == data[j + 1][i] && data[j][i] != 0){
					tmp.push_back(data[j][i] * 2);
					j += 2;
				}
				else{
					if (data[j][i] != 0) tmp.push_back(data[j][i]);
					j++;
				}
			}
			if (data[3][i] != 0 && data[3][i] != data[2][i] != 0) tmp.push_back(data[3][i]);
			res.push_back(tmp);
		}
		vector<vector<int>> print(4, vector<int>(4, 0));
		for (int i = 0; i < 4;++i){
			int j;
			vector<int> tmp = res[i];
			for (j = 0; j < tmp.size(); ++j){
				print[j][i] = tmp[j];
			}
			while (j < 4){
				print[j][i] = 0;
				++j;
			}
		}
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				cout << print[i][j] << " ";
			}
			cout << endl;
		}
	}
	else if (dir == 2){
		vector<vector<int>> res;
		for (int i = 0; i < 4; ++i){ //列
			vector<int> tmp;
			for (int j = 3; j > 0;){
				if (data[j][i] == data[j - 1][i] && data[j][i] != 0){
					tmp.push_back(data[j][i] * 2);
					j -= 2;
				}
				else{
					if (data[j][i] != 0) tmp.push_back(data[j][i]);
					j--;
				}
			}
			if (data[0][i] != 0 && data[0][i] != data[1][i]) tmp.push_back(data[0][i]);
			res.push_back(tmp);
		}
		vector<vector<int>> print(4, vector<int>(4, 0));
		for (int i = 0; i < 4; ++i){
			int j = 3;
			vector<int> tmp = res[i];
			for (j = 3; j > 3 - tmp.size(); --j){
				print[j][i] = tmp[3 - j];
			}
			while (j >= 0){
				print[j][i] = 0;
				--j;
			}
		}
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				cout << print[i][j] << " ";
			}
			cout << endl;
		}
	}
	else if (dir == 3){ //左
		vector<vector<int>> res;
		for (int i = 0; i < 4; ++i){ //列
			vector<int> tmp;
			for (int j = 0; j < 3;){
				if (data[i][j] == data[i][j + 1] && data[i][j] != 0){
					tmp.push_back(data[i][j] * 2);
					j += 2;
				}
				else{
					if (data[i][j] != 0) tmp.push_back(data[i][j]);
					j++;
				}
			}
			if (data[i][3] != 0 && data[i][3] != data[i][2]) tmp.push_back(data[i][3]);
			res.push_back(tmp);
		}
		vector<vector<int>> print(4, vector<int>(4, 0));
		for (int i = 0; i < 4; ++i){
			int j;
			vector<int> tmp = res[i];
			for (j = 0; j < tmp.size(); ++j){
				print[i][j] = tmp[j];
			}
			while (j < 4){
				print[i][j] = 0;
				++j;
			}
		}
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				cout << print[i][j] << " ";
			}
			cout << endl;
		}
	}
	else{
		vector<vector<int>> res;
		for (int i = 0; i < 4; ++i){ //列
			vector<int> tmp;
			for (int j = 3; j > 0;){
				if (data[i][j] == data[i][j - 1] && data[i][j] != 0){
					tmp.push_back(data[i][j] * 2);
					j -= 2;
				}
				else{
					if (data[i][j] != 0) tmp.push_back(data[i][j]);
					j--;
				}
			}
			if (data[i][0] != 0 && data[i][0] != data[i][1]) tmp.push_back(data[i][0]);
			res.push_back(tmp);
		}
		vector<vector<int>> print(4, vector<int>(4, 0));
		for (int i = 0; i < 4; ++i){
			int j = 3;
			vector<int> tmp = res[i];
			for (j = 3; j > 3 - tmp.size(); --j){
				print[i][j] = tmp[3 - j];
			}
			while (j >= 0){
				print[i][j] = 0;
				--j;
			}
		}
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				cout << print[i][j] << " ";
			}
			cout << endl;
		}
	}

	
	return 0;
}