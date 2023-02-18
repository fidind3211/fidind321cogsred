import discord
from discord.ext import commands
from random import shuffle

TROPHY_EMOJI = "\U0001F3C6"
X_EMOJI = "\U0000274C"

class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def starttorny(self, ctx, num_participants: int, *participants: str):
        if not ctx.author.guild_permissions.administrator:
            return await ctx.send("You do not have permission to start a tournament.")

        if num_participants % 2 != 0:
            return await ctx.send("Number of participants should be even.")

        if len(participants) != num_participants:
            return await ctx.send("Number of participants doesn't match the provided participants list.")

        shuffle(participants)
        round_num = 1
        while len(participants) > 1:
            await ctx.send(f"**Round {round_num}**")
            for i in range(0, len(participants), 2):
                message = await ctx.send(f"{participants[i]} VS {participants[i+1]}")
                await message.add_reaction(TROPHY_EMOJI)
                await message.add_reaction(X_EMOJI)
            round_num += 1
            winners = []
            async for reaction in message.channel.history(limit=len(participants), after=message.created_at):
                if reaction.message.id != message.id:
                    continue
                if reaction.emoji == TROPHY_EMOJI:
                    winners.append(reaction.message.content.split(" VS ")[0])
                elif reaction.emoji == X_EMOJI:
                    winners.append(reaction.message.content.split(" VS ")[1])
            participants = winners
        await ctx.send(f"{participants[0]} won the tournament!")

def setup(bot):
 bot.add_cog(Tournament(bot))
