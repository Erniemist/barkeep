from discord import app_commands

import Drink
import Suggestions
from src import Token
import Utilities
import discord
from discord.ext.commands import Bot
from discord.utils import get


test_server = {
    'id': 583862568049967164,
}
nook_and_cranny = {
    'id': 773225381331206156,
    'channels': {
        'general': 773225381331206159,
    },
}


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        for guild_id in (test_server['id'], nook_and_cranny['id']):
            guild = discord.Object(id=guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)


client = MyClient(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
async def drink(interaction: discord.Interaction):
    """Barkeep will recommend you a drink"""
    chosen_drink = Drink.get_drink()
    await interaction.response.send_message(f'Might I suggest {chosen_drink.article} {chosen_drink.name}?')


@client.tree.command()
async def suggest(interaction: discord.Interaction, suggestion: str):
    """Make a suggestion to improve the bot"""
    Suggestions.add_suggestion(Utilities.sanitise(suggestion))
    await interaction.response.send_message("I'll take a note of that.")


client.run(Token.get_token())
