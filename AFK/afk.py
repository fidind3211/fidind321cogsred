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
            await user.send('You are now marked as AFK.')

    async def _remove_afk(self, user):
        if user.id in self.afk_users:
            await user.edit(nick=user.display_name[6:])
            self.afk_users.remove(user.id)
            if user.id in self.afk_reasons:
                del self.afk_reasons[user.id]
            await user.send('You are no longer marked as AFK.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == '!AFK':
            await self._set_afk(message.author)

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
            response = 'AFK Users:\n'
            for member in afk_users:
                reason = self.afk_reasons.get(member.id)
                if reason:
                    response += f"{member.name}#{member.discriminator} ({member.id}): {reason}\n"
                else:
                    response += f"{member.name}#{member.discriminator} ({member.id})\n"
        else:
            response = 'No users are currently AFK.'
        await ctx.send(response)

def setup(bot):
    bot.add_cog(AFKCog(bot))