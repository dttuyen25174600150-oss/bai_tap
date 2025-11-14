tien = float(input("Nhập số tiền gửi ban đầu: "))
lai = float(input("Nhập lãi suất năm (%): ")) / 100
tien1 = round(tien * (1 + lai), 2)
tien2 = round(tien * (1 + lai)**2, 2)
tien3 = round(tien * (1 + lai)**3, 2)
print("Tiền sau 1 tháng:", tien1)
print("Tiền sau 2 quý:", tien2)
print("Tiền sau 3 năm:", tien3)