# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:51:57 2021

@author: 柏均
"""
from mcpi.minecraft import minecraft
import time

mc=minecraft.create()

def builPyramid(x,y,z,base=10):
    height=base//2+1
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        
        x2=x+base-i
        z2=z+base-i
        mc.setblocks(x1,y1,z1,x2,y1,z2,56)     
        
        

x, y, z = mc.player.getTilePos()
buildPyramid(x, y, z, 8)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
fori in range(1,10)
list1.append(1*1)
fori in range(1,10)
list2.append(2*1)        
        
        
        
        

fori in range(1,10):
list3.append(3*1)       
        
        
        
        
        
        
        
        
        
        
 number=1       
 for i inrang(8):
     for u inrang(number):
         mc.spawnEntity(x,y,z,33)
number=number*2
mc. posTochat(str(number)+"隻")
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        