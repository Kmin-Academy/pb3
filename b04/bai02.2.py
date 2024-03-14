# Lần 0: s = ""
# Lần 1: s = "*"
# Lần 2: s ="**"
# Lần 3: s = "***"
# Tổng quát: s += "*"

k = int(input("Nhap k: "))
s = ""
x = 1
while x <= k:
    s += "*"
    x += 1

print(s)


# while k > 0:
#     k -= 1