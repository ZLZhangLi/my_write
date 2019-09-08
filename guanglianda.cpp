#include <iostream>
#include <math>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_set>
using namespace std;
int main(){
    int prices[50000];
    int fee;
    cin >> fee;
    while(cin >> prices[i]){
        i++;
        if(cin.get() == '\n')
            break;
    }
    int maxp_without = 0;
    int maxp_with = -prices[0];
    for(int i=1; i<prices.length; i++){
        maxp_without = Math.max(maxp_without, prices[i]+maxp_with-fee);
        maxp_with = Math.max(maxp_with, maxp_without-prices[i]);
    }
    cou << maxp_without << endl;
    return 0;
}
