import discord
from discord.ext import commands
from datetime import datetime, timedelta
import aiohttp
from io import BytesIO

class BetterWhoIsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bwhois(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        embed = discord.Embed(title=f"User Info - {user.name}", color=0x00FFFF)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="Nickname", value=user.nick, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Activity", value=user.activity, inline=True)
        embed.add_field(name="Account Created", value=user.created_at.strftime("%m/%d/%Y %H:%M:%S"), inline=True)
        embed.add_field(name="Joined Server", value=user.joined_at.strftime("%m/%d/%Y %H:%M:%S"), inline=True)

        if user.activity is not None and isinstance(user.activity, discord.Spotify):
            artist = user.activity.artist
            album = user.activity.album
            track_title = user.activity.title
            album_cover_url = user.activity.album_cover_url
            track_url = user.activity.track_url

            embed.add_field(name="Currently Listening to Spotify", value=f"{artist} - {track_title}", inline=False)
            embed.set_image(url=album_cover_url)

        if user.activity is not None and isinstance(user.activity, discord.Game):
            game_name = user.activity.name
            if user.activity.large_image_url:
                image_url = user.activity.large_image_url
            elif user.activity.small_image_url:
                image_url = user.activity.small_image_url

            embed.add_field(name="Currently Playing", value=game_name, inline=True)
            async with session.get(image_url) as r:
                if r.status == 200:
                    data = BytesIO(await r.read())
                    embed.set_image(url=image_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BetterWhoIsCog(bot))    
