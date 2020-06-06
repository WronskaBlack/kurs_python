# Input:
# 4
# 4 11111
# 1 09
# 5 110011
# 0 1
# Sample Output
# Case #1: 0
# Case #2: 1
# Case #3: 2
# Case #4: 0


def ovation(audience):
    standing = 0
    friends = 0
    for index, element in enumerate(audience):
        if standing < index:
            friends += index - standing
            standing = index
        standing += int(element)
    return friends

#
# out = ""
# for i in range(int(input())):
#     inputs = input().split()
#     out += f"Case #{i + 1}: {ovation(inputs[1])} \n"
# print(out)
print(ovation("130001"))