# Example 1: 49. Group Anagrams
#
# Given an array of strings strs, group the anagrams together.
#
# For example, given strs = ["eat" ,"tea" ,"tan" ,"ate" ,"nat" ,"bat"], return [["bat"] ,["nat" ,"tan"] ,["ate" ,"eat" ,"tea"]].

# How can we check if two strings are anagrams of each other? We could use two hash maps, count all the characters in each string, and then compare if the hash maps are the same. This is very cumbersome to implement and also doesn't help us with grouping strings together if a group has more than 2 strings. For each group, we need a way to uniquely identify the group.
#
# The cleanest way to know if two strings are anagrams of each other is by checking if they are equal after both being sorted. Also, all strings in a group will be the same when sorted, so we can use the sorted version as a key. We can map these keys to the groups themselves in a hash map, and then our answer is just the values of the hash map.
#
# Essentially, every group has its own "identifier" (the sorted string), and we can use this identifier to group them in a hash map easily.
#
# A group could have many strings in it. We need a way to easily identify what strings belong to what group.
#
# Two strings are anagrams of each other if and only if they are sorted. This makes sense because when you sort a string, the characters are forced to appear in a well defined order. By definition, anagrams have the same letters, so when these letters appear in the same order, they must be equal.
#
# If we have a string "bcab", then sort it, we have "abbc". This is its "identifier" because every anagram of "bcab" will also result in "abbc" when sorted. We can use the identifier of each string as a hash map key to easily group all the anagrams together.

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())

# Note for Python: dictionary.values() doesn't actually return a list, but actually a view object. We need to convert it to a list first.
#
# Given n as the length of strs and m as the average length of the strings, we iterate over each string and sort it, which costs O(n⋅m⋅log⁡m)O(n⋅m⋅logm). Then, we need to iterate over the keys. In the worst case scenario, when there are no matching anagrams, there will be nn groups, which means this will cost O(n)O(n), giving an overall time complexity of O(n⋅m⋅log⁡m)O(n⋅m⋅logm) (the final +n+n is dominated). The space complexity is O(n⋅m)O(n⋅m) as each string will be placed in an array within the hash map.
#
# Another way to solve this problem is to use a tuple of length 26 representing the count of each character as the key instead of the sorted string. This would technically solve the problem in O(n⋅m)O(n⋅m) because the 26 is a constant defined by the problem, but for test cases with smaller strings it would be slower due to the constant factor which is hidden by big O.
#
# It also assumes that the strings can only have 26 different characters, which is valid here but less general and less resistant to follow-ups.


# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Input: jewels = "z", stones = "ZZ"
# Output: 0

def numJewelsInStones(jewels: str, stones: str) -> int:
    stones_dictionary = {}
    counter = 0
    for element in stones:
        if element in stones_dictionary:
            stones_dictionary[element] += 1
        else:
            stones_dictionary[element] = 1
    for jewel in jewels:
        if jewel in stones_dictionary:
            counter += stones_dictionary[jewel]
    return counter