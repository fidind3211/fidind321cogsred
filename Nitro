import discord
from redbot.core import commands

class NitroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nitro(self, ctx, *, arg=""):
        if arg == "nerd":
            await ctx.send("https://discord.gift/abc123") 
        else:
            await ctx.send("https://discord.gift/xyz456") 

def setup(bot):
    bot.add_cog(NitroCog(bot))
