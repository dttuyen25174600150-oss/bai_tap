ma_tran = [
    [1, 1, 1, 1],
    [2, 4, 6, 8],
    [3, 5, 7, 9],
]
tong_lon_nhat = None
chi_so_hang_lon_nhat = -1
i = 0
for hang in ma_tran:
    tong_hang_hien_tai = 0
    for phan_tu in hang:
        tong_hang_hien_tai += phan_tu
    if tong_lon_nhat is None or tong_hang_hien_tai > tong_lon_nhat:
        tong_lon_nhat = tong_hang_hien_tai
        chi_so_hang_lon_nhat = i
    i += 1
print(f"Hàng có tổng lớn nhất là hàng thứ: {chi_so_hang_lon_nhat + 1} (chỉ số {chi_so_hang_lon_nhat})")
print(f"Tổng lớn nhất là: {tong_lon_nhat}")
print(f"Chi tiết hàng đó: {ma_tran[chi_so_hang_lon_nhat]}")
