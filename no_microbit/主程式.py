from 模擬3D模組 import *
from 視覺模組 import *
from 語音模組 import *
import 共用
import 鏡子狀態1
import 魔鏡狀態2
import 立體狀態3
import 視覺特效狀態4
import 水晶球狀態5

from 初始 import 初始設定

初始設定()

def 當更新時(時間差):
    共用.目前狀態.更新()

def 當按下時(按鍵):
    if 按鍵 == '1':
        共用.切換(鏡子狀態1)
    elif 按鍵 == '2':
        共用.切換(魔鏡狀態2)
    elif 按鍵 == '3':
        共用.切換(立體狀態3)
    elif 按鍵 == '4':
        共用.切換(視覺特效狀態4)
    elif 按鍵 == '5':
        共用.切換(水晶球狀態5)
    
模擬主迴圈()
