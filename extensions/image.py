import nextcord
import aiohttp
import io
import json
from nextcord.ext import commands
from nextcord.ext.commands import BucketType

class Image(commands.Cog, name="image"):
    """Fun image commands for any user to use"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    COG_EMOJI = "🖼️"

		
    @commands.command(help="🐶 Shows a picture of a dog and a random fact about dogs")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Woof", 
            url=pictureJson['link'],
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="🐼 Shows a picture of a panda and a random fact about pandas")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/panda')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Panda!", 
            url=pictureJson['link'],
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=embed)

    @commands.command(help="🦊 Shows a picture of a fox and a random fact about foxes")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/fox')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Fox!", 
            url=pictureJson['link'], 
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=embed)

    @commands.command(help="🐦 Shows a picture of a bird and a random fact about birds")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/bird')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/bird')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Bird!", 
            url=pictureJson['link'], 
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="🐨 Shows a picture of a koala and a random fact about koalas")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def koala(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/koala')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/koala')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Koala!", 
            url=pictureJson['link'], 
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=embed)

    @commands.command(help="🦘 Shows a picture of a kangaroo and a random fact about kangaroos")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def kangaroo(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/kangaroo')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/kangaroo')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Kangaroo!", 
            url=pictureJson['link'], 
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=embed)

    @commands.command(help="🦝 Shows a picture of a raccoon and a random fact about raccoons")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def raccoon(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/racoon')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/racoon')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Racoon!", 
            url=pictureJson['link'],
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=embed)

    @commands.command(help="🐳 Shows a picture of a whale and a random fact about whales", aliases=['urmom', 'ur_mom', 'yourmom', 'your_mom'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def whale(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/whale')
            pictureJson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/whale')
            factJson = await request2.json()

        embed = nextcord.Embed(
            title="Whale!", 
            url=pictureJson['link'], 
            description=factJson['fact'],
            colour=0xff0000
        )
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)



    @commands.command(help="Shows a picture of a pikachu")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def pikachu(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/pikachu')
            pictureJson = await request.json()

        embed = nextcord.Embed(
            title="Pikachu!", url=pictureJson['link'], colour=0xff0000)
        embed.set_image(url=pictureJson['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Let's you hug someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def hug(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't hug yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/hug')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} hugged {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Let's you pat someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def pat(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't pat yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/pat')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} patted {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you kiss someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def kiss(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't kiss yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/kiss')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} kissed {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you pat someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def pat(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't pat yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/pat')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} patted {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you lick someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def lick(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't lick yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/lick')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} licked {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you bonk someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def bonk(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't bonk yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/bonk')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} bonked {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you yeet someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def yeet(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't yeet yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/yeet')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} yeeted {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you wave at someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def wave(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't hug yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/wave')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} waved at {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you high five someone!", aliases=['high_five'])
    @commands.cooldown(1, 5, BucketType.member)
    async def highfive(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't high five yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/highfive')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} high fived {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Let's you bite someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def bite(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't bite yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/bite')
            json = await request.json()

        embed = nextcord.Embed(title=f"{ctx.author.name} bit {member.name}")
        embed.set_image(url=json['url'])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
        await ctx.send(embed=embed)

    @commands.command(help="Sends a image of the member you mention but triggered")
    @commands.cooldown(1, 5, BucketType.member)
    async def triggered(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar.with_format("png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "triggered.gif")
        
                    embed = nextcord.Embed(title=f"{member.name} is triggered", colour=0xff0000)
                    embed.set_image(url="attachment://triggered.gif")
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)        
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['horny_license', 'license_horny'])
    @commands.cooldown(1, 5, BucketType.member)
    async def horny(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/horny?avatar={member.avatar.with_format("png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "horny.png")

                    embed = nextcord.Embed(title=f"{member.name} has the license to be horny", colour=0xff0000)
                    embed.set_image(url="attachment://horny.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['go_to_jail', 'in_jail'])
    @commands.cooldown(1, 5, BucketType.member)
    async def jail(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/jail?avatar={member.avatar.with_format("png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "jail.png")

                    embed = nextcord.Embed(title=f"{member.name} has been sent to jail for 69420 years", colour=0xff0000)
                    embed.set_image(url="attachment://jail.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['waste'])
    @commands.cooldown(1, 5, BucketType.member)
    async def wasted(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar.with_format("png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "wasted.png")

                    embed = nextcord.Embed(title=f"WASTED.", colour=0xff0000)
                    embed.set_image(url="attachment://wasted.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['pride', 'gay'])
    @commands.cooldown(1, 5, BucketType.member)
    async def rainbow(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar.with_format("png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "gay.png")
                    embed = nextcord.Embed(title=f"{member.name} is now gay")
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
                    embed.set_image(url="attachment://gay.png")
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny")
    @commands.cooldown(1, 5, BucketType.member)
    async def glass(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/glass?avatar={member.avatar.with_format("png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "glass.png")

                    embed = nextcord.Embed(title=f"{member.name} is now **glass**")
                    embed.set_image(url="attachment://glass.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)                    
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Waifu", hidden=True)
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def waifu(self, ctx):
        async with aiohttp.ClientSession() as session:
            waifu = await session.get('https://api.waifu.pics/nsfw/waifu')
            json = await waifu.json()
            embed = nextcord.Embed(title=f"Waifu", colour=0xff0000)
            embed.set_image(url=json['url'])
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)                    
            await ctx.send(embed=embed)

    @commands.command(help="Neko")
    @commands.is_nsfw()
    @commands.cooldown(1, 5, BucketType.member)
    async def neko(self, ctx):
        async with aiohttp.ClientSession() as session:
            waifu = await session.get('https://api.waifu.pics/nsfw/neko')
            json = await waifu.json()
            embed = nextcord.Embed(title=f"Neko", colour=0xff0000)
            embed.set_image(url=json['url'])
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)                    
            await ctx.send(embed=embed)

    @commands.command(help="Tweets the given message")
    @commands.cooldown(1, 5, BucketType.member)
    async def tweet(self, ctx, *, comment : str = None):
        if comment == None:
            return await ctx.send('Pls say something to send in the tweet')
        if member == None:
            member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/tweet?avatar={member.avatar.with_format("png")}&username={member.name}&displayname={member.display_name}&comment={comment}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = nextcord.File(fp, "tweet.png")

                    await ctx.send(file=file)
		
def setup(bot: commands.Bot):
    bot.add_cog(Image(bot))
