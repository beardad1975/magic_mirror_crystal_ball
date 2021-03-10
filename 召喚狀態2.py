import time as 時間

from 語音模組 import *
from 模擬3D模組 import *


import 共用
import 鏡子狀態1
import 召喚狀態2
import 魔鏡狀態3
import 立體狀態4
import 視覺特效狀態5
import 水晶球狀態6

def 進入():
    print('進入 召喚狀態2')
    共用.召喚動畫.開始()    

def 更新():    
    if 辨識成功了嗎():
        文字 = 取得辨識文字()
        if '魔鏡' in 文字  :
            共用.切換(魔鏡狀態3 )
            
def 按下(按鍵):
    pass
    
def 離開():
    print('離開 召喚狀態2')
    共用.召喚動畫.結束()
    共用.召喚文字.有效狀態 = False
    共用.閃電.有效狀態 = False
    暫停語音辨識()
    
    

