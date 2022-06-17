import Drink
import Suggestions
from src import Token
import Utilities
import discord
from discord.utils import get


intents = discord.Intents.default()
# noinspection PyUnresolvedReferences, PyDunderSlots
intents.message_content = True
intents.reactions = True

test_server = {
    'id': 583862568049967164,
}
nook_and_cranny = {
    'id': 773225381331206156,
    'channels': {
        'general': 773225381331206159,
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


@bot.slash_command(name='drink', description='Barkeep will recommend you a drink', guild_ids=server_ids)
async def get_drink(ctx):
    drink = Drink.get_drink()
    await ctx.respond(f'Might I suggest {drink.article} {drink.name}?')


@bot.slash_command(description='Make a suggestion to improve the bot', guild_ids=server_ids)
async def suggest(ctx, suggestion: str):
    Suggestions.add_suggestion(Utilities.sanitise(suggestion))
    await ctx.respond("I'll take a note of that.")


@bot.event
async def on_raw_reaction_add(event):
    if event.emoji.name != '⭐':
        return
    channel = bot.get_channel(event.channel_id)
    message = await channel.fetch_message(event.message_id)
    reaction = get(message.reactions, emoji=event.emoji.name)
    if reaction.count == 3:
        guild_name = bot.get_guild(event.guild_id).name
        hall_of_fame = get(bot.get_all_channels(), guild__name=guild_name, name='hall-of-fame')
        await hall_of_fame.send(message.content + '\n' + message.jump_url)


bot.run(Token.get_token())
