from .post import Post

async def setup(bot):
    bot.add_cog(Post(bot))
