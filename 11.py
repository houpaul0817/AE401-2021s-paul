from mcpi.minecraft import Minecraft
from time import sleep
import random
mc=Minecraft.create()

x,y,z=mc.player.getTilePos

for i in range(10):
    r=random.randrange(1,5)
    
    if r ==1:
    mc.setBlocks(x,y,z,x+4,y,z,57)
    x+=4
    if r ==2:
    mc.setBlocks(x,y,z,x-4,y,z,57)
    x-=4
    if r ==3:
         mc.setBlocks(x,y,z,x,y,z+4,57)
         z+=4
    if r ==4:
         mc.setBlocks(x,y,z,x,y,z-4,57)
         z-=4
         
     x,y,z=mc.player.getTilePos()
     x=x+i
     for j in range(10):
          r=randrange(0,16)
          z=z+1
          mc.setBlock(x,y,z,35,r)
        
from random import randrange

r= randrange(1,16)
while True:
    hits=mc.events.pollBlockHits()#傾聽事件
    if len(hits)>0:
         hit=hits[0] 
         
         block=mc.getBlockWithData(hit.pos)
         data=block.data
         elif data<r:
             mc.postToChat("試試看更大地id8")
         elif datar>:
             mc.postToChat("試試看更地id8") 
         if date==r:
             mc.postToChat("恭喜>///<")
             mc.setBlocks(hit.pos,56)
             break
    
    
    