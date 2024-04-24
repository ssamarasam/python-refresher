from sys import getsizeof

point1 = {"x": 1, "y": 2}
point2 = dict(a=0, x=3, y=4)
print(point1)
print(point2)
print(point2["x"])
point2["z"] = 5
if "a" in point2:
    print(point2["a"])
print(point2)
print(point2.get("u"))
print(point2.get("u", 0))
del point2["a"]
print(point2)
for key in point2:
    print(key, point2[key])

for key, value in point2.items():
    print(key, value)


values = {x: x * 2 for x in range(4)}
print(values)


values1 = (x for x in range(100000))
# print(values1)
# for i in values1:
#     print(i)
print("gen: ", getsizeof(values1))
