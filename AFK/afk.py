import discord
from redbot.core import commands

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx):
        member = ctx.author
        old_nickname = member.display_name

        if "[AFK]" in old_nickname:
            new_nickname = old_nickname.replace("[AFK] ", "")
            message = f"Welcome back {member.mention}!"
        else:
            new_nickname = f"[AFK] {old_nickname}"
            message = f"{member.mention} is now AFK."

        await member.edit(nick=new_nickname)
        await ctx.send(message)

def setup(bot):
    cog = AFK(bot)
    bot.add_cog(cog)
