import discord
from discord.ext import commands

class PhoneStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user.name}!')
        await self.bot.change_presence(status=discord.Status.online, mobile=True)

def setup(bot):
    bot.add_cog(PhoneStatus(bot))