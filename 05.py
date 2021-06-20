# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:02:44 2021

@author: 柏均
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

try:
    x, y, z = mc.player.getTilePos()
    blockType = int(input("請輸入ID:"))
    mc.setBlock(x, y, z, blockType)
except:
    print("bibibi")

x, y, z = mc.player.getTilePos()

mc.setBlocks(x+3, y ,z, x+13, y+10, z+10, 1)
mc.setBlocks(x+4, y+1 ,z+1, x+12, y+9, z+9, 0)



x, y, z = mc.player.getTilePos()

hight = int(input("請輸入多高："))
length = int(input("請輸入多長："))
width = int(input("請輸入多寬："))
blockID = int(input("請輸入ID："))

mc.setBlocks(x, y+1, z, x+length-1, y+hight, z+width-1, blockID)
mc.setBlocks(x+1, y+2, z+1, x+length-2, y+hight-1, z+width-2, 0)
mc.setBlocks(x+2, y+2, z, x+2, y+3, z, 0)


