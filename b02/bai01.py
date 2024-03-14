# B1: Input: Số nguyên x, Output: Âm hay không
# B2: Điều kiện: x < 0
# B3: Code
# B4: Kiểm thử

# Xử lý input
x = int(input("Nhap so nguyen x:"))

# Xử lý tính toán
kq = ""
if x < 0:
    kq = "Yes"
else:
    kq = "No"

# Xử lý output
print(kq)