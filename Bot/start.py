#!/usr/bin/env python3
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print('-------')

@client.event
async def on_message(message)
    if message.content.startswith("!test")
        print("Test complete")

client,run('token')
