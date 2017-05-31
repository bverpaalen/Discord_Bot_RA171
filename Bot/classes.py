class bot:
    def __init__(self,client):
        self.client = client
        self.channels = ["divinity"]

    async def say(self,channel,text):
         await self.client.send_message(channel,text)

    def getServers(self):
        allServers = ""
        for server in client.servers:
            allServers += ","+server.name
        allServers = allServers[1:]
        return allServers

    def setChannels(self,channels):
        self.channels = channels

    def addChannels(self,channels):
        for channel in channels:
            self.channels.append(channel)

    def getChannels(self):
        return self.channels

    def getUser(self):
        return client.user
