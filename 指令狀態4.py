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
    
    
    共用.指令動畫.開始()
    
    #設定語音速度(-2)
    
    
    
    

def 更新():
    if 共用.指令動畫.結束了嗎:
        if 辨識成功了嗎():
            文字 = 取得辨識文字()
            
            if '世界'  in 文字 and '可怕' in 文字 :
                共用.進入特效動畫.開始()
                
            elif '學校'  in 文字 and '自由' in 文字 :
                共用.進入導覽動畫.開始()
        
            
    
    
    
    
def 按下(按鍵):
    pass
    
        
      
    
    
def 離開():
    print('離開 指令狀態4')
    共用.火焰.有效狀態 = False
    共用.魔鏡角色.有效狀態 = False
    共用.命令文字.有效狀態 = False
    共用.煙霧.有效狀態 = False
    暫停語音辨識()
    
