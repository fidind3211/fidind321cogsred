import discord
import aiohttp
from redbot.core import commands

class RandomApis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def comrade(self, ctx, *, user: discord.Member=None):
        user = user or ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/overlay/comrade?avatar={user.avatar_url}") as resp:
                if resp.status != 200:
                    return await ctx.send('Error getting image...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'comrade.png'))

def setup(bot):
    bot.add_cog(RandomApis(bot))