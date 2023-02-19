import discord
from redbot.core import commands, checks

class AFKCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = set()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('!AFK'):
            # Update user's nickname with [AFK] prefix
            await message.author.edit(nick='[AFK] ' + message.author.display_name)
            self.afk_users.add(message.author.id)

        elif message.author.id in self.afk_users:
            # Remove [AFK] prefix from user's nickname
            await message.author.edit(nick=message.author.display_name[6:])
            self.afk_users.remove(message.author.id)
            await message.channel.send(f'{message.author.mention} is no longer AFK.')

    @commands.command()
    async def AFK(self, ctx):
        # Update user's nickname with [AFK] prefix
        await ctx.author.edit(nick='[AFK] ' + ctx.author.display_name)
        self.afk_users.add(ctx.author.id)
        await ctx.send(f'{ctx.author.mention} is now AFK.')

    @commands.command()
    async def AFKS(self, ctx):
        # List all users with [AFK] prefix in their nickname
        afk_users = [member for member in ctx.guild.members if member.nick and member.nick.startswith('[AFK]')]
        if afk_users:
            response = 'AFK Users: ' + ', '.join(member.mention for member in afk_users)
        else:
            response = 'No users are currently AFK.'
        await ctx.send(response)

def setup(bot):
    bot.add_cog(AFKCog(bot))