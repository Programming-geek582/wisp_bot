import nextcord
import datetime
import requests
from nextcord.ext import commands

class InDev(commands.Cog, name="indev"):
    'In dev commands'
    
    COG_EMOJI = "👨‍💻"
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def hentai2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/hentai')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def yuri2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/yuri')
        res = r.json()
        embed = nextcord.Embed(title="Yuri", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def solog2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/solog')
        res = r.json()
        embed = nextcord.Embed(title="Solog", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def smug2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/smug')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.is_owner()
    async def feet2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/feet')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def smallboobs2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/smallboobs')
        res = r.json()
        embed = nextcord.Embed(title="Hentai", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.is_owner()
    async def lewdkemo2(self, ctx : commands.Context):
        r = requests.get('https://nekos.life/api/v2/img/lewdkemo')
        res = r.json()
        embed = nextcord.Embed(title="Lewd kemo", colour=0xff0000)
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

        
def setup(bot):
    bot.add_cog(InDev(bot))
