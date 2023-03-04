import discord
from discord.ext import commands
import chess

class Chess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.games = {}

    @commands.command()
    async def newchess(self, ctx):
        # Check if a game is already in progress
        if ctx.channel.id in self.games:
            await ctx.send('A game is already in progress in this channel!')
            return

        # Initialize a new chess board
        board = chess.Board()
        game_over = False
        turn = True

        # Display the initial chess board
        message = await ctx.send(f'```\n{board}\n```')

        # Store the game state
        self.games[ctx.channel.id] = (board, message, turn)

        # Keep accepting moves until the game is over
        while not game_over:
            # Wait for a move from the player whose turn it is
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                move_msg = await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.send(f'{ctx.author.mention}, your turn has timed out!')
                break

            move = move_msg.content.lower()

            # Check if the player wants to end the game
            if move == '!endchess':
                await ctx.send('The game has ended!')
                del self.games[ctx.channel.id]
                game_over = True
                break

            # Try to make the move on the chess board
            try:
                board, message, turn = self.games[ctx.channel.id]
                if turn:
                    board.push_san(move)
                    turn = False
                else:
                    board.push_san(move)
                    turn = True
            except ValueError:
                await ctx.send('That move is not valid. Try again!')
                continue

            # Check if the game has ended
            if board.is_game_over():
                result = board.result()
                if result == '1-0':
                    winner = 'White'
                elif result == '0-1':
                    winner = 'Black'
                else:
                    winner = 'Nobody'
                await message.edit(content=f'```\n{board}\n```{winner} has won the game!')
                del self.games[ctx.channel.id]
                game_over = True
                break

            # Display the updated chess board
            await message.edit(content=f'```\n{board}\n```')
            self.games[ctx.channel.id] = (board, message, turn)

    @commands.command()
    async def endchess(self, ctx):
        # Check if a game is in progress
        if ctx.channel.id not in self.games:
            await ctx.send('No game is in progress in this channel!')
            return

        # End the game
        await ctx.send('The game has ended!')
        del self.games[ctx.channel.id]

def setup(bot):
    bot.add_cog(Chess(bot))