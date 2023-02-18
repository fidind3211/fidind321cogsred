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

    @commands.command()
    async def listnitro(self, ctx):
        nitro_links = await self.config.nitro_links()
        if not nitro_links:
            await ctx.send("There are no Nitro links configured.")
        else:
            nitro_list = "\n".join([f"{name}: {link['url']}" for name, link in nitro_links.items()])
            await ctx.send(f"Available Nitro links:\n{nitro_list}")

    @commands.command()
    @commands.is_owner()
    async def removenitro(self, ctx, nitro_name: str):
        nitro_links = await self.config.nitro_links()
        if nitro_name not in nitro_links:
            await ctx.send(f"Invalid Nitro name '{nitro_name}'.")
        else:
            await self.config.nitro_links.clear_raw(nitro_name)
            await ctx.send(f"Removed Nitro link '{nitro_name}'.")

    @commands.command()
    @commands.is_owner()
    async def updatenitro(self, ctx, nitro_name: str, nitro_url: str):
        nitro_links = await self.config.nitro_links()
        if nitro_name not in nitro_links:
            await ctx.send(f"Invalid Nitro name '{nitro_name}'. Use !addnitro to add a new Nitro link.")
        else:
            await self.config.nitro_links.set_raw(nitro_name, value={"url": nitro_url})
            await ctx.send(f"Updated Nitro link '{nitro_name}': {nitro_url}")

    @commands.command()
    @commands.is_owner()
    async def nitrocount(self, ctx):
        nitro_links = await self.config.nitro_links()
        if not nitro_links:
            await ctx.send("There are no Nitro links configured.")
        else:
            counts = {name: 0 for name in nitro_links.keys()}
            messages = await ctx.channel.history(limit=1000).flatten()
            for message in messages:
                for word in message.content.split():
                    if word in nitro_links:
                        counts[word] += 1
            count_list = "\n".join([f"{name}: {count}" for name, count in counts.items()])
            await ctx.send(f"Usage counts:\n{count_list}")
