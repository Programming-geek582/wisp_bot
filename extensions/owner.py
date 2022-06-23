import nextcord
from jishaku.codeblocks import codeblock_converter
from nextcord.ext import commands

class Owner(commands.Cog, name="owner"):
    """Owner commands for owner only nabs"""
    def __init__(self, bot : commands.Bot):
        self.bot : commands.Bot = bot
        self.jishaku = bot.get_cog("jishaku")

    COG_EMOJI = "👑"

    @commands.command(name="toggle", help="Enable or disable a command!")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)

        if command is None:
            embed = nextcord.Embed(title="ERROR", description="I can't find a command with that name!", color=0xff0000)
            await ctx.send(embed=embed)

        elif ctx.command == command:
            embed = nextcord.Embed(title="ERROR", description="You cannot disable this command.", color=0xff0000)
            await ctx.send(embed=embed)

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            embed = nextcord.Embed(title="Toggle", description=f"I have {ternary} {command.qualified_name} for you!", color=0xff00c8)
            await ctx.send(embed=embed)

    @commands.command(help="Spamping a given user")
    @commands.is_owner()
    async def spamping(self, ctx, member : nextcord.Member, count : int = 1):
        counter = 0
        while counter < count:
            counter += 1
            await ctx.send(member.mention)

    @commands.command(help="Load a cog")
    @commands.is_owner()
    async def load(self, ctx : commands.Context, cog_name : str = None):
        try:
            self.bot.load_extension(cog_name)
            await ctx.reply('Loaded cog {}'.format(cog_name))
        except Exception as e:
            print(e)

    @commands.command(help="Unload a cog")
    @commands.is_owner()
    async def unload(self, ctx : commands.Context, cog_name : str = None):
        try:
            self.bot.unload_extension(cog_name)
            await ctx.reply('Unoaded cog {}'.format(cog_name))
        except Exception as e:
            print(e)
	
    @commands.command(help="Reload a given cog")
    @commands.is_owner()
    async def reload(self, ctx : commands.Context, cog_name : str = None):
        try:
            self.bot.reload_extension(f"{cog_name}")
            await ctx.reply('Reloaded cog {}'.format(cog_name))
        except Exception as e:
            print(e)

    @commands.command(name="eval")
    async def _eval(self, ctx, *, code: codeblock_converter):
        await ctx.invoke(self.jishaku.jsk_python, argument=code)
				
def setup(bot : commands.Bot):
    bot.add_cog(Owner(bot))