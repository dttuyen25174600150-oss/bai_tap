def chuyen_doi_nhiet_do(do_c):
    do_f = do_c * 1.8 + 32
    return do_f
do_c = float(input("nhập nhiệt độ(độ C):"))
do_f = chuyen_doi_nhiet_do(do_c)
print("độ F",do_f)