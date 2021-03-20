"""
Created on Sat Mar 20 10:44:18 2021

@author: 柏均
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
x=247.666
y=99.0
z=777.88
mc.player.setPos(x,y,z)








x,y,z = mc.player.getTilePos()

import time
while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("you are located at" + str(x) + ", " + str(y) + ", " + str(z))
    time.sleep(0.5)