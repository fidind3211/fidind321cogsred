from .afk import AFKCog

async def setup(bot):
    bot.add_cog(AFKCog(bot))
