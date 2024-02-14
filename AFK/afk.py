import discord
from redbot.core import commands
from datetime import datetime
import traceback

class AFKCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = set()
        self.afk_reasons = {}

    async def _set_afk(self, user, reason=None):
        try:
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
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f"An error occurred: {e}")

    async def _remove_afk(self, user):
        try:
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
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f"An error occurred: {e}")

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.content == '!AFK':
                await self._set_afk(message.author)
        except Exception as e:
            traceback.print_exc()
            await message.channel.send(f"An error occurred: {e}")

    @commands.command()
    async def afk(self, ctx, *, reason=None):
        try:
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
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f"An error occurred: {e}")

    @commands.command()
    async def back(self, ctx):
        try:
            await self._remove_afk(ctx.author)
            embed = discord.Embed(
                title='AFK status updated',
                description='You are no longer marked as AFK.',
                color=discord.Color.dark_green()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f"An error occurred: {e}")

    @commands.command()
    async def isafk(self, ctx, user_id: int):
        try:
            user = ctx.guild.get_member(user_id)
            if user and user.id in self.afk_users:
                reason = self.afk_reasons.get(user.id, '')
                timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                embed = discord.Embed(
                    title='AFK status',
                    description=f'{user.display_name} is AFK since {timestamp}. Reason: {reason}',
                    color=discord.Color.dark_orange()
                )
                embed.set_footer(text=f"AFK since {timestamp}")
            else:
                member = await ctx.guild.fetch_member(user_id)
                embed = discord.Embed(
                    title='AFK status',
                    description=f'{member.display_name} is not AFK.',
                    color=discord.Color.dark_green()
                )
            await ctx.send(embed=embed)
        except Exception as e:
            traceback.print_exc()
            await ctx.send(f"An error occurred: {e}")

def setup(bot):
    bot.add_cog(AFKCog(bot))
