#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution
{
public:
   vector<string> summaryRanges(vector<int> &nums)
   {
      vector<string> res;
      int start = 0;
      for (int i = 0 ; i < nums.size(); i++ ){
         if (i + 1 == nums.size() || nums[i] + 1 != nums[i + 1]){    // if is the last number or is not a secuence (like 5,6)
            if (i == start){      // if is a isolate number we push it
               res.push_back(to_string(nums[i]));
            }  
            else{
               res.push_back(to_string(nums[start]) + "->" + to_string(nums[i]));
            }
            start = i + 1; // we plus 1 to reach i
         }
      }
      return res;
   }
};