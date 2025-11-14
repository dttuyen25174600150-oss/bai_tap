luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))
luong_mot_ngay = luong_co_ban / 22
luong_thang = luong_mot_ngay * so_ngay_cong
thuong = luong_thang * 0.10 * (so_ngay_cong > 22)
phat = luong_thang * 0.05 * (so_ngay_cong < 22)
tong_luong = luong_thang + thuong - phat
print(f"Tổng lương thực nhận: {tong_luong:.2f} VNĐ")