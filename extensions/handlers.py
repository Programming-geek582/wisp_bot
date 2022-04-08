import nextcord
from nextcord.ext import commands

class Handlers(commands.Cog, name="Handlers"):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx : commands.Context, error):
        if isinstance(error, commands.NotOwner):
            embed = nextcord.Embed(
                title="Sorry",
                description="This command is a developer only command. you cannot use it without prior authentication from my owner",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)
        
        if isinstance(error, commands.CommandOnCooldown):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"This command is on cooldown. pls try again in {int(error.retry_after)} seconds",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)

        if isinstance(error, commands.CommandNotFound):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"Command {ctx.invoked_with} was not found",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"You dont have perms dude, try again with relevant permissions",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"I am missing the {str(','.join(error.missing_permissions))} permissions",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"I could not find a member named {error.argument}. pls mention a member like this. {ctx.author.mention}",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)

        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title="Invalid usage",
                description=f"pls try the {ctx.invoked_with} command in the following format.\n\n`wisp {ctx.invoked_with} {ctx.command.signature}`",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)
			
        else:
            raise error
def setup(bot : commands.Bot):
    bot.add_cog(Handlers(bot))