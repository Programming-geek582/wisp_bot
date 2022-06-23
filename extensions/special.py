import nextcord
from .accept_decline_view import confirm_view as accept_decline_view
from nextcord.ext import commands

class Suggest(commands.Cog, name="suggest"):
    """Suggest system of wisp bot"""
    COG_EMOJI = "📧"
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def suggest(self, ctx : commands.Context, *, suggestion : str = None):
        if suggestion == None:
            await ctx.command.reset_cooldown()
            return await ctx.send('Argument `suggestion` cannot be none')

        embed = nextcord.Embed(
            title="Suggestion system",
            description=f"Your suggestion `{suggestion}` has been submitted. we will soon know if it was accepted or declined.",
            colour=0xff0000
        )
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

        embed = nextcord.Embed(
            title=suggestion,
            description=f"Suggestion submitted by {ctx.author}.",
            colour=0xff0000
        )
        embed.add_field(name="Status", value="Pending")
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await self.bot.get_channel(943178367837040680).send(embed=embed, view=accept_decline_view(ctx, suggestion=suggestion))

def setup(bot : commands.Bot):
    bot.add_cog(Suggest(bot))