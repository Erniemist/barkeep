from typing import Optional
import discord
import src.avalon.commands as avalon_commands
import src.chameleon.commands as chameleon_commands
from src.config import DISCORD_TOKEN, AVALON_ENABLED
from src.discord.client.client import Client

client = Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")


@client.tree.command()
async def chameleon_see_wordsets(interaction: discord.Interaction):
    """List current chameleon wordsets"""
    await chameleon_commands.see_wordsets(interaction)


@client.tree.command()
async def chameleon_update_wordsets(
    interaction: discord.Interaction, set_code: str, words: str
):
    """Add a chameleon wordset"""
    await chameleon_commands.update_wordsets(interaction, set_code, words)


@client.tree.command()
async def chameleon_start_game(
    interaction: discord.Interaction,
    set_code: str,
    member1: discord.Member,
    member2: Optional[discord.Member],
    member3: Optional[discord.Member],
    member4: Optional[discord.Member],
    member5: Optional[discord.Member],
    member6: Optional[discord.Member],
    member7: Optional[discord.Member],
    member8: Optional[discord.Member],
):
    """Play a game of chameleon!"""
    await chameleon_commands.start_game(
        interaction,
        set_code,
        client.user.id if client.user is not None else 0,
        member1,
        member2,
        member3,
        member4,
        member5,
        member6,
        member7,
        member8,
    )


if AVALON_ENABLED:

    @client.tree.command()
    async def avalon_start_game(interaction: discord.Interaction):
        """Start a game of avalon"""
        await avalon_commands.avalon_start_game(interaction)

    @client.tree.command()
    async def avalon_propose_quest(interaction: discord.Interaction):
        """Propose a quest"""
        await avalon_commands.avalon_propose_quest(interaction)

    @client.tree.command()
    async def avalon_check_turn_order(interaction: discord.Interaction):
        """Check the turn order. Unaware of next quest sender"""
        await avalon_commands.avalon_check_turn_order(interaction)


client.run(DISCORD_TOKEN)
