import discord
from discord.ext import commands

class GenZCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}

    @commands.command()
    async def whatisred(self, ctx):
        await ctx.send("Red Discord Bot is a self-hosted open-source modular bot for Discord. find it at discord.gg/red")

    @commands.command()
    async def afk(self, ctx):
        self.afk_users[ctx.author.id] = ctx.author.display_name
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
        await ctx.send(f"{ctx.author.mention} is now AFK.")

    @commands.command()
    async def afks(self, ctx):
        if not self.afk_users:
            await ctx.send("No one is currently AFK.")
            return

        afk_list = "\n".join(self.afk_users.values())
        await ctx.send(f"The following users are currently AFK:\n{afk_list}")

    @commands.command()
    @commands.is_owner()
    async def creditset(self, ctx, credit_type, *, credit_info):
        if credit_type.lower() not in ["owner", "developer", "contributor"]:
            await ctx.send("Invalid credit type. Valid types are `owner`, `developer`, and `contributor`.")
            return

        if credit_type.lower() == "owner":
            self.bot.owner_id = credit_info
        elif credit_type.lower() == "developer":
            self.bot.developer_name = credit_info
        else:
            self.bot.contributor_name = credit_info

        await ctx.send(f"{credit_type.title()} information updated.")

    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(title="Credits", color=0x7289da)
        embed.add_field(name="Owner", value=f"<@{self.bot.owner_id}>")
        embed.add_field(name="Developer", value=self.bot.developer_name)
        embed.add_field(name="Contributor", value=self.bot.contributor_name)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in self.afk_users:
            afk_name = self.afk_users[message.author.id]
            await message.author.edit(nick=afk_name[6:])
            del self.afk_users[message.author.id]
            await message.channel.send(f"Welcome back {message.author.mention}!")

def setup(bot):
    bot.add_cog(GenZCog(bot))
