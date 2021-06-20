# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:50:15 2021

@author: 柏均
"""


x,y,z = mc.player.getTilePos()    
mc.setBlocks(x+4,y+4,z+4,x+10,y+10,z+10,46) 
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,0)  
mc.setBlocks(x-4,y-4,z-4,x-10,y-10,z-10,20) 
mc.setBlocks(x-4,y-1,z-1,x-12,y-9,z-9,0) 
mc.setBlocks(x-4,y-4,z-4,x-10,y-10,z-10,46) 
mc.setBlocks(x-4,y-1,z-1,x-12,y-9,z-9,0)
mc.setBlocks(x+4,y+4,z+4,x+10,y+10,z+10,20) 
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,0)  
mc.setBlocks(x-4,y-4,z-4,x-10,y-10,z-10,46) 
mc.setBlocks(x-4,y-1,z-1,x-12,y-9,z-9,0)