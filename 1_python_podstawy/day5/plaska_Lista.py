"""
Przekształć listę na płaską
"""

L = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
L2 = []
for li in L:
    for i in li:
        L2.append(i)

print(L2)
# L = [1,2,3,4,5,6,7,8,9]