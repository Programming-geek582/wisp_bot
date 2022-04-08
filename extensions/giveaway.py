import nextcord
import datetime
from nextcord.ext import commands

class Giveaway(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gstart(self, ctx : commands.Context, prize : int = None, time : int = None, requirements : nextcord.Role = None, host : nextcord.Member = None, donor : nextcord.Member = None):
        nextcord.utils.time_snowflake()
        embed = nextcord.Embed(
            title=prize, 
            description=f"""Time left: {nextcord.utils.time_snowflake(datetime.datetime)}""",
            colour=0xff0000
        )
        embed.set_author(name="", icon_url="")
        await ctx.send(embed=embed)

def setup(bot : commands.Bot):
    bot.add_cog(Giveaway(bot))