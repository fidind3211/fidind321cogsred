import discord
from redbot.core import commands

class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def post(self, ctx, title, description, color, channel: discord.TextChannel):
        try:
            if color.startswith("#"):
                # if color starts with '#' it's a hexadecimal color code
                color_value = int(color[1:], 16)
            else:
                # otherwise, it's a color name
                color_value = getattr(discord.Colour, color.lower())().value
        except (KeyError, ValueError):
            await ctx.send(f"Invalid color '{color}'.")
            return
        
        embed = discord.Embed(title=title, description=description, color=color_value)
        await channel.send(embed=embed)
    
    @commands.command()
    async def postmessage(self, ctx, message, channel: discord.TextChannel):
        await channel.send(message)

def setup(bot):
    bot.add_cog(Post(bot))
