import nextcord, random, akinator
from helpers.tictactoe import TicTacToe, LookingToPlay
from nextcord.ext import commands, activities

class MiniGames(commands.Cog, name="games"):
    """games cog for wisp bot"""
    COG_EMOJI = "🕹️"
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["aki"], help="Play a game of akinator")
    async def akinator(self, ctx : commands.Context):
        await ctx.send("Akinator is here to guess!")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["yes", "no", "probably", "back"]
        try:
            aki = akinator.Akinator()
            q = aki.start_game()
            while aki.progression <= 1000:
                embed = nextcord.Embed(
                    title=q, 
                    description="""Your answer(yes/no/probably/back):""", 
                    colour=0xff0000
                )
                embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)
                msg = await self.bot.wait_for("message", check=check)
                if msg.content.lower() == "back":
                    try:
                        q = aki.back()
                    except akinator.CantGoBackAnyFurther as e:
                        await ctx.send(e)
                        continue
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except akinator.InvalidAnswerError as e:
                        await ctx.send(e)
                        continue
            aki.win()
            embed = nextcord.Embed(
                title=f"It's {aki.first_guess['name']}", 
                description=f"""{aki.first_guess['description']}!
                Was i correct?(yes/no)""", 
                colour=0xff0000
            )
            embed.set_image(url=aki.first_guess['absolute_picture_path'])
            embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            correct = await self.bot.wait_for("message", check=check)
            if correct.content.lower() == "y":
                await ctx.send("Yay. i win.")
            else:
                await ctx.send("Oof. you win. i suck lol")
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=["poke"], help="Play poker. boost locked")
    async def poker(self, ctx : commands.Context, voice_channel : nextcord.VoiceChannel):
	    if ctx.author.premium_since:
	    	invite_link = await voice_channel.create_activity_invite(activities.Activity.poker)
	    	await ctx.send(invite_link)

    @commands.command(aliases=["betray"], help="Play betrayel")
    async def betrayel(self, ctx : commands.Context, voice_channel : nextcord.VoiceChannel):
    	try:
    		invite_link = await voice_channel.create_activity_invite(activities.Activity.betrayal)
	    	await ctx.send(invite_link)
    	except Exception as e:
    		raise e
			
    @commands.command(
        help="Starts a Tic-Tac-Toe game",
        aliases=['ttt', 'tic'])
    async def tictactoe(self, ctx: commands.Context, user : nextcord.Member):
        embed = nextcord.Embed(description=f"🔎 {ctx.author.name} is looking to play Tic-Tac-Toe!")

        player1 = ctx.author
        view = LookingToPlay(timeout=120, user=user)
        view.ctx = ctx
        view.message = await ctx.send(embed=embed, view=view)
        await view.wait()
        player2 = view.value

        if player2:
            starter = random.choice([player1, player2])
            ttt = TicTacToe(ctx, player1, player2, starter=starter)
            ttt.message = await view.message.edit(content=f'#️⃣ {starter.name} goes first', view=ttt, embed=None)
            await ttt.wait()
			
def setup(bot):
    bot.add_cog(MiniGames(bot))
