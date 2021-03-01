import time as 時間

import 共用
import 鏡子狀態1 
import 召喚狀態2 
import 登場狀態3 
import 指令狀態4 
import 特效狀態5  
import 導覽狀態6 

def 進入():
    print('進入 指令狀態4')
    共用.進入時間 = 時間.time()

def 更新():
    pass
    #print('等待指令 更新')
    經過時間 = 時間.time() - 共用.進入時間
    
    if 經過時間 > 共用.等待指令限制秒數:
        print('無指令太久了')
        共用.切換(鏡子狀態1)
    
def 按下(按鍵):
    pass
        
      
    
    
def 離開():
    print('離開 指令狀態4')
    

