from .phone_status import PhoneStatus

def setup(bot):
    bot.add_cog(PhoneStatus(bot))