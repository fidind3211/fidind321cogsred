import discord
from discord.utils import get
from redbot.core import commands, checks, Config


class JoinReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)

    async def assign_join_role(self, member):
        join_role_id = await self.config.guild(member.guild).join_role()
        join_role = get(member.guild.roles, id=join_role_id)
        if join_role:
            await member.add_roles(join_role)

    async def remove_join_role_and_assign_reaction_role(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        join_role_id = await self.config.guild(guild).join_role()
        reaction_role_id = await self.config.guild(guild).reaction_role()
        join_role = get(guild.roles, id=join_role_id)
        reaction_role = get(guild.roles, id=reaction_role_id)
        if join_role and reaction_role:
            await member.remove_roles(join_role)
            await member.add_roles(reaction_role)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.assign_join_role(member)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = await self.config.guild(payload.guild_id).message_id()
        if payload.message_id == message_id:
            await self.remove_join_role_and_assign_reaction_role(payload)

    @commands.command()
    @checks.admin_or_permissions(manage_roles=True)
    async def set_join_role(self, ctx, role: discord.Role):
        await self.config.guild(ctx.guild).join_role.set(role.id)
        await ctx.send(f"Join role set to {role.mention}.")

    @commands.command()
    @checks.admin_or_permissions(manage_roles=True)
    async def set_reaction_role(self, ctx, role: discord.Role):
        await self.config.guild(ctx.guild).reaction_role.set(role.id)
        await ctx.send(f"Reaction role set to {role.mention}.")

    @commands.command()
    @checks.admin_or_permissions(manage_roles=True)
    async def set_message(self, ctx, message: discord.Message):
        await self.config.guild(ctx.guild).message_id.set(message.id)
        await ctx.send(f"Message set to {message.jump_url}.")

def setup(bot):
    bot.add_cog(JoinReactionRole(bot))