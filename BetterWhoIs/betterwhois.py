import discord
from discord.ext import commands
from datetime import datetime

class BetterWhoIsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.command()
async def whois(ctx, user: discord.Member):
    # User information
    created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    joined_at = user.joined_at.strftime("%Y-%m-%d %H:%M:%S")
    user_id = user.id
    user_name = user.name
    user_discriminator = user.discriminator
    user_avatar = user.avatar_url

    # Guild information
    member_number = sum(1 for member in ctx.guild.members if not member.bot and member.joined_at < user.joined_at) + 1

    # Roles information
    roles_list = [role.name for role in user.roles if role.name != "@everyone"]
    roles = ", ".join(roles_list) if roles_list else "None"

    # Status information
    status = str(user.status).title()

    # Game information
    game_name = "None"
    game_image = None
    if user.activity is not None:
        if isinstance(user.activity, discord.Spotify):
            game_name = f"Listening to {user.activity.title} by {user.activity.artist}"
            game_image = user.activity.album_cover_url
        elif isinstance(user.activity, discord.Game):
            game_name = f"Playing {user.activity.name}"
            game_image = user.activity.large_image_url

    # Send the response
    embed = discord.Embed(title=f"{user.name}'s Info", description="", color=0x00aaff)
    embed.add_field(name="User ID", value=user_id, inline=True)
    embed.add_field(name="User Name", value=user_name, inline=True)
    embed.add_field(name="Discriminator", value=user_discriminator, inline=True)
    embed.add_field(name="Account Created", value=created_at, inline=False)
    embed.add_field(name="Joined Server", value=joined_at, inline=False)
    embed.add_field(name="Member Number", value=member_number, inline=False)
    embed.add_field(name="Roles", value=roles, inline=False)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name=game_name, value="", inline=True)
    embed.set_thumbnail(url=user_avatar)
    if game_image is not None:
        embed.set_image(url=game_image)
    await ctx.send(embed=embed)

bot.run('')  # Leave this line empty
