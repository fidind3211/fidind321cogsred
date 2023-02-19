import discord
from redbot.core import commands, checks

class AFKCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = set()
        self.afk_embed = None
        self.afk_message = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('!AFK'):
            # Update user's nickname with [AFK] prefix
            await message.author.edit(nick='[AFK] ' + message.author.display_name)
            self.afk_users.add(message.author.id)
            await message.channel.send(f'{message.author.mention} is now AFK.')
            await self.update_afk_embed(message.guild)

        elif message.author.id in self.afk_users:
            # Remove [AFK] prefix from user's nickname
            await message.author.edit(nick=message.author.display_name[6:])
            self.afk_users.remove(message.author.id)
            await message.channel.send(f'{message.author.mention} is no longer AFK.')
            await self.update_afk_embed(message.guild)

    async def update_afk_embed(self, guild):
        if not self.afk_message:
            # Send initial message and store message object
            channel = self.bot.get_channel(1234567890)  # Replace with channel ID
            self.afk_message = await channel.send(embed=discord.Embed(title="AFK Users"))
            self.afk_embed = self.afk_message.embeds[0]

        # Clear existing fields from embed
        self.afk_embed.clear_fields()

        # Add fields to embed for each AFK user
        for member in guild.members:
            if member.nick and member.nick.startswith('[AFK]'):
                self.afk_embed.add_field(name=member.display_name, value="AFK", inline=False)

        # Update message with new embed
        if self.afk_embed.fields:
            if not self.afk_embed.footer:
                self.afk_embed.set_footer(text="Last updated:")
            await self.afk_message.edit(embed=self.afk_embed)
        else:
            await self.afk_message.delete()
            self.afk_message = None

    @commands.command()
    async def AFK(self, ctx):
        # Update user's nickname with [AFK] prefix
        await ctx.author.edit(nick='[AFK] ' + ctx.author.display_name)
        self.afk_users.add(ctx.author.id)
        await ctx.send(f'{ctx.author.mention} is now AFK.')
        await self.update_afk_embed(ctx.guild)

    @commands.command()
    async def AFKS(self, ctx):
        # List all users with [AFK] prefix in their nickname
        afk_users = [member for member in ctx.guild.members if member.nick and member.nick.startswith('[AFK]')]
        if afk_users:
            response = 'AFK Users: ' + ', '.join(member.mention for member in afk_users)
        else:
            response = 'No users are currently AFK.'
        await ctx.send(response)

    @commands.Cog.listener()
    async def on_message(self, message):
        for member in message.mentions:
            if member.id in self.afk_users:
                # Send DM to message author indicating mentioned user is AFK
                author = message.author
                await author.send(f'{member.display_name} is currently AFK.')

def setup(bot):
    bot.add_cog(AFKCog(bot))