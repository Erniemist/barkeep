import discord
import Drink

intents = discord.Intents.default()
intents.message_content = True

test_server_id = 583862568049967164
server_id = 773225381331206156
general_channel = 773225381331206159


bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


@bot.event
async def on_member_remove(member):
    if 'spotts' in member.name.lower():
        await bot.get_channel(general_channel).send('Not again!')


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(guild_ids=[test_server_id, server_id])
async def hello(ctx):
    await ctx.respond("Hello World.")


@bot.slash_command(guild_ids=[test_server_id, server_id])
async def drink(ctx):
    await ctx.respond(f'Might I suggest a {Drink.get_drink()}?')


with open('token.txt', 'r') as token_file:
    token = token_file.readline().strip()

bot.run(token)
