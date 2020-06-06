def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in word1:
        if i not in word2:
            return False
        word2 = word2.replace(i, '')
    return True


print(is_anagram("kot", "tok"))
print(is_anagram("cat", "dog"))