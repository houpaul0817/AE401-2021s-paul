
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())

x = 116
y = 180 
z = 82
mc.player.setTilePos(x,y,z)
outpoc
