from redbot.core import commands
from typing import List
import discord
from random import shuffle


class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.participants = []

    @commands.command()
    async def starttorny(self, ctx, num_participants: int, *participants: str):
        if num_participants != len(participants):
            await ctx.send("Number of participants and number of names provided do not match.")
            return
        if len(participants) < 2:
            await ctx.send("A tournament needs at least 2 participants.")
            return
        shuffle(participants)
        self.participants = participants
        await ctx.send("Tournament bracket has been generated and randomized!")
        for i in range(0, len(self.participants), 2):
            player1 = self.participants[i]
            player2 = self.participants[i + 1]
            match = f"{player1} VS {player2}"
            await ctx.send(f"**Match {i//2 + 1}**: {match}")

    @commands.command()
    @commands.has_role("Tournament Admin")
    async def win(self, ctx):
        if len(self.participants) == 0:
            await ctx.send("No tournament bracket is currently active.")
            return
        winner = self.participants.pop(0)
        await ctx.send(f"{winner} has won the match!")
        if len(self.participants) == 1:
            await ctx.send(f"The winner of the tournament is: {self.participants[0]}")
            self.participants = []

    @commands.command()
    @commands.has_role("Tournament Admin")
    async def lose(self, ctx):
        if len(self.participants) == 0:
            await ctx.send("No tournament bracket is currently active.")
            return
        self.participants.pop(0)
        await ctx.send("Match has been forfeited.")
        if len(self.participants) == 1:
            await ctx.send(f"The winner of the tournament is: {self.participants[0]}")
            self.participants = []

def setup(bot):
    bot.add_cog(Tournament(bot))