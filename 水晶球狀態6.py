import time as 時間
from 模擬3D模組 import *
from 語音模組 import *

import 共用
import 鏡子狀態1
import 召喚狀態2
import 魔鏡狀態3
import 立體狀態4
import 視覺特效狀態5
import 水晶球狀態6

def 進入():
    print('進入 水晶球狀態6')
    
    #共用.導覽動畫.開始()
    
    


def 更新():
    共用.水晶球.旋轉y += 0.2
    if 共用.導覽動畫.結束了嗎 and 語音說完了嗎():
        共用.切換(魔鏡狀態3 )
    

    
def 按下(按鍵):
    pass
            
    
def 離開():
    print('離開 水晶球狀態6')
    共用.水晶球.有效狀態 = False
    共用.水晶球玻璃.有效狀態 = False
    共用.導覽文字.有效狀態 = False
