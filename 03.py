# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:40:33 2021

@author: 柏均
"""

from mcpi.minecraft import Minecraft
import time
mc= Minecraft.create()




x,y,z = mc.player.getTilePos()
time.sleep(6)
mc.setBlock(x,y,z,8)
time.sleep(6)
mc.setBlock(x+5,y,z,8)
time.sleep(6)
mc.setBlock(x,y,z+5,8)



x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+10,y,z+10,209)



x,y,z = mc.player.getTilePos()
mc.setBlocks(x-5, y-1, z-5,x+5,y+1,z+5,167)



    
x,y,z = mc.player.getTilePos()    
mc.setBlocks(x+3,y,z,x+13,y+10,z+10,152)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,0)     


