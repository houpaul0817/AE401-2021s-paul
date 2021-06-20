# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:43:37 2021

@author: 柏均
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc,player,getTilePos())
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
x, y, z = mc.player.getTilePos()

a = getBlock(x, y-1, z)
b = getBlock(x, y-1, z-1)
c = getBlock(x+1, y-1, z)
d = getBlock(x, y-1, z+1)
if a==8 or a==9 orb==8 or b==9 or c==8 or c==9:
    mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,46)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
a=0
while a<20:
    mc.setBlocks(x+30,y-1,z,x-30,y-10,z,19)
    z=z-5
    a=a+1
    
import time
while true:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y,z,19)
    time.sleep(10)
    # -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:02:44 2021

@author: 柏均
"""

rom mcpi.minecraft import Minecraft
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
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:02:44 2021

@author: 柏均


rom mcpi.minecraft import Minecraft
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
mc.setBlocks(x-5, y-1, z-5,x+5,y+1,z+5,46)



    
x,y,z = mc.player.getTilePos()    
mc.setBlocks(x+3,y,z,x+13,y+10,z+10,46)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,0)     
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
x, y, z = mc.player.getTilePos()

a = getBlock(x, y-1, z)
b = getBlock(x, y-1, z-1)
c = getBlock(x+1, y-1, z)
d = getBlock(x, y-1, z+1)
if a==8 or a==9 orb==8 or b==9 or c==8 or c==9:
    mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,46)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
a=0
while a<20:
    mc.setBlocks(x+30,y-1,z,x-30,y-10,z,19)
    z=z-5
    a=a+1
    
import time
while true:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y,z,19)
    time.sleep(10)
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
    # -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 08:04:58 2021

@author: 柏均
"""
from mcpi.minecraft import Minecraft
import time
mc= Minecraft.create()
    
x,y,z = mc.player.getTilePos()    
mc.setBlocks(x+3,y,z,x+13,y+10,z+10,265)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,0)  
mc.setBlocks(x+2,y,z-1,x+12,y+11,z+11,265)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,0)  
from mcpi.minecraft import  Minecraft
import time
mc= Minecraft.create()