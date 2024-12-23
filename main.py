def checkIfPangram(sentence: str) -> bool:
    hash = {}
    for index in range(len(sentence)):
        letter = sentence[index]
        if letter.isalpha() and letter.islower():
            hash[letter] = index
    if len(hash) == 26:
        return True
    else:
        return False



def checkIfPangram(sentence: str) -> bool:
    if len(set(sentence)) == 26:
        return True
    else:
        return False