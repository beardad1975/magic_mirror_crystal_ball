from 模擬3D模組 import *
from 視覺模組 import *
from 語音模組 import *
import 共用
import 鏡子狀態1
import 魔鏡狀態2
import 立體狀態3
import 視覺特效狀態4
import 水晶球狀態5


def 進入():
    print('進入 鏡子狀態1')
    共用.鏡子動畫.開始()
    

def 更新():
    陣列 = 擷取單張影像(共用.攝影機)
    共用.鏡子.多維陣列貼圖 = 陣列[共用.行1:共用.行2, 共用.列1:共用.列2]
    
    if 辨識成功了嗎():        
        文字 = 取得辨識文字()
        if '魔鏡' in 文字 :
            共用.切換(魔鏡狀態2)  
    
def 離開():
    print('離開 鏡子狀態1')
    共用.鏡子動畫.結束()
    共用.鏡子.有效狀態 = False
    共用.鏡子文字.有效狀態 = False
    暫停語音辨識()
