import time as 時間
from 模擬3D模組 import *

import 共用
import 鏡子狀態1 
import 召喚狀態2 
import 登場狀態3 
import 指令狀態4 
import 特效狀態5  
import 導覽狀態6 

def 進入():
    print('進入 登場狀態3')
    
    共用.動畫完成嗎 = False
    共用.登場動畫.開始()
    

def 更新():
    if 共用.登場動畫.結束了嗎:
        共用.切換(指令狀態4)
    
    
    
def 按下(按鍵):
    pass
        
   
def 離開():
    print('離開 登場狀態3')
    共用.魔鏡角色.有效狀態 = False
    共用.火焰.有效狀態 = False

    