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
    print('進入 立體狀態4')
    共用.立體動畫.開始()

def 更新():
    共用.愛心.旋轉y += 2
    
                
def 按下(按鍵):
    pass
    
        
      
    
    
def 離開():
    print('離開 立體狀態4')
    共用.立體動畫.結束()
    共用.舞台.背景顏色 = color.rgb(0, 0, 0)
    共用.愛心.有效狀態 = False
    共用.美麗文字.有效狀態 = False
    
    
