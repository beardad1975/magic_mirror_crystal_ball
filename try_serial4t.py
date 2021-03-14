from 序列模組 import *
import struct as 結構
import time as 時間


序列連線 = 連接microbit(例外錯誤=False, 讀取等待=0)


while True:

    位元組資料 = 序列連線.接收(位元組=8)
    
    if 位元組資料 and len(位元組資料) == 8:
        清單 = 結構.unpack('hhhh',位元組資料)
        序列連線.清除緩除區()
        print(清單)
    時間.sleep(0.1)

    

