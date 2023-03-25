import discord
import requests

from redbot.core import commands

class RandomApis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://some-random-api.ml/premium/amongus"

    @commands.command(name="amogus")
    async def amogus(self, ctx, *, username: str = None):
        avatar = str(ctx.author.avatar_url_as(format="png"))
        if not username:
            username = ctx.author.name

        params = {"username": username, "avatar": avatar}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        image_url = response.json()["data"]
        embed = discord.Embed(title="Amogus", color=discord.Color.red())
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RandomApis(bot))
