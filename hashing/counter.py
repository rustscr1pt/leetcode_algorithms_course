# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
#
# This problem deals with substrings and has a constraint on the substrings (at most k distinct characters). These characteristics let us know that we should consider sliding window. Remember, the idea of a sliding window is to add elements by sliding to the right until the window violates the constraint. Once it does, we shrink the window from the left until it no longer violates the constraint. In this problem, we are concerned with the number of distinct characters in the window. The brute force way to check for this constraint would be to check the entire window every time, which could take O(n)O(n) time. Using a hash map, we can check the constraint in O(1)O(1).
#
# Let's use a hash map counts to keep count of the characters in the window. This means we will map letters to their frequency. The length (number of keys) in counts at any time is the number of distinct characters. When we remove from the left, we can decrement the frequency of the elements being removed. When the frequency becomes 0, we know this character is no longer part of the window, and we can delete the key.
#
# Please review the sliding window article if you have forgotten the sliding window algorithm.
#
# In this problem, the constraint metric is "how many unique characters are in the window". The numeric restriction is <= k. We can use a hash map counts that keeps track of the frequency of each character in the window. The length of counts is the number of keys, which is also the constraint metric. Therefore the window is invalid when counts.length > k.
#
# When we add a character s[right], we increment its frequency in counts by one. If it doesn't exist in counts, we insert a new key value pair s[right]: 1.
#
# When we remove a character s[left], we decrement its frequency in counts by one. If the frequency becomes 0, we know that this character no longer exists. Therefore we delete the key from the hash map, which also decreases the length of counts.
#
# Recall that the length of a window is right - left + 1.

from collections import defaultdict


def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans



# Example 2: 2248. Intersection of Multiple Arrays
#
# Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.
#
# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
#
# The problem states that each individual array contains distinct integers. This means that a number appears n times if and only if it appears in all arrays.
#
# Let's use a hash map counts to count the frequency of elements. We iterate over each of the inner arrays and update counts with every element. After going through all the arrays, we can iterate over our hash map to see which numbers appear n times.

from collections import defaultdict


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)

# This problem is a good discussion point for why a hash map is convenient. You may be thinking, since our keys are integers, why can't we just use an array instead of a hash map? We could, but the problem is that the array needs to be at least as large as the maximum element. What if we have a test case like [1, 2, 3, 1000]? We need to initialize an array of size 1000, even though only a few of the indices will actually be used. Therefore, using an array could end up being a huge waste of space. Sure, sometimes it would be more efficient because of the overhead of a hash map, but overall, a hash map is much safer. Even if 99999999999 is in the input, it doesn't matter - the hash map handles it like any other element.
#
# Let's say that there are nn lists and each list has an average of mm elements. To populate our hash map, it costs O(n⋅m)O(n⋅m) to iterate over all the elements. The next loop iterates over all unique elements that we encountered. If all elements are unique, this can cost up to O(n⋅m)O(n⋅m), although this won't affect our time complexity since the previous loop also cost O(n⋅m)O(n⋅m). Finally, there can be at most mm elements inside ans when we perform the sort, which means in the worst case, the sort will cost O(m⋅log⁡m)O(m⋅logm). This gives us a time complexity of O(n⋅m+m⋅log⁡m)=O(m⋅(n+log⁡m))O(n⋅m+m⋅logm)=O(m⋅(n+logm)). If every element in the input is unique, then the hash map will grow to a size of n⋅mn⋅m, which means the algorithm has a space complexity of O(n⋅m)O(n⋅m).





# Example 3: 1941. Check if All Characters Have Equal Number of Occurrences
#
# Given a string s, determine if all characters have the same frequency.
#
# For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

# Using our knowledge of hash maps and sets, this is a straightforward problem. Use a hash map counts to count all character frequencies. Iterate through s and get the frequency of every character. Check if all frequencies are the same.
#
# Because a set ignores duplicates, we can put all the frequencies in a set and check if the length is 1 to verify if the frequencies are all the same.
#
# Click here for a more detailed explanation if needed
#
# Recall from the first article of the chapter that sets ignore frequency. If you add the same element to a set 100 times, the first operation will add it, then the next 99 will do nothing.
#
# In this problem, we want to determine if there exists only one unique frequency. We can first find the frequencies by counting each character using a hash map. After counting, the values of the hash map are our frequencies.
#
# If there is only one unique frequency, then after adding all the values to a set, the set will have a length of 1. If there are any characters with different frequencies, then the set would have a length greater than 1, as it would hold all unique frequencies.

from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        frequencies = counts.values()
        return len(set(frequencies)) == 1

# Given nn as the length of s, it costs O(n)O(n) to populate the hash map, then O(n)O(n) to convert the hash map's values to a set. This gives us a time complexity of O(n)O(n). The space that the hash map and set would occupy is equal to the number of unique characters. As previously discussed, some people would argue that this is O(1)O(1) since the characters come from the English alphabet, which is bounded by a constant. A more general answer would be to say that the space complexity is O(k)O(k), where kk is the number of characters that could be in the input, which happens to be 26 in this problem.

