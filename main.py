token = input("Token > ")

import discord
from discord import *
from discord.ext import commands

default_intents = discord.Intents.default()
default_intents.members = True
client = commands.Bot(command_prefix="//",
                      help_command=None,
                      intents=default_intents)

@client.event
async def on_ready():
    print("[ OK ] Bot ready")
    print("----- INFO -----")
    print("    Name:", client.user.name)
    print("    ID:", client.user.id)
    try:
        print("    Avatar:", client.user.avatar.url)
    except:
        print("    Avatar: None")
    for guild in client.guilds:
        print("----- SERVER -----")
        print("    Name:", guild.name)
        print("    ID:", guild.id)
        try:
            print("    Avatar", guild.icon.url)
        except:
            print("    Avatar: None")
        print("    Channel(s):")
        for ch in guild.channels:
            print(" "*8 + "-"*10)
            print(" "*8 + "Name:", ch.name, "\n" + " "*8 + "ID:", ch.id, "\n" + " "*8 + "Category:", f"{ch.category} [{ch.category_id}]" if ch.category is not None else "None")
            try:
                invit = await client.get_channel(int(ch.id)).create_invite(max_uses=1)
                print("        Invite:", invit)
            except:
                print("        Invite: No permission")

try:
    client.run(token)
except Exception as e:
    print("[ NO ] Token not working\n[WARN]", e)
