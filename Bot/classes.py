class bot:
    def __init__(self,client):
        self.client = client

    async def say(self,channel,text):
         await self.client.send_message(channel,text)

    def getServers(self):
        allServers = ""
        for server in client.servers:
            allServers += ","+server.name
        allServers = allServers[1:]
        return allServers

    def getUser(self):
        return client.user
