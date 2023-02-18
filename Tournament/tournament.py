import discord
from discord.ext import commands
from random import shuffle

class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def starttorny(self, ctx, num_of_participants: int, *participants: str):
        if num_of_participants <= 1:
            await ctx.send("Tournament requires at least 2 participants.")
            return

        if num_of_participants != len(participants):
            await ctx.send("Number of participants does not match the given count.")
            return

        shuffle(participants)

        await ctx.send(f"Tournament bracket is completely randomized.\n{num_of_participants} participants are: {', '.join(participants)}")

        for i in range(0, len(participants), 2):
            user1 = participants[i]
            user2 = participants[i+1]

            message = await ctx.send(f"{user1} VS {user2}")

            await message.add_reaction('🏆')
            await message.add_reaction('❌')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        message = reaction.message

        if user == self.bot.user:
            return

        if reaction.emoji == '🏆' or reaction.emoji == '❌':
            winner = None

            if reaction.emoji == '🏆':
                winner = message.content.split(' VS ')[0]
            else:
                winner = message.content.split(' VS ')[1]

            await message.delete()
            await message.channel.send(f"{winner} moves to the next round!")

def setup(bot):
    bot.add_cog(Tournament(bot))
