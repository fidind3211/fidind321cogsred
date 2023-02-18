from redbot.core import commands

class Thatonecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whatisred(self, ctx):
        """
        Responds with a brief description and links for Red Discord Bot
        """
        response = "Red Discord Bot is a self-hosted bot made by a team of people. It provides a wide range of functionality and can be customized to suit your needs. You can learn more about Red Discord Bot by visiting their website at https://red-discordbot.readthedocs.io/en/latest/ or by joining their Discord server at https://discord.gg/red."
        await ctx.send(response)
        
    @commands.command()
    async def afk(self, ctx, *, message: str = "AFK"):
        """Sets your status to AFK and adds [AFK] to your nickname"""
        member = ctx.author
        self.afk_users[member.id] = message
        await member.edit(nick="[AFK] " + member.display_name)
        await ctx.send(f"{member.mention} is now AFK.")

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        # Check if the author is AFK and has sent a message
        if member.id in self.afk_users and message.content:
            # Remove [AFK] from the author's nickname
            await member.edit(nick=member.display_name.split("[AFK] ")[-1])
            # Send a message to welcome the author back
            await message.channel.send(f"Welcome back, {member.mention}!")
            del self.afk_users[member.id]

def setup(bot):
    bot.add_cog(Thatonecog(bot))
