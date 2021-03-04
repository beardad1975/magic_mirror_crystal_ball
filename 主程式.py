from 模擬3D模組 import *
from 視覺模組 import *
from 語音模組 import *



import 共用
import 鏡子狀態1 
import 召喚狀態2 
import 登場狀態3 
import 指令狀態4 
import 特效狀態5  
import 導覽狀態6 

from 初始 import 初始設定

初始設定()

def 當更新時(時間差):
    共用.目前狀態.更新()

def 當按下時(按鍵):


    共用.目前狀態.按下(按鍵)
    
    # for test
    if 按鍵 == '1':
        共用.切換(鏡子狀態1)
    elif 按鍵 == '2':
        共用.切換(召喚狀態2)
    elif 按鍵 == '3':
        共用.切換(登場狀態3)
    elif 按鍵 == '4':
        共用.切換(指令狀態4)
    elif 按鍵 == '5':
        共用.切換(特效狀態5)
    elif 按鍵 == '6':
        共用.切換(導覽狀態6)
    elif 按鍵 == 'space':
        共用.舞台.全螢幕 = not 共用.舞台.全螢幕
        

模擬主迴圈()
