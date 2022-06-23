import nextcord
import aiosqlite
from .ticket_view import ticket_create_view
from nextcord.ext import commands

class Tickets(commands.Cog, name="tickets"):
	"""Ticket system for wisp bot"""
	def __init__(self, bot : commands.Bot):
		self.bot = bot

	COG_EMOJI = "📜"
	@commands.command()
	@commands.cooldown(1, 30, commands.BucketType.user)
	@commands.has_permissions(administrator=True)
	async def tickets(self, ctx : commands.Context, support_role_id : nextcord.Role = None):
		if support_role_id == None:
			await ctx.send('Sorry but support role is a must')

		await ctx.send('Tickets have successfully setup. now click the button to test out the ticket system', delete_after=2)
		embed = nextcord.Embed(title="Create a ticket", description="Create a ticket to contact the server mods, or to report something or whatever you want.", colour=0xff0000)
		await ctx.send(embed=embed, view=ticket_create_view())

def setup(bot : commands.Bot):
	bot.add_cog(Tickets(bot))
