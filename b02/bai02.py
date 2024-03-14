# Input
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# if a == b and b == c:
#     print("Yes")
# else:
#     print("No")

# De Morgan: (X and Y) phủ định ra là: !X or !Y

# Cách 2
# a = 4, b = 5, c = 4
# Lý luận sai: a khác b, b khác c => a khác c
if a != b or b != c:
    print("No")
else:
    print("Yes")




