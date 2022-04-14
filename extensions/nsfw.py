import nextcord
import datetime
import aiohttp
from nextcord.ext import commands
from nextcord.ext.commands.cooldowns import BucketType

class NSFW(commands.Cog, name="nsfw"):
    'NSFW commands, type "gif" as the type and it\'ll be animated'
    
    COG_EMOJI = "🔞"
    def __init__(self, bot):
        self.bot = bot

    # ----------------------------------------------------------------------------------------- #
    #  CUSTOM CONTEXT IS NOT USED IN THIS COG CAUSE IT WOULD BREAK THE "COLOR=DOMINANT_COLOR".  #
    # ----------------------------------------------------------------------------------------- #

    @commands.command(aliases=['nsfw_ass', 'ass_nsfw'])
    @commands.is_owner()
    async def ass(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/ass/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/ass/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()

        embed = nextcord.Embed(title="Ass", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['nsfw_ecchi', 'ecchi_nsfw'])
    @commands.is_owner()
    async def ecchi(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/ass/"
        
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/ecchi/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()
   
        embed = nextcord.Embed(title="Ecchi", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['nsfw_ero', 'ero_nsfw'])
    @commands.is_owner()
    async def ero(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/ero/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/ero/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()
            
        embed = nextcord.Embed(title="Ero", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['nsfw_hentai', 'hentai_nsfw'])
    @commands.is_owner()
    async def hentai(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/hentai/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/ero/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()

        embed = nextcord.Embed(title="Hentai", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['maidh', 'nsfw_maid', 'maid_nsfw'])
    @commands.is_owner()
    async def hmaid(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/hmaid/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/hmaid/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()

        embed = nextcord.Embed(title="Maid", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)

    @commands.command(aliases=['nsfw_milf', 'milf_nsfw'])
    @commands.is_owner()
    async def milf(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/milf/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/milf/?gif=True"
            
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()

        embed = nextcord.Embed(title="Milf", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)

    @commands.command(aliases=['nsfw_oppai', 'oppai_nsfw'])
    @commands.is_owner()
    async def oppai(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/oppai/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/oppai/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()

        embed = nextcord.Embed(title="Oppai", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)

    @commands.command(aliases=['nsfw_oral', 'oral_nsfw'])
    @commands.is_owner()
    async def oral(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/oral/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/oral/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()
            
        embed = nextcord.Embed(title="Oral", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)

    @commands.command(aliases=['nsfw_paizuri', 'paizuri_nsfw'])
    @commands.is_owner()
    async def paizuri(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/paizuri/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/paizuri/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()
            
        embed = nextcord.Embed(title="Paizuri", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['nsfw_selfies', 'selfies_nsfw', 'selfie', 'nsfw_selfie', 'selfie_nsfw'])
    @commands.is_owner()
    async def selfies(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/selfie/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/selfie/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()
            
        embed = nextcord.Embed(title="Selfie", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['nsfw_uniform', 'uniform_nsfw'])
    @commands.is_owner()
    async def uniform(self, ctx, type : str=None):
        url = "https://api.waifu.im/nsfw/uniform/"
      
        if str(type).lower() == "gif":
            url = "https://api.waifu.im/nsfw/uniform/?gif=True"
         
        async with aiohttp.ClientSession() as session:
            request = await session.get(url)
            json = await request.json()
            
        embed = nextcord.Embed(title="Uniform", url=json['url'], timestamp=nextcord.utils.utcnow(), color=0xff0000)
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(NSFW(bot))
