from .betterwhois import betterwhoisCog

def setup(bot):
    bot.add_cog(betterwhoisCog(bot))