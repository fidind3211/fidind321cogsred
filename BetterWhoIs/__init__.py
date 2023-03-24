from .betterwhois import BetterWhoIsCog

async def setup(bot):
    bot.add_cog(BetterWhoIsCog(bot))
