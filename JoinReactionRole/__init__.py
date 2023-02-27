from .join_reaction_role import JoinReactionRoleCog


def setup(bot):
    bot.add_cog(JoinReactionRoleCog(bot))