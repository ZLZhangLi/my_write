#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(){
	char a[110];
	string s;
	int m;
	cin >> s >> m;
	int L = s.size();
	for (int i = 0, q = -1; i < L - m; i++){
		int max = 0;
		for (int j = q + 1; j <= m + i; j++){
			if (max < s[j]){
				max = s[j], q = j;
			}
			a[i] = max;
		}
		a[L - m] = '\0';		
	}
	puts(a);
	return 0;
}