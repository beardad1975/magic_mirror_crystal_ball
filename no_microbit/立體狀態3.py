from 語音模組 import *
from 模擬3D模組 import *
import 共用
import 鏡子狀態1
import 魔鏡狀態2
import 立體狀態3
import 視覺特效狀態4
import 水晶球狀態5

def 進入():
    print('進入 立體狀態3')
    共用.立體動畫.開始()

def 更新():
    共用.愛心.旋轉y += 2
    
    if 辨識成功了嗎():
        文字 = 取得辨識文字()
        if '魔鏡' in 文字  :
            共用.切換(魔鏡狀態2 )                         
             
    
def 離開():
    print('離開 立體狀態3')
    共用.立體動畫.結束()
    共用.舞台.背景顏色 = color.black
    共用.愛心.有效狀態 = False
    共用.美麗文字.有效狀態 = False
    暫停語音辨識()
    
    
