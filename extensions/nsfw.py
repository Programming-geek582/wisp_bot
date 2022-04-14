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
    @commands.is_nsfw()
    async def hentai(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/hentai')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def yuri(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/yuri')
        res = r.json()
        embed = nextcord.Embed(title="Yuri", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def solog(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/solog')
        res = r.json()
        embed = nextcord.Embed(title="Solog", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def smug(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/smug')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.is_nsfw()
    async def feet(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/feet')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def smallboobs(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/smallboobs')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/hentai')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

        
def setup(bot):
    bot.add_cog(NSFW(bot))
