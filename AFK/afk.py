import discord
from redbot.core import commands, checks

class AFKCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = set()

    async def _set_afk(self, user, reason=None):
        if user.id not in self.afk_users:
            afk_tag = f'[AFK] {reason[:25]}' if reason else '[AFK]'
            await user.edit(nick=afk_tag + ' ' + user.display_name)
            self.afk_users.add(user.id)
            message = 'You are now marked as AFK.'
            if reason:
                message += f' Reason: {reason}'
            await user.send(message)

    async def _remove_afk(self, user):
        if user.id in self.afk_users:
            await user.edit(nick=user.display_name[6:])
            self.afk_users.remove(user.id)
            await user.send('You are no longer marked as AFK.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith('!afk'):
            reason = message.content[5:].strip()
            await self._set_afk(message.author, reason)

    @commands.command()
    async def afk(self, ctx, *, reason=None):
        await self._set_afk(ctx.author, reason)

    @commands.command()
    async def back(self, ctx):
        await self._remove_afk(ctx.author)

    @commands.command()
    async def afks(self, ctx):
        afk_users = [member for member in self.bot.get_all_members() if member.nick and member.nick.startswith('[AFK]') and member.id in self.afk_users]
        if afk_users:
            response = 'AFK Users:\n' + '\n'.join(f"{member.name}#{member.discriminator} ({member.id})" for member in afk_users)
        else:
            response = 'No users are currently AFK.'
        await ctx.send(response)

def setup(bot):
    bot.add_cog(AFKCog(bot))