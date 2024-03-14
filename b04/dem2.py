a = 3
b = 9

dem = 0
x = a
while x <= b:
    if x % 2 == 0:
        dem += 1
    x += 1

print(dem)