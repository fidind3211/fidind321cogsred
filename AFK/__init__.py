from .afk import AFK

def setup(bot):
    bot.add_cog(AFK(bot))
