import time as 時間


import 共用
import 登場動畫 # 3
import 休眠 # 1

def 進入():
    print('進入 準備召喚2')
    共用.進入時間 = 時間.time()
    
    

def 更新():
    pass
    #print('準備召喚 更新')
    經過時間 = 時間.time() - 共用.進入時間
    
    if 經過時間 > 共用.準備召喚限制秒數:
        print('超過時間')
        離開()
        共用.目前狀態 = 1
        休眠.進入()
    
def 按下(按鍵):
    if 按鍵 == '3':
        離開()         
        共用.目前狀態 = 3
        登場動畫.進入() 
      
    
    
def 離開():
    print('離開 準備召喚2')