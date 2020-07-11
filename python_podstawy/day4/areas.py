"""
Calculate areas of the figures and save them in dict
areas = {
    'triangles': [0.5, 5],
    'rectangles: [...],
    'squares': [...],
}
"""
#             a h    a h
triangles = [[1,2], [3,4]]
# 1/2 a * h
#          a a a a a a a a a
squares = [2,4,5,6,2,1,2,4,6]
# a * a
#              a b    a b    a b
rectangles = [[2,4], [7,6], [4,2]]
# a * b
areas = {}

areas_triangles = []
for a, h in triangles:
    areas_triangles.append(1/2 * a * h)
areas["triangles"] = areas_triangles

areas_squares = []
for a in squares:
    areas_squares.append(a * a)
areas["squares"] = areas_squares

areas_rectangles = []
for a, b in rectangles:
    areas_rectangles.append(a * b)
areas["rectangles"] = areas_rectangles

print(areas)