import nextcord, aiohttp, urllib
from .contact_view import DevContactView
from nextcord.ext import commands

class Utils(commands.Cog, name="utility"):
    """Utility extension for wisp bot"""
    COG_EMOJI = "🔨"
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def calc(self, ctx : commands.Context, sum : str = None):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://api.mathjs.org/v4?expr={urllib.parse.quote(sum)}') as request:
                    json = await request.json()
			
            embed = nextcord.Embed(title=json['result'], description="Calculated in 0.1 seconds", colour=0xff0000)
            embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
            await ctx.reply(embed=embed)
        except commands.MissingRequiredArgument:
            embed = nextcord.Embed(title="Invalid usage", description="Pls try the command again in the following format.\n\n`wisp calculate <sum>`", colour=0xff0000)
            embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
			
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def policy(self, ctx : commands.Context, sum : str = None):
        embed = nextcord.Embed(title="Wisp bot privary policy", description="Dont worry we dont store anything about you or your information except the guild id and stuff in the ticket system")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 36000, commands.BucketType.user)
    async def contact_dev(self, ctx : commands.Context):
        await ctx.send('Press the below button to open up the developer contact form', view=DevContactView(ctx))

    @commands.command()
    @commands.is_owner()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def message(self, ctx : commands.Context, user : nextcord.User, *, message = None):
        dev = self.bot.get_user(837730346874306581)
        embed = nextcord.Embed(
            title="Response from developer", 
            description=message, 
            colour=0xff0000
        )
        embed.set_footer(text=dev.name, icon_url=dev.display_avatar)
        await user.send(embed=embed)
        embed = nextcord.Embed(title="Message sent", description=f"Your message was successfully delivered to {user}. awaiting their response", colour=0xff0000)
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def banner(self, ctx : commands.Context, member : nextcord.Member):
        if not member.banner:
            return await ctx.send(f'Member {member.mention} does not have a banner')
        else:
            embed = nextcord.Embed(title=f"{member.display_name}'s banner", colour=0xff0000)
            embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
            embed.set_image(url=member.banner.url)
            await ctx.send(embed=embed)

def setup(bot : commands.Bot):
    bot.add_cog(Utils(bot))