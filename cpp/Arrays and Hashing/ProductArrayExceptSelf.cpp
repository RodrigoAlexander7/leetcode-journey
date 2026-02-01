// 238. Product of Array Except Self

#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            vector<int> res;    
            int len = nums.size();        

            // calculate the list of prefix
            vector<int> prefix;
            int aux_prefix = 1;
            for (int i = 0; i < len; i++){
                prefix.push_back(aux_prefix);
                aux_prefix *= nums[i];
            }
            // calculate the list of sufix
            
            vector<int> sufix(len,0);   // fixed size and initialize in 0
            int aux_sufix = 1;
            for(int i = len - 1; i >= 0 ; i--){ // until 0 cause we neet to iterate over nums[0] lol
                sufix[i] = aux_sufix;
                aux_sufix *= nums[i];
            }

            for(int i = 0; i < len; i++){
                res.push_back(prefix[i] * sufix[i]);
            }
            return res;
        }
};