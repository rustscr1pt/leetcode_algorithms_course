# Example 1: 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.
#
# For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.

# The "correct" order is determined by whatever the previous opening bracket was. Whenever there is a closing bracket, it should correspond to the most recent opening bracket. For example, if the string starts "({[", and the next 3 characters are closing brackets, then they should be in the order of how recently their opening bracket appeared: "]})" (otherwise we would end up with something like "[)" occurring). The order is last in, first out (LIFO) - the last opening bracket we saw is the first one we should close, which is perfect functionality for a stack to provide.
#
# As we iterate over the string, if we see an opening bracket, we should put it on the stack. If we see a closing bracket, we can check the most recent unclosed opening bracket by popping it from the top of the stack. If it matches, then continue, if it doesn't, or there is no opening bracket on the stack at all (this would occur in a case like "{}]"), then we know the string is invalid. In the end, there should be no unmatched open brackets (like in the case of "(){"), so the stack should be empty for the string to be valid.
#
# How can we associate the opening and closing brackets together? We can use a hash map to map each opening bracket to its closing bracket. Then, when we see a closing bracket, we can use the top of the stack as a key and check if the value is equal to the current character.

# We iterate over the string and try to process each bracket. At any given time, a stack holds all opening brackets we have seen so far that has not yet been closed. Every time we see an opening bracket, we push it onto the stack.
#
# When we see a closing bracket, the most recent unmatched opening bracket must match. Otherwise, you would have a case of (} etc. somewhere. The top of the stack is the most recent unmatched opening bracket. If we have a match, we can just pop from the stack and move on. If we have a mismatch, the string is invalid. If the stack is empty, it means there is no available opening bracket - the string is also invalid in this case.
#
# By using a stack, we can easily keep a history of unmatched opening brackets. If the stack is empty at the end, it means we matched all opening brackets.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in matching:  # if c is an opening bracket
                stack.append(c)
            else:
                if not stack:
                    return False

                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False

        return not stack

# Because the stack's push and pop operations are O(1)O(1), this gives us a time complexity of O(n)O(n), where nn is the size of the input array. This is because each element can only be pushed or popped once. The space complexity is also O(n)O(n) because the stack's size can grow linearly with the input size.
#
# The key to recognizing the stack solution for this problem is seeing that the problem follows a LIFO nature, where the last (most recent) opening bracket is the first to be closed.



# Example 2: 1047. Remove All Adjacent Duplicates In String
#
# You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.
#
# For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.
#
# The tricky part of this problem is that not all removals are necessarily available at the start. As you can see in the example, deleting the "aa" is only possible after deleting the "bb". We don't need to delete the first character until we have already iterated quite a bit past it. What if the input was s = "abccba"? We have the same problem with the b now as well, and the a is two layers back. The deletion order is c -> b -> a. This follows the LIFO pattern, where the last (most recent) character is the first one to be deleted (the first half of characters being deleted is "abc", and we need to delete the c, then b, then a).
#
# When we recognize a LIFO pattern, we know we can use a stack. Iterate over the input and put characters in the stack. At each step, if the top of the stack is the same as the current character, we know that they are adjacent (at some point in time) and can be deleted.
#
# We are concerned about matching characters that will be adjacent to each other at any point in time. There could be two characters that will eventually be deleted, but not until other characters between them have been deleted first. The characters between them are "in the way".
#
# When we use a stack, we keep a history of characters that are "in the way" of each other. For example, with "abccba", the c and b deletions are in the way of the a deletion.
#
# After 3 iterations, the stack is ["a", "b", "c"]. Once the "c" is deleted, the next character in the stack is "ready" to be deleted. Once the "b" is deleted, the "a" is finally ready to be deleted.
#
# The stack maintains the order for us. The main observation needed to recognize the stack solution is that the most recently seen character is the first one that needs to be deleted.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)



# Example 3: 844. Backspace String Compare
#
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
# For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".
#
# Once again, we can recognize that the backspace follows the LIFO pattern, where the first character to be deleted is the one that was most recently typed. We can just simulate the typing of the strings using a stack, and then compare them at the end.
#
# When typing characters, push them onto a stack. Whatever character is at the top of the stack is the most recently typed character, so when we backspace, we can just pop. Make sure to be careful of the edge case where we backspace on an empty string.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)