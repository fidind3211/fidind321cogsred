from discord.ext import commands
import random

class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_brackets = {}

    @commands.command()
    async def starttorny(self, ctx, *players):
        num_players = len(players)
        if num_players < 2:
            await ctx.send('You need at least 2 players to start a tournament.')
            return
        elif num_players > 32:
            await ctx.send('The maximum number of players is 32.')
            return

        # Shuffle the players to create a randomized bracket
        random.shuffle(players)

        # Create the bracket and send it to the channel
        bracket = []
        while len(players) > 1:
            bracket.append((players.pop(0), players.pop(0)))
        if players:
            bracket.append((players[0], 'BYE'))
        message = 'Tournament bracket created!\n' + self.print_bracket(bracket)
        await ctx.send(message)

        # Store the active bracket in a dictionary with the channel ID as the key
        self.active_brackets[ctx.channel.id] = bracket

        # Start the first round of the tournament
        await ctx.send('First match: {} VS {}'.format(bracket[0][0], bracket[0][1]))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def win(self, ctx):
        bracket = self.active_brackets.get(ctx.channel.id)
        if not bracket:
            await ctx.send('No active tournament found.')
            return
        winner = bracket.pop(0)[0]
        if bracket:
            message = 'Next match: {} VS {}'.format(bracket[0][0], bracket[0][1])
        else:
            message = 'Tournament complete! {} is the winner.'.format(winner)
        await ctx.send(message)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lose(self, ctx):
        bracket = self.active_brackets.get(ctx.channel.id)
        if not bracket:
            await ctx.send('No active tournament found.')
            return
        winner = bracket.pop(0)[1]
        if bracket:
            message = 'Next match: {} VS {}'.format(bracket[0][0], bracket[0][1])
        else:
            message = 'Tournament complete! {} is the winner.'.format(winner)
        await ctx.send(message)

    def print_bracket(self, bracket):
        max_len = max(len(p1) + len(p2) + 3 for p1, p2 in bracket)
        border = '+' + '-' * (max_len + 2) + '+'
        lines = []
        for p1, p2 in bracket:
            line = '| ' + p1.ljust(max_len - len(p2)) + ' VS ' + p2 + ' |'
            lines.append(line)
        return '```' + border + '\n' + '\n'.join(lines) + '\n' + border + '```'

def setup(bot):
    bot.add_cog(Tournament(bot))
