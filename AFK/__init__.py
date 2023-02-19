from .afk import AFKCog

def setup(bot):
    bot.add_cog(AFKCog(bot))
