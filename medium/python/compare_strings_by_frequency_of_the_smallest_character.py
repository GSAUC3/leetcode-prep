# Question: 1170 (https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/) 
# Medium 

# Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

# You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

# Return an integer array answer, where each answer[i] is the answer to the ith query.

# Example 1:

# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

# Example 2:

# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


from typing import List
import numpy as np

# Solution 1: 
def f(s:str) -> int:
    l = sorted(s) # sort the string
    count = 1 
    sample = l[0] 
    for i in range(1, len(l)):
        # iterate from 2nd element to last character 
        # and increment the count by 1 upon finding the 
        # same character as sample 
        if l[i] == sample:
            count += 1
    return count

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # for each query go through all the words, 
        # and append the number of words that satisfy the 
        # given condition 
        answer = []
        for q in queries: 
            c = 0
            Fq = f(q)
            for w in words: 
                if Fq <f(w):
                    c+=1
            answer.append(c)
        return answer




# Solution 2:

f = lambda s: s.count(min(s)) # lambda function to count the frequency of the smallest character

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        q = list(map(f, queries)) # list of frequencies of the smallest character in queries
        w = np.array(sorted(list(map(f, words)))) # sorted list of frequencies of the smallest character in words

         # for each frequency in queries, find the number of frequencies in words that are greater than it
        # np.searchsorted() function returns the index of the first element in w that is greater than or equal to each element in q 
        # side='right' means that if the element is found, the index of the next element is returned
        # len(w) - np.searchsorted() gives the number of elements in w that are greater than the element in q i.e the count of elements in w that are greater than the element in q
        return [int((len(w) - np.searchsorted(w,i,side='right'))) for i in q]
