# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:52:54 2021

@author: 柏均
"""


from mcpi.minecraft import minecraft 
from time import sleep
import random
mc=minecraft.create()
x,y,z=mc.player.getTilePos()

for i in range(20):
    r= random.randrange(1,5)
    
    if r==1:
        mc.setblocks(x,y,z,x+4,y,z,46)
        x+=4
    elif r==2:
        mc.setblocks(x,y,z,x-4,y,z,46)
        x-=4
    elif r==3:
        mc.setblocks(x,y,z,x,y,z+4,46)
        z+=4
    elif r==2:
        mc.setblocks(x,y,z,x,y,z-4,46)
        z-=4
while True:
    mc.executecommant('time add 50')
    sleep(0.1)
        
                   
   
