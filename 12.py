# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:04:12 2021

@author: 柏均
"""

from mcpi.minecraft import minecraft
mc=Minecraft.create()

from random import choice

mineral=[14,15,16,56,73,129]

r=choice(mineral)

myID=mc.getPlayerEntityID("你的麥塊ID")
x,y,z=mc.entity.getTilepos(myID)

mc.setBlock(x,y,z,r)
