#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

class Solution
{
public:
   bool containsDuplicate(vector<int> &nums)
   {
      unordered_set<int> aux;
      for (int i = 0; i < nums.size(); i++)
      {
         if (aux.find(nums[i]) != aux.end())
            return true;
         aux.insert(nums[i]);
      }
      return false;
   }
};