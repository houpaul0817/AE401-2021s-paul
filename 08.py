from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x+1,y+6,z+1,x-1,y+4,z-1,20)
    mc.setBlocks(x,y+1,z,x,y+5,z,17)
    
x,y,z=mc.player.getTilePos()
plantTree(x,y,z)

x,y,z=mc.player.getTilePos()
for i in range(10):
    plantTree(x+i*5,y,z)
    
x,y,z=mc.player.getTilePos()
for i in range(0, 46, 5):
    plantTree(x+i,y,z)


x,y,z=mc.player.getTilePos()
for i in range(10):
    for h in range(10):
        plantTree(x+i*5,y,z+h*5)
        
x,y,z=mc.player.getTilePos()
for i in range(10):
    for h in range(10):
        plantTree(x+i*5,y+h*5,z)
        
        
        
x,y,z=mc.player.getTilePos()
for i in range(10):
    for h in range(5):
        plantTree(x+i*5,y+i*h,z)
        
x,y,z=mc.player.getTilePos()
for i in range(10):
    for h in range(5):
        for y in range(5):
            plantTree(x+i*5,y+i*h,z+i*y)