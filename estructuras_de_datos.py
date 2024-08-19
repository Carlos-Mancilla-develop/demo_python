x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print("x:", x)
print("y:", y)

for i, f in enumerate(x):
    print("i:", i, "f:", f)

for e in y:
    print("e:", e)