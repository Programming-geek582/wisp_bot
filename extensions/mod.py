import nextcord
from nextcord.ext import commands

class Mod(commands.Cog, name="mod"):
    """Mod commands for only moderators and admins"""
    def __init__(self, bot):
        self.bot = bot
	
    COG_EMOJI = "⚒️"
		
    @commands.command(help="Purge a given amount of messages in the current channel")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx : commands.Context, amount : int):
        await ctx.channel.purge(limit=amount)

    @commands.command(help="Ban a user from the current guild")
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx : commands.Context, member : nextcord.Member, *, reason = "Not specified"):
        await member.ban(reason=reason)
        embed = nextcord.Embed(title="Member banned", description=f"Member {member.mention} has been banned for the following reason: {reason}", colour=0xff0000)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Kick a user from the current guild")
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx : commands.Context, member : nextcord.Member, *, reason = "Not specified"):
        await member.kick(reason=reason)
        embed = nextcord.Embed(title="Member kicked", description=f"Member {member.mention} has been kicked for the following reason: {reason}", colour=0xff0000)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

	
    @commands.command(help="Set the slowmode of the current channel")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def slowmode(self, ctx : commands.Context, seconds : int = 0):
        if seconds == 0:
            await ctx.channel.edit(slowmode_delay=0, reason=f"This was done by {ctx.author.display_name} by using the slowmode command.")
            await ctx.send(f'Slowmode has successfully been reset for channel {ctx.channel.mention}')
        else:
            await ctx.channel.edit(slowmode_delay=seconds, reason=f"This was done by {ctx.author.display_name} by using the slowmode command.")
            await ctx.send(f'Slowmode has successfully updated to {seconds} seconds for channel {ctx.channel.mention}')


def setup(bot : commands.Bot):
    bot.add_cog(Mod(bot))
