from .nitro import NitroCog


async def setup(bot):
    bot.add_cog(NitroCog(bot))
