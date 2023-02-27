from .joinreactionrole import JoinReactionRole

def setup(bot):
    bot.add_cog(JoinReactionRole(bot))