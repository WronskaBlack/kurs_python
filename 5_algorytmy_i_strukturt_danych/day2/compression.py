def compress(text):
    if not text:
        return []
    result = []
    temp = text[0]
    count = 0
    for i in text:
        if i == temp:
            count += 1
        else:
            result.append((temp, count))
            temp = i
            count = 1
    result.append((temp, count))
    return result

# def compress(text: str) -> list:
#     if len(text) == 0:
#         return []
#     result = []
#     counter = 1
#     for prev, current in zip(text[:-1], text[1:]):
#         if prev == current:
#             counter += 1
#         else:
#             result.append((prev, counter))
#             counter = 1
#     result.append((text[-1], counter))
#     return result

def decompress(items):
    result = ''
    for char, count in items:
        result += char * count
    return result


s = 'aaaaa'
com = compress(s)
print(com)
dec = decompress(com)
print(dec)
print(s == dec)