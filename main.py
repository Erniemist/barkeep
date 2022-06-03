from discord import Client, Intents, Member

intents = Intents.default()
intents.members = True


class MyClient(Client):
    general_channel = 773225381331206159

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_remove(self, member: Member):
        if 'spotts' in member.name.lower():
            await self.get_channel(MyClient.general_channel).send('Not again!')


client = MyClient(intents=intents)

with open('token.txt', 'r') as token_file:
    token = token_file.readline().strip()
client.run(token)
