// Question (https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/) 
// --------
// Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

// You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

// Return an integer array answer, where each answer[i] is the answer to the ith query.

 

// Example 1:

// Input: queries = ["cbd"], words = ["zaaaz"]
// Output: [1]
// Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

// Example 2:

// Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
// Output: [1,2]
// Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


int f(string& s){
    char min_character = *min_element(s.begin(), s.end());
    int count = std::count(s.begin(), s.end(), min_character);
    return count; 
}

class Solution {
public:
    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        vector<int> v;
        for (int i =0; i<queries.size() ; i++ ){
            int c = f(queries[i]);
            int count_ = 0; 
            for (int j=0; j<words.size() ; j++ ){
                if (c<f(words[j])){
                    count_++;
                }
            }
            v.push_back(count_);
        }
        return v;
    }
};