import radio as 廣播
import ustruct as 結構
import utime as 時間
from microbit import display as 燈光
from microbit import uart as 序列

序列.init(115200)
廣播.on()
燈光.scroll('ok')

while True:
    燈光.clear()
        
    包裝資料 = 廣播.receive_bytes()
    if 包裝資料 and len(包裝資料) == 8:
        燈光.set_pixel(4, 4, 3)
        序列.write(包裝資料)
    時間.sleep_ms(200)
    

