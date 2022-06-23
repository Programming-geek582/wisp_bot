import os
import nextcord
from dashboard import keep_alive
from nextcord.ext import commands, ipc

class WispBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ipc = ipc.Server(self, secret_key="werkzeug", host="0.0.0.0")
        
    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("IPC is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)
		
bot = WispBot(command_prefix=['wisp ', 'w!', 'w.', '!w'], intents=nextcord.Intents.all(), owner_ids=[837730346874306581, 824236988433039391, 764795494832537600], case_insensitive=True)

bot.lavalink_nodes = [
    {"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
    {"host": "lava.link", "port": 80, "password": "dismusic"},
    {"host": "lavalink.islantay.tk", "port": 8880, "password": "waifufufufu"}
]

extensions = ['extensions.image','extensions.mod','extensions.owner','extensions.info', 'extensions.help', 'extensions.minigames', 'extensions.fun', 'dismusic', 'extensions.utils', 'jishaku', 'extensions.nsfw', 'extensions.ticket', 'extensions.indev', 'extensions.config', 'extensions.special', 'extensions.handlers', 'extensions.btncalc', 'extensions.giveaway', 'extensions.ipc']

@bot.event
async def on_member_join(member: nextcord.Member):
    pass

@bot.event
async def on_member_remove(member: nextcord.Member):
    pass

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')
    print(f'Bot guilds count: {len(bot.guilds)}')
    for cog in extensions:
        try:
            bot.load_extension(cog)
            print(f'{cog} has been loaded up')
        except Exception as e:
            raise e
#
@bot.event
async def on_message(message : nextcord.Message):
    if message.author == bot.user:
        return
    
    if message.content.isupper == True:
        if message.author.id == bot.owner_id:
            return
        else:
            await message.reply('Stop sending messages in uppercase nab')

    await bot.process_commands(message)

def run():
    bot.ipc.start()
    bot.loop.create_task(keep_alive.app.run_task(host="0.0.0.0"))
    bot.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    run()