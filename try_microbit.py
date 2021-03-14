from microbit import uart as 序列
import utime as 時間



序列.init(115200)


for 數 in range(10):
    序列.write(str(數))
    時間.sleep_ms(1000)
