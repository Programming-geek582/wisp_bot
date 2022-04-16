import nextcord
import aiosqlite
from .ticket_view import ticket_create_view
from nextcord.ext import commands

class Tickets(commands.Cog, name="tickets"):
	"""Ticket system for wisp bot"""
	def __init__(self, bot : commands.Bot):
		self.bot = bot

	COG_EMOJI = "📜"
	@commands.Cog.listener()
	async def on_ready():
		async with aiosqlite.connect('tickets.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute('CREATE TABLE IF NOT EXISTS tickets(guild_id INT, category TEXT, counter INT, channel INT)')

		await db.commit()

	@commands.command()
	@commands.cooldown(1, 30, commands.BucketType.user)
	@commands.has_permissions(administrator=True)
	async def tickets(self, ctx : commands.Context):
		async with aiosqlite.connect('tickets.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute('SELECT category, channel FROM tickets WHERE guild_id = ?', (ctx.guild.id,))
				data = await cursor.fetchone()
				if data:
					await cursor.execute('UPDATE tickets SET category = ? AND counter = ? AND channel ? WHERE guild_id = ?', (ctx.channel.category.name, 0, ctx.channel.id, ctx.guild.id))
				else:
					await cursor.execute('INSERT INTO tickets(guild_id, category, counter, channel) VALUES (?, ?, ?, ?)', (ctx.guild.id, ctx.channel.category.name, 0, ctx.channel.id))
		await db.commit()
		await ctx.send('Tickets have successfully setup. now click the button to test out the ticket system', delete_after=10)
		embed = nextcord.Embed(title="Create a ticket", description="Create a ticket to contact the server mods, or to report something or whatever you want.", colour=0xff0000)
		await ctx.send(embed=embed)

def setup(bot : commands.Bot):
	bot.add_cog(Tickets(bot))
