import discord
from discord.ext import commands
from datetime import date
import datetime
from bs4 import BeautifulSoup
import re
import requests


class commands(commands.Cog, name='commands'):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def bans(self, ctx, user):
        today = datetime.datetime.utcnow()
        today = today.strftime("%H:%M %p")

        page = requests.get(f'https://streamerbans.com/user/{user}')
        soup = BeautifulSoup(page.text, 'html.parser')
        i = soup.select('div', class_="mt-4 w-full")

        try:
            for i in soup():
                divider = soup.findAll('div', class_="text-center mx-4 md:mx-12")

                for objects in divider:
                    total = divider[0].get_text()
                    last = divider[2].get_text()
                    longest = divider[1].get_text()

                images = soup.findAll('img')
                for image in images:
                    image = images[0]
                    image = image['src']

                member = ctx.message.author
                pfp = member.avatar_url

            embed=discord.Embed(title=f"@{user.lower()}", description=f"{user}'s **ban history**\n based on the amount of ban(s), longest one and the recent one.\n Everything is handled by https://streamerbans.com/ \n", color=0x36393E)
            embed.add_field(name="``Total ban(s)``", value=f"{total.replace('Total bans', '')}", inline=True)
            embed.add_field(name="``Longest one``", value=f"{longest.replace('Longest ban', '')}", inline=True)
            embed.add_field(name="``Last one``", value=f"{last.replace('Last ban', '')}", inline=True)
            embed.set_thumbnail(url=f"{image}")
            embed.set_footer(text=f"Requested by {ctx.author} @ {today}", icon_url=f"{pfp}")
            await ctx.send(embed=embed)

        except Exception:
            await ctx.send(f"**{user}** has no bans, or this user isn't on the database.")


def setup(bot):
    bot.add_cog(commands(bot))
