# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:51:04 2021

@author: 柏均
"""

from mcpi.minecraft import minecraft
mc=Minecraft.create()

while True:
    chat=mc.events.pollChatposts()
   if len (chat)>0:
       strchat=str(chat[0])
       comma1=strchat.find(",")
       