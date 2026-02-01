//344. Reverse String
#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

// Pointers solution


class Solution {
public:
   void reverseString(vector<char>& s) {
      char* start = &s[0];          //pointer to start
      char* end = &s[s.size()-1];   //pointer to end
      while (start < end){
         char temp = *start;
         *start = *end;
         *end = temp;
         start++;
         end--;
      }
   }
}; 


/*

class Solution {
public:
   void reverseString(vector<char>& s) {
      for(int i = 0 ; i < s.size() / 2; i++){
         int end_idx = s.size() - 1 - i;
         char aux_s = s[i];   
         s[i] = s[end_idx];
         s[end_idx] = aux_s;
      }
   }
}; 
*/