from .chess import Chess

def setup(bot):
    bot.add_cog(Chess(bot))