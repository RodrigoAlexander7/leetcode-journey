#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
#include <unordered_map>
using namespace std;

// 242. Valid Anagram 

class Solution {
public:
   bool isAnagram(string s, string t) {
      if(s.length() != t.length()) return false;
      unordered_map<char, int> count_s;
      unordered_map<char, int> count_t;
      for(char letter : s) count_s[letter] += 1;
      for(char letter : t) count_t[letter] += 1;
      return (count_s==count_t);
   }  
};