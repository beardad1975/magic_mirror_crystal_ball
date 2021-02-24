import time as 時間

import 共用
import 等待指令 # 4


def 進入():
    print('進入 校園導覽6')
    共用.進入時間 = 時間.time()

def 更新():
    pass
    #print('校園導覽 更新')
    經過時間 = 時間.time() - 共用.進入時間
    
    if 經過時間 > 共用.校園導覽秒數:
        print('校園導覽結束')
        離開()
        共用.目前狀態 = 4
        等待指令.進入()
    
def 按下(按鍵):
    pass
        
      
    
    
def 離開():
    print('離開 校園導覽6')