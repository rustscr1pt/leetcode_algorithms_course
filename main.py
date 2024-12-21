from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        starting_point = 0
        end_point = len(s) - 1
        while starting_point < end_point:
            s[starting_point], s[end_point] = s[end_point], s[starting_point]
            starting_point += 1
            end_point -= 1
