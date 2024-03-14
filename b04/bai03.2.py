# n = 6 => 1 2 3 6
# Một ước số của n thì chỉ thuộc [1, n]
# Dùng biến chạy x cho chạy từ 1 đến n (+=1) để kiểm tra xem n có chia hết cho x không
# Nếu có thì x là ước, thì in x ra

n = 9
x = 1
while x <= n:
    if n % x == 0:
        print(x)
    x += 1

