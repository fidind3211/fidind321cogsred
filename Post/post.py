import discord
from redbot.core import commands
import webcolors

class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def post(self, ctx, title, description, color, channel: discord.TextChannel):
        try:
            color_value = int(color, 16)
        except ValueError:
            try:
                color_value = int(webcolors.name_to_hex(color).lstrip('#'), 16)
            except ValueError:
                await ctx.send("Invalid color value")
                return

        embed = discord.Embed(title=title, description=description, color=color_value)
        await channel.send(embed=embed)

    @commands.command()
    async def postmessage(self, ctx, *, message):
        channel = ctx.channel
        await channel.send(message)

def setup(bot):
    bot.add_cog(Post(bot))