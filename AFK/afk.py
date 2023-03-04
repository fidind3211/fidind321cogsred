import discord
from redbot.core import commands, checks

class AFKCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = set()
        self.afk_reasons = {}

    async def _set_afk(self, user, reason=None):
        if user.id not in self.afk_users:
            await user.edit(nick='[AFK] ' + user.display_name)
            self.afk_users.add(user.id)
            if reason:
                self.afk_reasons[user.id] = reason[:25]
            embed = discord.Embed(
                title='AFK status updated',
                description='You are now marked as AFK.',
                color=discord.Color.dark_orange()
            )
            await user.send(embed=embed)

    async def _remove_afk(self, user):
        if user.id in self.afk_users:
            await user.edit(nick=user.display_name[6:])
            self.afk_users.remove(user.id)
            if user.id in self.afk_reasons:
                del self.afk_reasons[user.id]
            embed = discord.Embed(
                title='AFK status updated',
                description='You are no longer marked as AFK.',
                color=discord.Color.dark_green()
            )
            await user.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == '!AFK':
            await self._set_afk(message.author)

    @commands.command()
    async def afk(self, ctx, *, reason=None):
        await self._set_afk(ctx.author, reason)
        if reason:
            embed = discord.Embed(
                title='AFK status updated',
                description=f'You are now marked as AFK. Reason: {reason[:100]}',
                color=discord.Color.dark_orange()
            )
        else:
            embed = discord.Embed(
                title='AFK status updated',
                description='You are now marked as AFK.',
                color=discord.Color.dark_orange()
            )
        await ctx.send(embed=embed)

    @commands.command()
    async def back(self, ctx):
        await self._remove_afk(ctx.author)
        embed = discord.Embed(
            title='AFK status updated',
            description='You are no longer marked as AFK.',
            color=discord.Color.dark_green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def isafk(self, ctx, user: discord.Member):
        if user.id in self.afk_users:
            reason = self.afk_reasons.get(user.id, '')
            embed = discord.Embed(
                title='AFK status',
                description=f'{user.display_name} is AFK. Reason: {reason}',
                color=discord.Color.dark_orange()
            )
        else:
            embed = discord.Embed(
                title='AFK status',
                description=f'{user.display_name} is not AFK.',
                color=discord.Color.dark_green()
            )
        await ctx.send(embed=embed)

    @commands.command()
    async def afks(self, ctx):
        guild = ctx.guild
        await guild.fetch_members()
        afk_users = [member for member in guild.members if member.nick and member.nick.startswith('[AFK]') and member.id in self.afk_users]
        if afk_users:
            response = 'AFK Users:\n'
            for member in afk_users:
                reason = self.afk_reasons.get(member.id)
                if reason:
                    response += f"{member.name}#{member.discriminator} ({member.id}): {reason}\n"
                else:
                    response += f"{member.name}#{member.discriminator} ({member.id})\n"
            embed = discord.Embed(
                title='List of AFK Users',
                description=response,
                color=discord.Color.dark_orange()
            )
        else:
            embed = discord.Embed(
                title='List of AFK Users',
                description='No users are currently AFK.',
                color=discord.Color.dark_green()
            )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AFKCog(bot))