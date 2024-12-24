def main(text: str) -> int:
    dictionary = {}
    constant = "balloon"
    highest = 0
    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    print(dictionary)
    for char in constant:
        if dictionary.get(char, 0) > highest:
            highest = dictionary[char]
        else:
            highest = 0
    return highest

print(main("balon"))