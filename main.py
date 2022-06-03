import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id != self.user.id:
            await message.channel.send(f'{message.author} said {message.content}')


client = MyClient()

with open('token.txt', 'r') as token_file:
    token = token_file.readline().strip()
client.run(token)
