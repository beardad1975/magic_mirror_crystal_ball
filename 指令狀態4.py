from 語音模組 import *


import 共用
import 鏡子狀態1 
import 召喚狀態2 
import 登場狀態3 
import 指令狀態4 
import 特效狀態5  
import 導覽狀態6 

def 進入():
    print('進入 指令狀態4')
    共用.魔鏡角色.有效狀態 = True
    共用.火焰.有效狀態 = True
    設定語音速度(-2)
    語音合成('我是哈哈魔鏡', 等待=False)
    
    

def 更新():
    pass
    
    
    
def 按下(按鍵):
    pass
    
        
      
    
    
def 離開():
    print('離開 指令狀態4')
    共用.火焰.有效狀態 = False
    共用.魔鏡角色.有效狀態 = False

