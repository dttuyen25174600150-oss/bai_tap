t = tuple(map(int, input("Nhập tuple: ").split()))
chan = ()
le = ()
tong_chan = tong_le = 0
for x in t:
    if x % 2 == 0:
        chan += (x,)
        tong_chan += x
    else:
        le += (x,)
        tong_le += x
print(chan, tong_chan)
print(le, tong_le)
