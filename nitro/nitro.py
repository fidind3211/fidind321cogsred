import discord
from redbot.core import commands, Config

class NitroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)  # use your own identifier here
        default_global = {"nitro_links": {}}
        self.config.register_global(**default_global)

    @commands.command()
    async def nitro(self, ctx, nitro_name: str):
        nitro_links = await self.config.nitro_links()
        if nitro_name not in nitro_links:
            await ctx.send(f"Invalid Nitro name '{nitro_name}'. Use !addnitro to add a new Nitro link.")
        else:
            await ctx.send(nitro_links[nitro_name]["url"])

    @commands.command()
    @commands.is_owner()
    async def addnitro(self, ctx, nitro_name: str, nitro_url: str):
        await self.config.nitro_links.set_raw(nitro_name, value={"url": nitro_url})
        await ctx.send(f"Added new Nitro link '{nitro_name}': {nitro_url}")
