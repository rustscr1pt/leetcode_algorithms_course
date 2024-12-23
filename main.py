from typing import List


def countElements(arr: List[int]) -> int:
    cleaned = set(arr)
    memo = 0
    for number in arr:
        if number + 1 in cleaned:
            memo += 1
    return memo

print(countElements([1,1,3,3,5,5,7,7]))