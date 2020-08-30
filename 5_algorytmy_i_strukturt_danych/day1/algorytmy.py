def as_bin(x: int) -> str:
    if x == 0:
        return "0b0"
    result = []
    while x:
        x, reminder = divmod(x, 2)
        result.append(str(reminder))
    return '0b' + ''.join(reversed(result))


# O(log n), pamięć O(3) ?

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# O(n), pamięć O(1)

def minmax(items: list) -> tuple:
    mini = items[0]
    maxi = items[0]
    for i in items:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
    return mini, maxi

def merge(items):
    result = []
    temp = items[0]
    for i in items:
        if i[0] > temp[1]:
            result.append(temp)
            temp = i
        else:
            if i[0] > temp[0]:
                val1 = temp[0]
            else:
                val1 = i[0]
            if i[1] > temp[1]:
                val2 = i[1]
            else:
                val2 = temp[1]
            temp = (val1, val2)
    result.append(temp)
    return result

class Solution:
    def twoSum(self, nums, target):
        items = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            value = items[i] + items[j]
            if value > target:
                j -= 1
            elif value < target:
                i += 1
            else:
                break
        a = nums.index(items[i])
        if items[i] == items[j]:
            b = nums.index(items[j], a+1)
        else:
            b = nums.index(items[j])
        return [a, b]


if __name__ == '__main__':
    # for i in range(10):
    #     print(as_bin(i), bin(i))
    # print(factorial(1))
    # print(minmax([-9, 9, -10, 9]))

    # [(1, 3), (2, 6), (8, 10), (7, 20)]
    # merge(
    #   [(1, 3), (2, 6), (8, 10), (7, 20)]
    # ) => [(1, 6), (7, 20)]
    print(merge([(-1, 1), (1, 3), (2, 6), (8, 10), (7, 20), (21, 22)]))



