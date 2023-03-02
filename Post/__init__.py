from .post import Post

def setup(bot):
    bot.add_cog(Post(bot))