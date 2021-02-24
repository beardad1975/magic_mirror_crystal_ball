import time as 時間


import 共用
import 休眠 # 1
import 等待指令 # 4

def 進入():
    print('進入 登場動畫3')
    共用.進入時間 = 時間.time()

def 更新():
    pass
    #print('準備召喚 更新')
    經過時間 = 時間.time() - 共用.進入時間
    
    if 經過時間 > 共用.登場動畫秒數:
        print('動畫結束')
        離開()
        共用.目前狀態 = 4
        等待指令.進入()
    
def 按下(按鍵):
    pass
        
      
    
    
def 離開():
    print('離開 登場動畫3')