import discord
import requests

from redbot.core import commands

class RandomApis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://some-random-api.ml/premium/amongus"

    @commands.command(name="amogus")
    async def amogus(self, ctx, username: str = None, *, custom: str = None):
        if username is None and len(ctx.message.mentions) > 0:
            username = ctx.message.mentions[0].name
            avatar_url = str(ctx.message.mentions[0].avatar_url_as(format='png'))
        else:
            username = ctx.author.name
            avatar_url = str(ctx.author.avatar_url_as(format='png'))

        params = {"username": username, "avatar": avatar_url}
        if custom:
            params["custom"] = custom
        response = requests.get(self.base_url, params=params)
        image_url = response.json()["link"]
        embed = discord.Embed(title="Amogus", color=discord.Color.red())
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RandomApis(bot))
