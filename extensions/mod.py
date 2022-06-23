import nextcord, humanfriendly
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
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx : commands.Context, member : nextcord.Member, *, reason = "Not specified"):
        await member.ban(reason=reason)
        embed = nextcord.Embed(title="Member banned", description=f"Member {member.mention} has been banned for the following reason: {reason}", colour=0xff0000)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Kick a user from the current guild")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx : commands.Context, member : nextcord.Member, *, reason = "Not specified"):
        await member.kick(reason=reason)
        embed = nextcord.Embed(title="Member kicked", description=f"Member {member.mention} has been kicked for the following reason: {reason}", colour=0xff0000)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

	
    @commands.command(help="Set the slowmode of the current channel")
    async def slowmode(self, ctx : commands.Context, seconds : int = 0):
        if seconds == 0:
            await ctx.channel.edit(slowmode_delay=0, reason=f"This was done by {ctx.author.display_name} by using the slowmode command.")
            await ctx.send(f'Slowmode has successfully been reset for channel {ctx.channel.mention}')
        else:
            await ctx.channel.edit(slowmode_delay=seconds, reason=f"This was done by {ctx.author.display_name} by using the slowmode command.")
            await ctx.send(f'Slowmode has successfully updated to {seconds} seconds for channel {ctx.channel.mention}')
		
    @commands.command(help="Locks down the given channel(locks the current channel if no channel is given)")
    @commands.has_permissions(manage_guild=True)
    async def lock(self, ctx : commands.Context, channel : nextcord.TextChannel):
        if channel == None:
            channel = ctx.channel

        overwrites = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrites.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
        await ctx.send(f'Locked down {ctx.channel.mention}')

    @commands.command(help="Locks down the given channel(locks the current channel if no channel is given)")
    @commands.has_permissions(manage_guild=True)
    async def unlock(self, ctx : commands.Context):
        overwrites = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrites.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
        await ctx.send(f'Unlocked {ctx.channel.mention}')
		
    @commands.command(help="Locks down the given channel(locks the current channel if no channel is given)")
    @commands.has_permissions(manage_guild=True)
    async def mute(self, ctx : commands.Context, member : nextcord.Member = None, time : str = '10m', *, reason : str = "Not specified"):
        time = humanfriendly.parse_timespan(time)
        embed = nextcord.Embed(title=f"Muted {member.mention}", colour=0xff0000)
        await ctx.send(embed=embed)


def setup(bot : commands.Bot):
    bot.add_cog(Mod(bot))
