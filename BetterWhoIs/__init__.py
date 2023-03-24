from .betterwhois import BetterWhoIsCog

def setup(bot):
    bot.add_cog(BetterWhoIsCog(bot))