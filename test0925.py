# from mcpi.minecraft import Minecraft
# import time
# mc = Minecraft.create()

# while 1+1==2:
#     mc.setBlock(-236,77,238,46)
#     time.sleep(0.1)

score = int(input("score: "))
if score >= 90:
    print('Grade is: A')
elif score >= 80:
    print('Grade is: B')
elif score >= 70:
    print('Grade is: C')
elif score >= 60:
    print('Grade is: D')
else:
    print('Grade is: F')
