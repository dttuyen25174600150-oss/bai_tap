import sys
import os
duong_dan_thu_vien = os.path.abspath("../thu_vien_chung")
sys.path.append(duong_dan_thu_vien)
import su_ly_so as kiem_tra_so_nguyen_to
n = 17
if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")

