import nextcord
import humanfriendly
import datetime
from nextcord.ext import commands

class Giveaway(commands.Cog, name="giveaway"):
	"""Giveaway system of wisp bot"""
	COG_EMOJI = "🎉"
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def gstart(self, ctx : commands.Context, prize : str, time : str, winners : int = 1):
		time = humanfriendly.parse_timespan(time)
		time = nextcord.utils.utcnow() + datetime.timedelta(time)
		embed = nextcord.Embed(
			title=prize,
			description=f"""React with :tada: to join
			Ends in: {nextcord.utils.format_dt(time, style="R")} ( {nextcord.utils.format_dt(time)} )
			Winners: {winners}
			Hosted by: {ctx.author.mention}""",
			color=0xff0000
		)
		await ctx.send(f'New gaw in {ctx.guild.name}', embed=embed)

def setup(bot : commands.Bot):
	bot.add_cog(Giveaway(bot))