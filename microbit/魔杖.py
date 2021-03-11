import radio as 廣播
import ustruct as 結構
from microbit import display as 燈光
from microbit import accelerometer as 加速度
import utime as 時間

廣播.on()

while True:
    燈光.clear()
    x = 加速度.get_x()
    y = 加速度.get_y()
    z = 加速度.get_z()
    晃動 = 加速度.is_gesture('shake')
    
    包裝資料 = 結構.pack('hhhh',x, y, z, 晃動)
    廣播.send_bytes(包裝資料)    
    燈光.set_pixel(0, 0, 3)
    時間.sleep_ms(100)


