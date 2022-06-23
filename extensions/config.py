import nextcord
import aiosqlite
import time
from nextcord.ext import commands

class Configuration(commands.Cog, name="configuration"):
	"""Configuration system"""
	def __init__(self, bot : commands.Bot):
		self.bot = bot

	COG_EMOJI = "📜"

	@commands.command()
	@commands.cooldown(1, 30, commands.BucketType.user)
	@commands.has_permissions(manage_guild=True)
	async def setWelcome(self, ctx : commands.Context):
		message = await ctx.send('Hello there!. i see that you have invoked the wisp welcome configuration command. so lets proceed on with the questions. the max time you got to answer a question is 30 seconds. lets get started.')
		
		time.sleep(3)
		await message.edit('Alr, config system is loaded up, so now its the first question.')

		time.sleep(2)
		await message.edit('What should be the welcome channel?')
		# get input
		welcome_channel = await self.bot.wait_for('message', timeout=30, check=lambda m: m.author.id == ctx.author.id)
		# convert it into a discord text channel object
		wlcm_channel = await commands.TextChannelConverter().convert(ctx, welcome_channel.content)
		await ctx.send('Please enter the welcome message below. use `{}` where you wanna mention the member.')
		# welcome message
		welcome_msg = await self.bot.wait_for('message', timeout=30, check=lambda m: m.author.id == ctx.author.id)
		# get input
		await ctx.send('Please enter the leave channel below.')
		leave_channel = await self.bot.wait_for('message', timeout=30, check=lambda m: m.author.id == ctx.author.id)
		# convert it into a discord text channel object
		leave_chnl = await commands.TextChannelConverter().convert(ctx, leave_channel.content)
		# leave message
		await ctx.send('Please enter the leave message below. use `{}` where you wanna mention the member.')
		leave_msg = await self.bot.wait_for('message', timeout=30, check=lambda m: m.author.id == ctx.author.id)
		async with aiosqlite.connect('bot.db') as db:
			async with db.cursor() as cursor:
				await cursor.execute('CREATE TABLE IF NOT EXISTS guilds(guild_id INT, welcome_channel TEXT, welcome_message TEXT, leave_channel TEXT, leave_message TEXT)')
				await cursor.execute('SELECT welcome_channel, welcome_message, leave_message, leave_channel FROM guilds WHERE guild_id = ?', (ctx.guild.id,))
				data = await cursor.fetchone()
				if data:
					await cursor.execute('UPDATE guilds SET welcome_channel = ?, welcome_message = ?, leave_channel = ?, leave_message = ? WHERE guild_id = ?', (wlcm_channel.id, wlcm_channel.content, leave_chnl.id, leave_msg.content,))
				else:
					await cursor.execute('INSERT INTO guilds(guild_id, welcome_channel, welcome_message, leave_channel, leave_message) VALUES (?, ?, ?, ?, ?)', (ctx.guild.id, wlcm_channel.id, welcome_msg.content, leave_chnl.id, leave_msg.content,))
			await db.commit()
		await ctx.send('Welcome system has been successfully setup. all thats left to do is test. ')

def setup(bot : commands.Bot):
	bot.add_cog(Configuration(bot))
