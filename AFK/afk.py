import discord
from discord.ext import commands
from datetime import datetime


class AFKCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_statuses = {}
        self.afk_reasons = {}

    async def _set_afk(self, user, afk=True, reason=None):
        self.afk_statuses[user.id] = afk
        self.afk_reasons[user.id] = (reason, datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.author.id in self.afk_statuses and self.afk_statuses[message.author.id]:
            await message.channel.send(f"{message.author.mention} is currently AFK: {self.afk_reasons[message.author.id][0]} since {self.afk_reasons[message.author.id][1]}.")
            await message.add_reaction("👀")

    @commands.command(name="afk")
    async def afk_command(self, ctx, *, reason=None):
        """Set yourself as AFK."""
        await self._set_afk(ctx.author, True, reason)
        await ctx.send(f"You are now AFK: {reason}")

    @commands.command(name="notafk")
    async def not_afk_command(self, ctx):
        """Remove your AFK status."""
        await self._set_afk(ctx.author, False)
        await ctx.send("You are no longer AFK.")
