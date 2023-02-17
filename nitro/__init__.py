from .nitro import NitroCog


def setup(bot):
    bot.add_cog(NitroCog(bot))
