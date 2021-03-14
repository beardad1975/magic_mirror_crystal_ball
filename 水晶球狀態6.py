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
    
    共用.水晶球動畫.開始()
    
    


def 更新():
    #共用.水晶球.旋轉y += 0.2

    魔杖動作 = 共用.取得魔杖動作()
    if 魔杖動作:
            x = 魔杖動作[0]            
            比例 = 2000 / 360
            角度x = -x // 比例
            print('角度x', 角度x)
            共用.水晶球.旋轉y = 角度x
            
    if 辨識成功了嗎():
        文字 = 取得辨識文字()
        if '魔鏡' in 文字  :
            共用.切換(魔鏡狀態3 )
    
def 按下(按鍵):
    pass
            
    
def 離開():
    print('離開 水晶球狀態6')
    共用.水晶球動畫.結束()
    共用.水晶球.有效狀態 = False
    共用.水晶球玻璃.有效狀態 = False
    共用.導覽文字.有效狀態 = False
    暫停語音辨識()