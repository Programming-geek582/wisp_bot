import nextcord, humanfriendly, traceback
from nextcord.ext import commands

class Buttons(nextcord.ui.View):
    def __init__(self, traceback_, timeout=180):
        self.traceback = traceback_
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Traceback", emoji=None, style=nextcord.ButtonStyle.blurple)
    async def view_traceback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        return await interaction.response.send_message(f"Read the last line for proper info.\n```py\n{self.traceback}\n```", ephemeral=True)

    @nextcord.ui.button(label="Delete", emoji=None, style=nextcord.ButtonStyle.blurple)
    async def delete_message(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.message.delete()
        return await interaction.response.send_message("Message deleted.", ephemeral=True)
		
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
            return
        error = getattr(error, "original", error)
        if isinstance(error, commands.CommandOnCooldown):
            time = humanfriendly.format_timespan(error.retry_after)
            embed = nextcord.Embed(
                title="Sorry",
                description=f"This command is on cooldown. pls try again in {time}",
                colour=0xff0000,
            )
            await ctx.reply(embed=embed)
            return
        if isinstance(error, commands.CommandNotFound):
            print('Cmd not found')
            return

        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"You dont have perms dude, try again with relevant permissions",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.BotMissingPermissions):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"I am missing permissions to do that action so gimme perms",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.BadArgument):
            embed = nextcord.Embed(
                title="Sorry",
                description=f"I could not find a member named {error.argument}. pls mention a member like this. {ctx.author.mention}",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title="Invalid usage",
                description=f"pls try the {ctx.invoked_with} command in the following format.\n\n`wisp {ctx.invoked_with} {ctx.command.signature}`",
                colour=0xff0000
            )
            await ctx.reply(embed=embed)
            return
        if isinstance(error, commands.NSFWChannelRequired):
            pass

        if isinstance(error, commands.ChannelNotReadable):
            await ctx.send(f'I am not able to access the channel {error.argument}. so pls allow me access to admin perms or give me permissions so that i can access it.')
            return
			
        else:
            # unknown error
            embed = nextcord.Embed(title=f"🚫 Command {ctx.command.name} raised an **unknown** error", colour=0xff0000)

            await self.bot.get_channel(966956781718892564).send(embed=embed, view=Buttons("".join(traceback.format_exception(etype=None, value=error, tb=error.__traceback__)), 180))
            await ctx.send('An unknown error occured, reporting to developer')
			
def setup(bot : commands.Bot):
    bot.add_cog(Handlers(bot))