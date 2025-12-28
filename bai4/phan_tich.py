from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri
ds = [5, 2, 9, 1, 7]
print(f"Danh sách sau khi sắp xếp: {sap_xep_tang_dan (ds)}")
my_dict = {"name": "Python", "version": 3.12}
k = "name"
print(f"Giá trị của khóa '{k}': {lay_gia_tri(my_dict, k)}")