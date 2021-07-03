# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:37:42 2021

@author: 柏均
"""

a="axsaxsaxsaxsaxsaxsaxsaxsaxs"
from mcpi.minecraft import minecraft
mc=Minecraft.create()
print(a[:10])
while True :
    chat=mc.events.pollChatposts()
    if len(chat)>0:
        strach=chat[0]
         comma1= strachat.find(",")
         comma2= strachat.find(",", comma 1+1
         senderID=int(strchat[comma1+1:comma2])
         message=strchat[comma2+1+1:len(strchat)-1]
         name=mc.entity.getname(senderID)
         x,y,z=mc.entity.getTilePos(senderID)
         mc.setSing(x,y,z,63,0,name,"",message)
           