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
		async with aiosqlite.connect('tickets.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute('CREATE TABLE IF NOT EXISTS tickets(guild_id INT, category TEXT, counter INT, channel INT, support_role_id INT)')
				await cursor.execute('SELECT category, channel, counter FROM tickets WHERE guild_id = ?', (ctx.guild.id,))
				data = await cursor.fetchone()
				if data:
					await cursor.execute('UPDATE tickets SET category = ?, counter = ?, channel = ?, support_role_id = ? WHERE guild_id = ?', (ctx.channel.category.name, data[2], ctx.channel.id, support_role_id.id, ctx.guild.id,))
				else:
					await cursor.execute('INSERT INTO tickets(guild_id, category, counter, channel, support_role_id) VALUES (?, ?, ?, ?, ?)', (ctx.guild.id, ctx.channel.category.name, 0, ctx.channel.id, support_role_id.id,))
			await db.commit()
		await ctx.send('Tickets have successfully setup. now click the button to test out the ticket system', delete_after=2)
		embed = nextcord.Embed(title="Create a ticket", description="Create a ticket to contact the server mods, or to report something or whatever you want.", colour=0xff0000)
		await ctx.send(embed=embed, view=ticket_create_view())

def setup(bot : commands.Bot):
	bot.add_cog(Tickets(bot))
