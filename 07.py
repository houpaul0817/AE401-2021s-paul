# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:20:51 2021

@author: 柏均
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
for i in range(100):
    for e in range(3):
        mc.setBlock(x+i+e,y-1,z+i,164)
        
plantTree(x,y,z)
    mc.setBlock(x+i,y-1,z+i,276)
    mc.setBlock(x+i+1,y-1,z+i,276)
    mc.setBlock(x+i+2,y-1,z+i,276)
    
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+1,y+6,z+1,x-1,y+4,z-1,20)
mc.setBlocks(x,y+1,z,x,y+5,z,17)

