import discord
from discord.ext import commands

class Fidind321sGenZcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}
        self.dev_info = ""
        self.owner_info = ""
        self.contributor_info = ""
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.author.id in self.afk_users:
                del self.afk_users[message.author.id]
                await message.author.edit(nick=message.author.display_name.replace("[AFK] ", ""))
                await message.channel.send(f"Welcome back {message.author.mention}!")
                
    @commands.command()
    async def afk(self, ctx):
        """Set your status as AFK."""
        self.afk_users[ctx.author.id] = True
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
        await ctx.send(f"{ctx.author.mention} is now AFK.")
        
    @commands.command()
    async def afks(self, ctx):
        """List all users who are currently AFK."""
        afk_list = [str(self.bot.get_user(user_id)) for user_id in self.afk_users.keys()]
        if afk_list:
            await ctx.send("The following users are currently AFK:\n• " + "\n• ".join(afk_list))
        else:
            await ctx.send("No users are currently AFK.")
        
    @commands.command()
    @commands.is_owner()
    async def creditset(self, ctx, info_type: str, *, info: str):
        """Set the developer, owner, or contributor info."""
        if info_type.lower() == "dev":
            self.dev_info = info
            await ctx.send("Developer info updated.")
        elif info_type.lower() == "owner":
            self.owner_info = info
            await ctx.send("Owner info updated.")
        elif info_type.lower() == "contributor":
            self.contributor_info = info
            await ctx.send("Contributor info updated.")
        else:
            await ctx.send("Invalid info type. Please choose from dev, owner, or contributor.")
            
    @commands.command()
    async def credits(self, ctx):
        """Display the developer, owner, and contributor info."""
        embed = discord.Embed(title="Credits", color=0xff0000)
        if self.dev_info:
            embed.add_field(name="Developer", value=self.dev_info)
        if self.owner_info:
            embed.add_field(name="Owner", value=self.owner_info)
        if self.contributor_info:
            embed.add_field(name="Contributor", value=self.contributor_info)
        if not self.dev_info and not self.owner_info and not self.contributor_info:
            embed.description = "No credits set."
        await ctx.send(embed=embed)
    
    @commands.command()
    async def whatisred(self, ctx):
        """Explain what Red Discord Bot is."""
        embed = discord.Embed(title="What is Red Discord Bot?", color=0xff0000, description="Red is a customizable, self-hosted Discord bot.")
        embed.add_field(name="Website", value="https://red-discordbot.readthedocs.io/en/latest/")
        embed.set_footer(text="For more information, visit the website.")
        await ctx.send(embed=embed)