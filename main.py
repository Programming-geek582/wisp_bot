import os
import nextcord
import time
import aiohttp
from nextcord.ext import commands

bot = commands.Bot(command_prefix=['wisp ', 'w!', 'w.', '!w'], intents=nextcord.Intents.all(), owner_ids=[837730346874306581, 824236988433039391], case_insensitive=True)

bot.lavalink_nodes = [
	{"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
	{"host": "lava.link", "port": 80, "password": "dismusic"},
	{"host": "lavalink.islantay.tk", "port": 8880, "password": "waifufufufu"}
]

extensions = ['extensions.image','extensions.mod','extensions.owner','extensions.info', 'extensions.handlers', 'extensions.help', 'extensions.minigames', 'extensions.fun', 'dismusic', 'extensions.utils', 'jishaku']

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')
    print(f'Bot guilds count: {len(bot.guilds)}')
    for cog in extensions:
    	try:
	    	bot.load_extension(cog)
	    	print(f'Loaded cog {cog}')
    	except Exception as e:
	    	raise e

@bot.event
async def on_message(message : nextcord.Message):
    if message.author == bot.user:
        return
    
    if message.content.isupper == True:
        if message.author.id == bot.owner_id:
            return
        else:
            await message.reply('Stop sending messages in uppercase nab')
	
    async with aiohttp.ClientSession() as session:
        request = session.get(f"https://some-random-api.ml/chatbot?message={message.content}&key={os.getenv('APIKEY')}")
        response = request.json()

    await message.channel.send(response['response'])
    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
