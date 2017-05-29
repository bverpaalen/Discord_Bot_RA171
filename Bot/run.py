#!/usr/bin/env python3
import discord
import asyncio
import config
import logging
from datetime import datetime
import time

logging.basicConfig(level=logging.INFO)
client = discord.Client()


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
    print("Message recieved: "+message)
    if message.startswith("!time"):
            currentTime = getCurrentTime()
            landingTime = 1502031600
            difference = landingTime - int(time.time())
            print("Sending time")
            await client.send_message(channel,"System time: "+str(currentTime))
            await client.send_message(channel,"Brent will be back in: "+str(difference))    
    elif message.startswith("!discVersion"):
        await client.send_message(channel,"Library version: "+discord.__version__)
    elif message.startswith("!allServers"):
        allServers = ""
        for server in client.servers:
            allServers += ","+server.name
            allServers = allServers[1:]
        await client.send_message(channel,"Running on: "+allServers)
    elif message.startswith("!test"):
        print(client.user)
        print(client.email)
        client.change_status("Drinking beer")


def getCurrentTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

client.run(config.app['token'])
