import time as 時間
from 模擬3D模組 import *
from 語音模組 import *

import 共用
import 鏡子狀態1 
import 召喚狀態2 
import 登場狀態3 
import 指令狀態4 
import 特效狀態5  
import 導覽狀態6 


def 進入():
    print('進入 導覽狀態6')
    
    共用.水晶球.有效狀態 = True
    共用.水晶球.材質貼圖 = '圖片/操場360.jpg'
    共用.水晶球玻璃.有效狀態 = True
    共用.導覽文字.有效狀態 = True
    
    語音合成(共用.操場導覽內容, 等待=False)
    


def 更新():
    共用.水晶球.旋轉y += 0.2
    if 語音說完了嗎():
        共用.切換(指令狀態4 )
    

    
def 按下(按鍵):
    pass
            
    
def 離開():
    print('離開 導覽狀態6')
    共用.水晶球.有效狀態 = False
    共用.水晶球玻璃.有效狀態 = False
    共用.導覽文字.有效狀態 = False
