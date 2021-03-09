from 模擬3D模組 import *
from 視覺模組 import *


import time as 時間

import 共用
import 鏡子狀態1
import 召喚狀態2
import 魔鏡狀態3
import 立體狀態4
import 視覺特效狀態5
import 水晶球狀態6


def 進入():
    print('進入 視覺特效狀態5')
    共用.視覺特效動畫.開始()

def 更新():
    陣列 = 擷取單張影像(共用.攝影機)
    共用.鏡子.多維陣列貼圖 = 255 - 陣列[共用.行1:共用.行2, 共用.列1:共用.列2]
    
    
def 按下(按鍵):
    pass
        
      
    
    
def 離開():
    print('離開 視覺特效狀態5')
    共用.鏡子.有效狀態 = False
    共用.可怕文字.有效狀態 = False
