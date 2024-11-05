import json
import random
from typing import Optional

import discord

from src import utilities, suggestions
from src.avalon import proposal_view
from src.avalon.game import load_players, display_turn_order
from src.avalon.start_game_view import StartGameView
from src.config import DISCORD_TOKEN, AVALON_ENABLED
from src.discord.client.client import Client
from src.drink import get_drink_repository

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
async def drink(interaction: discord.Interaction):
    """Barkeep will recommend you a drink"""
    await interaction.response.send_message(
        f"Might I suggest {get_drink_repository().get_drink()}?",
    )


@client.tree.command()
async def see_chameleon_wordsets(interaction: discord.Interaction):
    """List current chameleon wordsets"""
    with open('wordsets.txt', 'r') as f:
        wordsets = json.load(f)
    if len(wordsets) == 0:
        await interaction.channel.send("No wordsets")
    else:
        await interaction.channel.send('\n'.join(f"{set_code}: {', '.join(words)}" for set_code, words in wordsets.items()))


@client.tree.command()
async def update_chameleon_wordsets(interaction: discord.Interaction, set_code: str, words: str):
    """Add a chameleon wordset"""
    try:
        await add_wordset(set_code, words)
        await interaction.channel.send(f"Added {set_code}")
    except Exception as e:
        await interaction.channel.send(f"Failed to add {set_code}: {repr(e)}")


async def add_wordset(set_code: str, words: str):
    with open('wordsets.txt', 'r') as f:
        wordsets = json.load(f)

    wordsets[set_code] = words.split(', ')

    with open('wordsets.txt', 'w') as f:
        json.dump(wordsets, f)


@client.tree.command()
async def play_chameleon(
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
    with open('wordsets.txt', 'r') as f:
        wordsets = json.load(f)
    if set_code not in wordsets.keys():
        await interaction.response.send_message(f"Set {set_code} not found")
        return

    words = wordsets[set_code]

    members = [
        member
        for member in [member1, member2, member3, member4, member5, member6, member7, member8]
        if member is not None and member.id != client.user.id
    ]
    random.shuffle(members)
    turn_order_display = str.join("\n", [f"{i + 1}: {member.mention}" for i, member in enumerate(members)])
    await interaction.response.send_message(f"Words are {', '.join(words)}" + "\nTurn order:\n" + turn_order_display)

    word = random.choice(words)
    random.shuffle(members)
    await members[0].send("You are the chameleon")
    for member in members[1:]:
        await member.send(f"The word is {word}")


@client.tree.command()
async def suggest(interaction: discord.Interaction, suggestion: str):
    """Make a suggestion to improve the bot"""
    suggestions.add_suggestion(utilities.sanitise(suggestion))
    await interaction.response.send_message("I'll take a note of that.")


if AVALON_ENABLED:
    @client.tree.command()
    async def start_game(interaction: discord.Interaction):
        """Start a game of avalon"""
        await interaction.response.send_message(
            "",
            view=StartGameView(),
            embed=discord.Embed(
                title="Roles",
                description="No roles selected",
                color=discord.Color.light_embed(),
            ),
        )

    @client.tree.command()
    async def propose_quest(interaction: discord.Interaction):
        """Propose a quest"""
        view = await proposal_view.make(interaction.client)
        await interaction.response.send_message(view=view)

    @client.tree.command()
    async def check_turn_order(interaction: discord.Interaction):
        """Check the turn order. Unaware of next quest sender"""
        players = await load_players(interaction.client)
        await display_turn_order(interaction, players)


client.run(DISCORD_TOKEN)
