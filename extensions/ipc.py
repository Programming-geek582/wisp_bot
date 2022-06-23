from nextcord.ext import commands, ipc

class IpcRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ipc.server.route()
    async def get_guild_ids(self, data):
        final = []
        for guild in self.bot.guilds:
            final.append(guild.id)

        return final

    @ipc.server.route()
    async def get_guild_count(self, data):
        return len(self.bot.guilds)

    @ipc.server.route()
    async def get_guild(data):
        guild = self.bot.get_guild(data.guild.id)
        if not guild: return None

        return guild

def setup(bot):
    bot.add_cog(IpcRoutes(bot))