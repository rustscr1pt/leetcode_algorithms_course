# To summarize what each variable does in the code:
#
#     left: the leftmost index of our current window
#     right: the rightmost index of our current window
#     curr: the sum of our current window
#     ans: the length of the longest valid window we have seen so far
#
# Iterate right over the input to add elements to the window. Update curr by adding nums[right] to it. When the window becomes invalid (curr > k), remove elements from the window by subtracting nums[left] from curr. Then increment left. We need to do this until the window becomes valid again, so we use a while loop.
#
# The size of a window is right - left + 1. Update our answer only when the window becomes valid.

def find_length(string: str) -> int:
    left = current = answer = 0
    for right in range(len(string)):
        if string[right] == '0':
            current += 1
        while current > 1:
            if string[left] == '0':
                current -= 1
            left += 1
        answer = max(answer, right - left + 1)
    return answer





answer = find_length("1101100111")
print(answer)
