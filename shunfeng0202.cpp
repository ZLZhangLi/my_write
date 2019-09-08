#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int root[100],rank[100];
//初始化n个元素 
void init(int n){
    for(int i=0;i<n;i++){
        root[i]=i;
        rank[i]=0;
    }
}
//查询树的根 
int find(int x){
    if(root[x]==x){
        return x;
    } else{
        return root[x]=find(root[x]);
    }
}
//合并x和y所属的集合 
void unite(int x,int y){
    x=find(x);
    y=find(y);
    if(x==y)
     return;
    if(rank[x]<rank[y]){
        root[x]=y;
    }
    else{
        root[y]=x;
        if(rank[x]==rank[y])
        {
            rank[x]++;
        }
    }
}
int main(){
    int n,m,x,y,k;
    cin>>n>>k>>m;
    init(n);
    for(int i=0;i<m;i++){
        cin>>x>>y;
        unite(x,y); 
    }
    int sum1[100]={0},sum2[100]={0};
    int sum=0;
    sum1[sum]=root[0];
    sum++; 
    for(int i=1;i<n;i++){

        for(int j=0;j<sum;j++)
        {
            if(root[i]==sum1[j])
            break;
            if(j==sum-1)
            {
                sum1[sum]=root[i];
                sum++;
            }
        }

    }
    cout<<sum<<endl;
    /*for(int i=0;i<sum;i++){
        for(int j=0;j<n;j++){
            if(root[j]==sum1[i]){
                sum2[i]++;
            } 
        }

    }
    sort(sum2,sum2+sum);
    for(int i=0;i<sum;i++){
        cout<<sum2[i]<<" ";
    }
*/
    return 0;
} 
