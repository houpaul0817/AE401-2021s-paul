# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:26:02 2021

@author: 柏均
"""

from mcpi.minecraft import Minecraft
import time
mc= Minecraft.create()

pos=mc.player.getTlePos()
while True:
    x=pos.x +　random.uniform(20,-20)
    z=pos.z　+random.uniform(20,-20)
    y=pos.y + 50
    mc.spawnEntity(x,y,z,50)
    time.sleep (0.1)
while True: 
    hits=mc.events.pollprojectilehits()
    if(len(hits)>0)
    hit=hits[0]
    x,y,z=hit.pos.x.hit.pos.y.hit.pos.z
    mc.createExplosion(x,y,z)
    
    