import nextcord
import datetime
import requests
from nextcord.ext import commands
from nextcord.ext.commands.cooldowns import BucketType

class NSFW(commands.Cog, name="nsfw"):
    'NSFW commands, type "gif" as the type and it\'ll be animated'
    
    COG_EMOJI = "🔞"
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def hentai(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/hentai')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(NSFW(bot))
