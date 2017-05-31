import divinity as div

def selectFlow(message,channel,commands,bot):
    text = ""
    if message.startswith("!divinity"):
        item = commands[0]
        if len(commands) > 1:
            hits = commands[1]
        else:
            hits = 1
        text = div.QueryUrl(item,hits)
    elif message.startswith("!channel"):
        command = commands[0]
        if command.lower() == "add":
            bot.addChannels(commands[1:])
    return text
