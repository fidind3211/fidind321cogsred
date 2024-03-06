from .randomapis import RandomApis

async def setup(bot):
    bot.add_cog(RandomApis(bot))
