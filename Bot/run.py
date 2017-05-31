#!/usr/bin/env python3
import discord
import logging
import asyncio
import time
from datetime import datetime

from classes import bot
import selector
import tools
import config

logging.basicConfig(level=logging.INFO)
client = discord.Client()
robin = bot(client)

@client.event
async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print('-------')

@client.event
async def on_message(discordInput):
    channel = discordInput.channel
    allowedChannels = robin.getChannels()
    if tools.stringInList(channel,allowedChannels):
        message = discordInput.content
        print("Message recieved: "+message)
        commands = message.split(" ")[1:]
        text = selector.selectFlow(message,channel,commands,robin)
        await submitText(channel,text)

async def submitText(channel,text):
    if text != "" and text != []:
        textType = type(text)
        if textType == str:
            await robin.say(channel,text)
            print(text)
        elif textType == list:
            listOfText = text
            for text in listOfText:
                print(text)
                await robin.say(channel,text)

def getCurrentTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

client.run(config.app['Token'])
