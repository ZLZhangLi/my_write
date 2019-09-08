//#include <iostream>
//#include <string>
//#include <vector>
//#include <map>
//#include <algorithm>
//#include <set>
//#include <limits.h>
//using namespace std;
//#pragma warning(disable:4996)
//
//std::vector<std::string> split(std::string str, std::string pattern)
//{
// std::string::size_type pos;
// std::vector<std::string> result;
//
// str += pattern;
// int size = str.size();
//
// for (int i = 0; i < size; i++)
// {
//  pos = str.find(pattern, i);
//  if (pos < size)
//  {
//   std::string s = str.substr(i, pos - i);
//   result.push_back(s);
//   i = pos + pattern.size() - 1;
//  }
// }
// return result;
//}


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
 int c;
 cin >> c;
 while (c--) {
  int t;
  cin >> t;
  vector<int> data(t);
  for (int i = 0; i < t; ++i) {
   cin >> data[i];
  }
  int res = 0;
  sort(data.begin(), data.end(), [](int a, int b) {return a > b; });
  while (data[2] > 0) {
   int tmp = data[2];
   res += tmp;
   data[0] = data[0] - tmp;
   data[1] = data[1] - tmp;
   //data[2] = 0;
   //sort(data.begin(), data.end(), [](int a, int b) {return a > b; });
   data.erase(data.begin() + 2);
  }
  cout << res << endl;
 }
 return 0;
}