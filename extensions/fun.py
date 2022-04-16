import nextcord
import random
import io
import datetime
import aiohttp
from nextcord.ext import commands
from nextcord.ext.commands.cooldowns import BucketType
import praw
import requests

reddit = praw.Reddit(
                    client_id="dMNBCPGr8BgCa6LWhEJbjw",
                    client_secret="mTyZEZPNXw8Y4vO_BpgWXR8-cBUIGQ",
                    username="No_Activity_6143",
                    password="prawvideo",
                    user_agent="pythonpraw"
                )

class Fun(commands.Cog, name="fun"):
    "Fun commands like meme and more"
    COG_EMOJI = "⚽"
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Shows the size of someones pp!", aliases=['banana', 'eggplant', 'egg_plant'])
    async def pp(self, ctx : commands.Context, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        length = random.randint(10, 25)

        embed = nextcord.Embed(title=f"PP Size - {member}", description=f"8{'=' * length}D\n{member.name}'s :eggplant: is {length} cm", colour=0xff0000)

        await ctx.send(embed=embed)

    @commands.command(aliases=['amogus'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def amongus(self, ctx : commands.Context):
        embed = nextcord.Embed(
            title="Among us little mogus", 
            description="""```diff
-⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
-⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
-⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
-⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
-⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
-⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
-⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
-⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
-⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
-⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
-⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
-⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
-⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
-⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
-⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
-⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁
```""", 
            colour=0xff0000
        )
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Shows ascii art of putin")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def putin(self, ctx : commands.Context):
        message = """```diff
-⣿⡟⠛⠻⣿⣿⣿⠟⠛⠛⠻⣿⡟⠛⠛⠛⡟⠛⠛⠛⠛⢿⣿⡟⠛⢻⡿⠛⠻⣿⠿⠛⠻⣿
-⣿⡇⠀⠀⣿⣿⡇⠀⢠⡄⠀⢸⡇⠀⢀⣤⣧⡄⠀⠀⣤⣼⣿⡇⠀⠀⠃⠀⠀⡇⠀⢠⡄⠀⢸⣿
-⣿⡇⠀⠀⣿⣿⡇⠀⢸⠓⠒⢺⡇⠀⠈⠉⣿⡇⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⡇⠀⢸⡇⠀⢸⣿
-⣿⡇⠀⠀⣿⣿⡇⠀⢸⡆⠀⢸⡇⠀⢰⣶⣿⡇⠀⠀⣿⣿⣿⡇⠀⢠⠀⠀⠀⡇⠀⢸⡇⠀⢸⣿
-⣿⡇⠀⠀⣿⣿⣧⡀⠈⠁⠀⢸⡇⠀⠀⠀⢸⡇⠀⠀⣿⣿⣿⡇⠀⢸⡄⠀⢀⣧⡀⠈⠀⢀⣼⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⡷⠏⡍⠀⠀⠨⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⠉⠁⢠⡄⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠑⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣧⠀⠀⡾⠘⠀⠀⠀⠀⠀⠈⢋⡟⠋⠉⢉⣉⠙⠻⣿⣿⠋⣿⣇⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⡄⢀⢷⠀⠀⠀⣀⡀⠀⠀⢸⣿⣦⡀⣤⣴⣶⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣧⠀⠈⠀⠀⠐⠚⣏⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠀⠀⠀⠈⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⢻⣛⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⢤⣸⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢆⠀⠀⠀⠀⠀⠀⠐⠐⠒⣴⣦⣄⣿⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢺⣦⡀⠀⠀⠀⠀⠀⠻⢿⣿⡿⠋⢈⣽⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⢻⣿⣦⣄⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡏⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
-⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣶⣴⣶⣦⣽⣿⣿⣿⣿⣧⠀⠈⠉⠛⠻⢿⣿⣿⣿⣿
-⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠉⠙⠛
-⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡿⡋⠀⢠⣄⣈⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
-⠀⣀⣤⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣄⡀⠀
-⡎⠉⠉⠉⠉⢻⡏⠉⠉⠉⠉⠉⠉⠉⡿⠋⠉⠉⠉⢻⡏⠉⢹⠉⠉⢹⠉⠉⠉⠉⡟⠉⠉⠉⠉⣢
-⡇⠀⠀⡇⠀⢈⡇⠀⠀⣷⡆⠀⢰⣶⡇⠀⠀⡆⠀⢸⡇⠀⠸⠀⠀⢸⠀⠀⢰⣶⡇⠀⠘⢤⣤⣼
-⡇⠀⠀⡀⠀⠘⡇⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⡷⠶⢾⡇⠀⢀⠀⠀⢸⠀⠀⢀⣀⣿⣤⡀⠀⠈⢿
-⡇⠀⠀⠇⠀⠀⡇⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠃⠀⢸⡇⠀⢸⠀⠀⢸⠀⠀⠸⠿⡇⠀⠸⠆⠀⢸
-⠃⢀⢠⡀⣠⣴⣧⣤⣤⣿⣧⣤⣬⣿⣷⣤⣤⣤⣤⣾⣧⣤⣼⣤⣤⣼⣤⣤⣤⣤⣿⣦⣤⣤⡤⠊
		```"""
        await ctx.send(message)

	
    @commands.command(help="Answers with yes or no to your question", aliases=['8ball', 'magicball', 'magic_ball', 'eight_ball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes – definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'send hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Dont count on it.',
                    'My send is no.',
                    'My sources say no',
                    'Outlook not so good.',
                    'Very doubtful.']

        embed = nextcord.Embed(title=f"8ball", description=f"""
Question: {question}
Answer: {random.choice(responses)}
                              """, colour=0xff0000)
        
        await ctx.send(embed=embed)

    @commands.command(help="Tells you if someone is a furry or not")
    async def furrydetector(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        responses = ['is a furry.',
                    'is not a furry.']
        
        await ctx.send(f"{member} {random.choice(responses)}")

    @commands.command(help="Tells you how gay someone is")
    async def gayrate(self, ctx, member : nextcord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
        embed = nextcord.Embed(title=f"Gayrate of {member.name}", description=f"{member} is {random.randint(0, 100)}% gay!", colour=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(help="Generates a random number", aliases=['rm'])
    async def randomnumber(self, ctx, minimum : int=None, maximum : int=None):
        if minimum == None:
            minimum = 1

        if maximum == None:
            maximum = 10

        if maximum > 1000000:
            return await ctx.send("Number cannot be more than `1000000`.")

        number = random.randint(minimum, maximum)

        await ctx.send(f"Randomly generated number between `{minimum}` and `{maximum}`: `{number}`")

    @commands.command(help="Messages you.", aliases=['msg_me'])
    async def msgme(self, ctx, *, content):
        try:
            await ctx.author.send(content)
            await ctx.send("Successfully messaged you.")
            
        except:
            await ctx.send("I couldn't message you, make sure your private messages are enabled.")

    @commands.command(help="Let's you reverse some text")
    async def reverse(self, ctx, *, text):
        embed = nextcord.Embed(title=f"Text reversed", description=f"""
Original text: {text}
<:reverse:879724816834375791> Reversed text: {text[::-1]}
        """, colour=0xff0000)
        
        await ctx.send(embed=embed)

    @commands.command(help="OOF's the person you mentioned", aliases=['commitoof', 'commit_oof'])
    async def oof(self, ctx, member : nextcord.Member=None):
        if member == None or member == ctx.author:
            responses = [f"{ctx.author.name} was killed in Electrical.",
            f"{ctx.author.name} failed math.",
            f"{ctx.author.name} rolled down a large hill.",
            f"{ctx.author.name} cried to death.",
            f"{ctx.author.name} smelt their own socks.",
            f"{ctx.author.name} forgot to stop texting while driving. Don't text and drive, kids.",
            f"{ctx.author.name} said Among Us in a public chat.",
            f"{ctx.author.name} stubbed their toe.",
            f"{ctx.author.name} forgot to grippen their shoes when walking down the stairs.",
            f"{ctx.author.name} wasn't paying attention and stepped on a mine.",
            f"{ctx.author.name} held a grenade for too long.",
            f"{ctx.author.name} got pwned by a sweaty tryhard.",
            f"{ctx.author.name} wore a black shirt in the summer.",
            f"{ctx.author.name} burned to a crisp.",
            f"{ctx.author.name} choked on a chicken nugget.",
            f"{ctx.author.name} forgot to look at the expiration date on the food.",
            f"{ctx.author.name} ran into a wall.",
            f"{ctx.author.name} shook a vending machine too hard.",
            f"{ctx.author.name} was struck by lightning.",
            f"{ctx.author.name} chewed 5 gum.",
            f"{ctx.author.name} ate too many vitamin gummy bears.",
            f"{ctx.author.name} tried to swim in lava. Why would you ever try to do that?"]
            return await ctx.send(f"{random.choice(responses)}")
        
        else:
            responses = [f"{ctx.author.name} exploded {member.name}.",
                        f"{ctx.author.name} shot {member.name}.",
                        f"{ctx.author.name} went ham on {member.name}.",
                        f"{ctx.author.name} betrayed and killed {member.name}.",
                        f"{ctx.author.name} sent {member.name} to Davy Jones' locker.",
                        f"{ctx.author.name} no scoped {member.name}.",
                        f"{ctx.author.name} said no u and killed {member.name}.",
                        f"{ctx.author.name} blew up {member.name} with a rocket.",
                        f"{ctx.author.name} pushed {member.name} off a cliff.",
                        f"{ctx.author.name} stabbed {member.name} to death.",
                        f"{ctx.author.name} slammed {member.name} with a chair.",
                        f"{ctx.author.name} recited a magic spell and killed {member.name}.",
                        f"{ctx.author.name} electrified {member.name}.",
                        f"{member.name} was slain by {ctx.author.name}.",
                        f"{ctx.author.name} burnt {member.name} alive.",
                        f"{ctx.author.name} buried {member.name}.",
                        f"{ctx.author.name} shoved {member.name}'s head underwater for too long.",
                        f"{ctx.author.name} slid a banana peel under {member.name}'s feet. They tripped and died...",
                        f"{ctx.author.name} got a headshot on {member.name}.",
                        f"{ctx.author.name} said a hilarious joke to {member.name} and died.",
                        f"{ctx.author.name} showed old Vicente0670 videos to {member.name} and died of cringe.",
                        f"{ctx.author.name} didn't buy Panda Express for {member.name} and exploded.",
                        f"{ctx.author.name} sent {member.name} to the Nether.",
                        f"{ctx.author.name} tossed {member.name} off an airplane.",
                        f"{ctx.author.name} broke {member.name}'s neck."]

            await ctx.send(f"{random.choice(responses)}")
		
    @commands.command(help="Lets you slap a user")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def roast(self, ctx : commands.Context, member : nextcord.Member):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/slap')
            json = await request.json()
        await ctx.send(json['insult'])
	
    @commands.command(help="Get a random trending meme from reddit")
    async def meme(self, ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []
        top = subreddit.top(limit=50)
        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        embed = nextcord.Embed(title=name, colour=0xff0000)
        embed.set_image(url=url)
        embed.set_author(name=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.reply(embed=embed)
	
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def pokemon(self, ctx : commands.Context, pokemon_name : str = None):
        if pokemon_name == None:
            return await ctx.send('You did not provide a pokemon name to search for.')

        r = requests.get(f'https://some-random-api.ml/pokedex?pokemon={pokemon_name}')
        res = r.json()
        evolution_line = res['family']['evolutionLine']
        species = "\n".join(res['species'])
        abilities = "\n".join(res['abilities'])
        egg_groups = "\n".join(res['egg_groups'])
        embed = nextcord.Embed(
            title=res['name'], 
            colour=0xff0000
        )
        embed.add_field(
            name="Basic info",
            value=f"""Pokemon ID: {res['id']}
            Type: {''.join(res['type'])}
            Height: {res['height']}
            Weight: {res['weight']}
            Base experience: {res['base_experience']}
            Gender: {''.join(res['gender'])}"""
        )
        embed.add_field(
            name="Species",
            value=species
        )
        embed.add_field(
            name="Abilities",
            value=abilities
        )
        embed.add_field(
            name="Egg groups",
            value=egg_groups
        )
        embed.add_field(
            name="Statistics",
            value=f"""Health points: {res['stats']['hp']}
            Attack: {res['stats']['attack']}
            Defence: {res['stats']['defense']}
            Sp attack: {res['stats']['sp_atk']}
            Sp def: {res['stats']['sp_def']}
            Speed: {res['stats']['speed']}
            Total: {res['stats']['total']}"""
        )
        embed.add_field(
            name="Family status",
            value=f"""Evolution Stage: {res['family']['evolutionStage']}
            Evolution line: {evolution_line if evolution_line else "Not found"}
            Generation: {res['generation']}"""
        )
        embed.set_thumbnail(url=res['sprites']['animated'])
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)
	
def setup(bot):
    bot.add_cog(Fun(bot))
