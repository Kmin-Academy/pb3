
k = int(input("Nhap k: "))
s = ""
x = 1
while x <= k:
    if x % 2 == 0:
        s += "$"
    else:
        s += "*"
    x += 1

print(s)