import time as 時間


from 模擬3D模組 import *
from 視覺模組 import *

import 共用
import 鏡子狀態1 
import 召喚狀態2 
import 登場狀態3 
import 指令狀態4 
import 特效狀態5  
import 導覽狀態6


def 進入():
    print('進入 鏡子狀態1')
    共用.目前時間 = 時間.time()
   

    陣列 = 擷取單張影像(共用.攝影機)
    共用.鏡面.多維陣列貼圖 = 陣列[共用.行1:共用.行2, 共用.列1:共用.列2]
    共用.鏡面.有效狀態 = True
    共用.鏡面.顏色 = color.rgba(255,255,255,0)
    共用.鏡面.淡入(持續=2)
    
    

def 更新():
    陣列 = 擷取單張影像(共用.攝影機)
    共用.鏡面.多維陣列貼圖 = 陣列[共用.行1:共用.行2, 共用.列1:共用.列2]
    
    
def 按下(按鍵):
    if 按鍵 == 'w':
        print('揮動魔杖')
        共用.切換(召喚狀態2)
        
            
    
def 離開():
    print('離開 鏡子狀態1')    
    #共用.鏡面.淡出(持續=1.5)
    
    共用.鏡面.有效狀態 = False
    



