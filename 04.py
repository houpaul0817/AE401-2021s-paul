from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while ture
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