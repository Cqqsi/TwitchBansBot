
import discord
from discord.ext import commands
import math
import json

bot = commands.Bot(command_prefix = ".", help_command=None)

@bot.event
async def on_ready():
    bot.load_extension('commands')
    latency = math.ceil(bot.latency * 1000)
    name = bot.user.name
    guild = bot.guilds
    users = len(bot.users)
    server = len(guild)
    print(f"\n{name} is online!\nConnected on {server} servers \nCurrent Ping {latency}ms\n")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"twitch bans @ {latency}ms!", url="https://twitch.tv/twitch"))


bot.run("") # Put in your own client.id
