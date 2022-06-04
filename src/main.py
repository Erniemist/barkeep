import Drink
import Suggestions
from src import Token
import Utilities
import discord

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


@bot.slash_command(description='Says hello', guild_ids=server_ids)
async def hello(ctx):
    await ctx.respond("Hello World.")


@bot.slash_command(description='Barkeep will recommend you a drink', guild_ids=server_ids)
async def drink(ctx):
    article, drink_name = Drink.get_drink()
    await ctx.respond(f'Might I suggest {article} {drink_name}?')


@bot.slash_command(description='Make a suggestion to improve the bot', guild_ids=server_ids)
async def suggest(ctx, suggestion: str):
    Suggestions.add_suggestion(Utilities.sanitise(suggestion))
    await ctx.respond("I'll take a note of that.")


bot.run(Token.get_token())
