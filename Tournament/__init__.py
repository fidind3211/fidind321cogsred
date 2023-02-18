from .tournament import Tournament

def setup(bot):
    bot.add_cog(Tournament(bot))