so_kwh = int(input("Nhập số kwh điện đã tiêu thụ: "))
gia_bac_1 = 1678 
gia_bac_2 = 1734 
gia_bac_3 = 2014 
tien_bac1 = min(so_kwh, 100) * gia_bac_1
tien_bac2 = min(max(so_kwh - 100, 0), 100) * gia_bac_2
tien_bac3 = min(max(so_kwh - 200, 0), 100) * gia_bac_3
tong_tien = tien_bac1 + tien_bac2 + tien_bac3
print(f"Tổng số tiền điện phải trả: {tong_tien} VNĐ")

