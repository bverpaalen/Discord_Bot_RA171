#!/usr/bin/env python3
import discord
import logging
import asyncio
import time
from datetime import datetime

from classes import bot
import divinity
import config

logging.basicConfig(level=logging.INFO)
client = discord.Client()
bot = bot(client)
@client.event
async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print('-------')

@client.event
async def on_message(discordInput):
    message = discordInput.content
    channel = discordInput.channel
    commands = message.split(" ")[1:]
    text = ""
    print("Message recieved: "+message)
    if message.startswith("!divinity"):
        item = commands[0]
        if len(commands) > 1:
            hits = commands[1]
        else:
            hits = 1
        text = divinity.getItemUrl(item,hits)
    
    while(text==""):
        time.sleep(10)
    await bot.say(channel,text)
        

def getCurrentTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

client.run(config.app['token'])
