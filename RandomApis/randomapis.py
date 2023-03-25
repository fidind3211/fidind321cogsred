import discord
import requests
from discord.ext import commands

class RandomAPIs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def amogus(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        avatar_url = str(user.avatar_url_as(format="png", size=1024))
        username = str(user)
        
        params = {
            "username": username,
            "avatar": avatar_url
        }
        
        response = requests.get("https://some-random-api.ml/premium/amongus", params=params)
        response.raise_for_status()
        
        data = response.json()
        image_url = data.get("link")
        if not image_url:
            await ctx.send("Failed to get image.")
            return
        
        await ctx.send(image_url)
