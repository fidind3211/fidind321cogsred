from .amplify import Amplify

def setup(bot):
    bot.add_cog(Amplify(bot))