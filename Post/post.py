import discord
from redbot.core import commands

class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def post(self, ctx, title, description, color, channel: discord.TextChannel):
        embed = discord.Embed(title=title, description=description, color=int(color, 16))
        await channel.send(embed=embed)
    
    @commands.command()
    async def postmessage(self, ctx, message, channel: discord.TextChannel):
        await channel.send(message)

def setup(bot):
    bot.add_cog(Post(bot))