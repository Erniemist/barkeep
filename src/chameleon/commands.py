import json
import random
from typing import Optional

import discord
from discord.abc import Messageable


async def see_wordsets(interaction: discord.Interaction):
    with open("wordsets.txt", "r", encoding="utf-8") as f:
        wordsets = json.load(f)
    if len(wordsets) == 0:
        await send_message(interaction.channel, "No wordsets")
    else:
        await send_message(
            interaction.channel,
            "\n".join(
                f"{set_code}: {', '.join(words)}"
                for set_code, words in wordsets.items()
            ),
        )


async def update_wordsets(interaction: discord.Interaction, set_code: str, words: str):
    with open("wordsets.txt", "r", encoding="utf-8") as f:
        wordsets = json.load(f)

    wordsets[set_code] = words.split(", ")

    with open("wordsets.txt", "w", encoding="utf-8") as f:
        json.dump(wordsets, f)
    await send_message(interaction.channel, f"Added {set_code}")


async def start_game(
    interaction: discord.Interaction,
    set_code: str,
    client_id: int,
    *members: Optional[discord.Member],
):
    with open("wordsets.txt", "r", encoding="utf-8") as f:
        wordsets = json.load(f)
    if set_code not in wordsets.keys():
        await interaction.response.send_message(f"Set {set_code} not found")
        return

    try:
        words = wordsets[set_code]
    except KeyError as e:
        await send_message(interaction.channel, repr(e))

    valid_members = [
        member for member in members if member is not None and member.id != client_id
    ]
    random.shuffle(valid_members)
    turn_order_display = str.join(
        "\n", [f"{i + 1}: {member.mention}" for i, member in enumerate(valid_members)]
    )
    await interaction.response.send_message(
        f"Words are {', '.join(words)}" + "\nTurn order:\n" + turn_order_display
    )

    word = random.choice(words)
    random.shuffle(valid_members)
    await valid_members[0].send("You are the chameleon")
    for member in valid_members[1:]:
        await member.send(f"The word is {word}")


async def send_message(channel, message: str):
    if not isinstance(channel, Messageable):
        raise ValueError("Command sent in a voice channel or something???")
    await channel.send(message)
