#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_set>
using namespace std;

#define LOCAL
#ifdef LOCAL
#pragma warning(disable:4996)
#endif
void local_input()
{
#ifdef LOCAL
 freopen("input.txt", "r", stdin);
#endif
}

std::vector<std::string> split(std::string str, std::string pattern)
{
 std::string::size_type pos;
 std::vector<std::string> result;

 str += pattern;//扩展字符串以方便操作
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


void swap(vector<string> &arr, int i, int j)
{
 string tmp = arr[i];
 arr[i] = arr[j];
 arr[j] = tmp;
}


int partition(vector<string> &arr, int l, int r)
{
 string pivot = arr[l];
 int mask = l;
 for (int i = l + 1; i <= r; i++) {
  if (arr[i] > pivot) {
   mask++;
   swap(arr, i, mask);
  }
 }
 swap(arr, mask, l);
 return mask;
}
void quickSort(vector<string> &arr, int l, int r)
{
 if (l < r) {
  int p;
  p = partition(arr, l, r);
  quickSort(arr, l, p - 1);
  quickSort(arr, p + 1, r);
 }
}

int main()
{
 //local_input();
 string input;
 cin >> input;
 vector<string> data = split(input, ",");
 quickSort(data, 0, data.size() - 1);
 string res;
 for (int i = 0; i < data.size(); ++i) {
  res += data[i];
  res += ",";
 }
 cout << res.substr(0, res.size() - 1) << endl;

 return 0;
}