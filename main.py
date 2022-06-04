import discord, Drink, Suggestions

intents = discord.Intents.default()
intents.message_content = True

test_server = {'id': 583862568049967164}
nook_and_cranny = {
    'id': 773225381331206156,
    'channels': {
        'general': 773225381331206159
    },
}

server_ids = [test_server['id'], nook_and_cranny['id']]

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


@bot.event
async def on_member_remove(member):
    if 'spotts' in member.name.lower():
        await bot.get_channel(nook_and_cranny['channels']['general']).send('Not again!')


@bot.event
async def on_ready():
    print(f"{bot.user} at your service")


@bot.slash_command(guild_ids=server_ids)
async def hello(ctx):
    await ctx.respond("Hello World.")


@bot.slash_command(guild_ids=server_ids)
async def drink(ctx):
    await ctx.respond(f'Might I suggest a {Drink.get_drink()}?')


@bot.slash_command(guild_ids=server_ids)
async def suggest(ctx, suggestion: str):
    safe_chars = 'abcdefghijklmnopqrstuvwxyz '
    Suggestions.add_suggestion(str.join('', [char for char in suggestion.lower() if char in safe_chars]))
    await ctx.respond("I'll take a note of that.")


with open('token.txt', 'r') as token_file:
    token = token_file.readline().strip()

bot.run(token)
