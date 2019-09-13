#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
#include<fstream>
#include<numeric>
#include<algorithm>
using namespace std;

//输入k个数字
int k;
cin >> k;
vector<int> data(k);
for (int i = 0; i < k; i++){
    cin >> data[i];
}

//输入一行数据，未知长度
while(cin >> i){
    data.push_back(i);
    if(cin.get() != '\n')
        break;
}