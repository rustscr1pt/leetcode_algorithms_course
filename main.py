# def solving(list : list[list[int]]) -> list[list[int]]:
#     dictionary = {}
#     for match in list:
#         winner = match[0]
#         loser = match[1]
#         dictionary[winner] = dictionary[winner] + 1 if winner in dictionary else 1
#         dictionary[loser] = dictionary[loser] - 1 if loser in dictionary else -1
#     print(dictionary)


def solving(list : list[list[int]]) -> list[list[int]]:
    winner_set = set()
    loser_set = set()
    for match in list:
        winner = match[0]
        loser = match[1]
        winner_set.add(winner)
        if loser in loser_set:
            loser_set.remove(loser)
        else:
            loser_set.add(loser)
    return [[*winner_set], [*loser_set]]


print(solving([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))