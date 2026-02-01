// 977. Squares of a Sorted Array
/*
[-a, ... , b] -> elements
[ i, ... , j] -> indexs
if (-a)^2 > b -> add b and j-- | else add a and i++
*/


#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <cmath>
#include <bits/stdc++.h>


using namespace std;

class Solution {
public:
   vector<int> sortedSquares(vector<int>& nums) {
      vector<int> res;
      int start = 0;    int end = nums.size() - 1;
      while (start <= end){
         int power_a = pow(nums[start],2) ; 
         int power_b = pow(nums[end],2);
         if(power_a > power_b){
            res.push_back(power_a);
            start++;
         }else{
            res.push_back(power_b);
            end--;
         }
      }
      reverse(res.begin(),res.end());
      return res;

      // reverse the array
   }
};
