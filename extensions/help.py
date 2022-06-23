import os
import random
import difflib
import typing
import nextcord
import contextlib

from nextcord.ui import Button
from nextcord import Interaction
from nextcord.ext import commands
from helpers import paginator as paginator
from helpers import errors


def reading_recursive(root: str, /) -> int:
    for x in os.listdir(root):
        if os.path.isdir(x):
            yield from reading_recursive(root + "/" + x)
        else:
            if x.endswith((".py", ".c")):
                with open(f"{root}/{x}") as r:
                    yield len(r.readlines())


def count_python(root: str) -> int:
    return sum(reading_recursive(root))


class VoteButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Button(emoji="<:dbl:757235965629825084>", label="top.gg", url="https://top.gg/bot/760179628122964008"))


class HelpCentre(nextcord.ui.View):
    def __init__(self, ctx: commands.Context, other_view: nextcord.ui.View):
        super().__init__()
        self.embed = None
        self.ctx = ctx
        self.other_view = other_view

    @nextcord.ui.button(label="Go Back", emoji="🏠", style=nextcord.ButtonStyle.blurple)
    async def go_back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.edit_message(embed=self.embed, view=self.other_view)
        self.stop()

    async def start(self, interaction: nextcord.Interaction):
        colors = [0x910023, 0xA523FF]
        color = random.choice(colors)

        embed = nextcord.Embed(title=f"Here's a guild on how to use the help menu", description=f"""
`<argument>`
This means that the argument is **required**.
`[argument]`
This means that the argument is **optional**.
`[argument=\"default\"]`
This means that the argument is **optional** and has a default value.
**Do not use these brackets when running a command.**
**They're only there to indicate if the argument is required or not.**
                              """, color=color)

        embed.set_footer(text=f"To continue browsing the help menu, press the \"Go back\" button.")

        self.embed = interaction.message.embeds[0]
        self.add_item(nextcord.ui.Button(label="Support server", emoji="❓", url="https://nextcord.gg/MrBcA6PZPw"))
        self.add_item(nextcord.ui.Button(label="Invite me", emoji="<:invite:895688440639799347>", url="https://nextcord.com/oauth2/authorize?client_id=760179628122964008&scope=applications.commands+bot&permissions=549755813887"))

        await interaction.response.edit_message(embed=embed, view=self)

    async def interaction_check(self, interaction: Interaction):
        if interaction.user and interaction.user == self.ctx.author:
            return True
        await interaction.response.defer()
        return False


class NewsCentre(nextcord.ui.View):
    def __init__(self, ctx: commands.Context, other_view: nextcord.ui.View):
        super().__init__()
        self.embed = None
        self.ctx = ctx
        self.other_view = other_view

    @nextcord.ui.button(label="Go Back", emoji="🏠", style=nextcord.ButtonStyle.blurple)
    async def go_back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.edit_message(embed=self.embed, view=self.other_view)
        self.stop()

    async def start(self, interaction: nextcord.Interaction):
        colors = [0x910023, 0xA523FF]
        color = random.choice(colors)

        embed = nextcord.Embed(title=f"Latest news", description=f"""
__**BIG NEWS**__
The bot ticket system is not ready for production but i will be fixing it soon + button component roles,
verification system and so much more coming up
__**:wave: New welcoming system (<t:1637247577:R>)**__
With this you can welcome new members that join your server!
Do **{self.ctx.prefix}help setWelcome** for more info.
                              """, color=color)

        embed.set_footer(text=f"To continue browsing the help menu, press the \"Go back\" button.")

        self.embed = interaction.message.embeds[0]
        # self.add_item(nextcord.ui.Button(label="Invite me", emoji="<:invite:895688440639799347>", url="https://nextcord.com/oauth2/authorize?client_id=760179628122964008&scope=applications.commands+bot&permissions=549755813887"))
        # self.add_item(nextcord.ui.Button(label="Vote on top.gg", emoji="<:dbl:757235965629825084>", url="https://top.gg/bot/760179628122964008"))

        await interaction.response.edit_message(embed=embed, view=self)

    async def interaction_check(self, interaction: Interaction):
        if interaction.user and interaction.user == self.ctx.author:
            return True
        await interaction.response.defer()
        return False


class HelpView(nextcord.ui.View):
    def __init__(self, ctx: commands.Context, usable_commands, data: typing.Dict[commands.Cog, typing.List[commands.Command]]):
        super().__init__()
        self.ctx = ctx
        self.usable_commands = usable_commands
        self.data = data
        self.bot = ctx.bot
        self.main_embed = self.build_main_page()
        self.current_page = 0
        self.message = None
        self.embeds: typing.List[nextcord.Embed] = [self.main_embed]

    @nextcord.ui.select(placeholder="Select a category...", row=0)
    async def category_select(self, select: nextcord.ui.Select, interaction: nextcord.Interaction):
        if select.values[0] == "index":
            self.current_page = 0
            self.embeds = [self.main_embed]
            self._update_buttons()
            return await interaction.response.edit_message(embed=self.main_embed, view=self)
        cog = self.bot.get_cog(select.values[0])
        if not cog:
            return await interaction.response.send_message('Somehow, that category was not found? 🤔')
        else:
            self.embeds = self.build_embeds(cog)
            self.current_page = 0
            self._update_buttons()
            return await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)


    def build_embeds(self, cog: commands.Cog):
        colors = [0x910023, 0xA523FF, 0xff0000]
        color = random.choice(colors)

        embeds = []
        cog_commands = cog.get_commands()
        embed = nextcord.Embed(title=f"{str(cog.qualified_name).title()} commands [{len(cog_commands)}]", description=f"{cog.description if cog.description else 'No description provided...'[0:1024]}", color=color, timestamp=nextcord.utils.utcnow())

        for cmd in cog_commands:
            embed.add_field(name=f"{cmd.name} {cmd.signature}", value=f"{cmd.help if cmd.help else 'No help provided...'[0:1024]}", inline=False)
            embed.set_footer(text="For info on a command, do help <command>")

            if len(embed.fields) == 5:
                embeds.append(embed)
                embed = nextcord.Embed(title=f"{str(cog.qualified_name).title()} commands [{len(cog_commands)}]", description=cog.description or "No description provided", color=color, timestamp=nextcord.utils.utcnow())

        if len(embed.fields) > 0:
            embeds.append(embed)

        return embeds


    def build_select(self):
        self.category_select: nextcord.ui.Select
        self.category_select.options = []
        self.category_select.add_option(label="Main page", value="index", emoji="🏠")

        for cog, comm in self.data.items():
            if not comm:
                continue

            emoji = getattr(cog, "COG_EMOJI", None)
            label = cog.qualified_name
            brief = cog.__doc__

            self.category_select.add_option(label=label, value=label, emoji=emoji, description=brief)


    def build_main_page(self):

        embed = nextcord.Embed(title="Help menu", description=f"""
Hello there! I'm **Wisp Bot**. Welcome to the help menu.
         """, colour=0xff0000)

        embed.add_field(name=f"**Getting help**", value=f"""
Use **wisp help <command>** for more info on a command.
There's also **wisp help <command> [sub-command]**.
Use **wisp help <category>** for more info on a category.
You can also use the dropdown below to select a category.
        """, inline=False)

        embed.add_field(name=f"**Getting support**", value=f"""
To get help, you can join my [support server](https://discord.gg/UufQX8C8).
You can also send me a DM if you prefer to.
        """, inline=False)

        embed.add_field(name=f"**Wait a minute.. Who are you?**", value=f"""
I'm a multipurpose discord bot created by Programming geek#5593.
You can use me to moderate your server, play music,
manipulate images and way more!
I've been on discord since {nextcord.utils.format_dt(self.ctx.me.created_at)} ({nextcord.utils.format_dt(self.ctx.me.created_at, style='R')})
I have **{len(self.bot.commands)}** commands.
But you can only use **{self.usable_commands}** of those in this server.
        """, inline=False)

        embed.add_field(name=f"**Important news**", value=f"""
CLICK THE NEWS BUTTON!!!
        """, inline=False)

        return embed

    @nextcord.ui.button(label="Help", emoji="❓", style=nextcord.ButtonStyle.blurple, row=1)
    async def help(self, button: Button, interaction: Interaction):
        view = HelpCentre(self.ctx, self)
        await view.start(interaction)

    @nextcord.ui.button(emoji="<:previous:921408043470688267>", style=nextcord.ButtonStyle.gray, row=1)
    async def previous(self, button: Button, interaction: Interaction):
        self.current_page -= 1
        self._update_buttons()
        await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    @nextcord.ui.button(emoji="<:close:921408051091759114>", style=nextcord.ButtonStyle.red, row=1)
    async def delete(self, button: Button, interaction: Interaction):
        await interaction.message.delete()
        if self.ctx.channel.permissions_for(self.ctx.me).manage_messages:
            await self.ctx.message.delete()

    @nextcord.ui.button(emoji="<:next:921408056766636073>", style=nextcord.ButtonStyle.gray, row=1)
    async def next(self, button: Button, interaction: Interaction):
        self.current_page += 1
        self._update_buttons()
        await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    @nextcord.ui.button(label="News", emoji="📰", style=nextcord.ButtonStyle.blurple, row=1)
    async def news(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        view = NewsCentre(self.ctx, self)
        await view.start(interaction)

    def _update_buttons(self):
        page = self.current_page
        total = len(self.embeds) - 1
        self.next.disabled = page == total
        self.previous.disabled = page == 0

    async def interaction_check(self, interaction: Interaction) -> bool:
        if interaction.user and interaction.user == self.ctx.author:
            return True
        await interaction.response.defer()
        return False

    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    async def start(self):
        self.build_select()
        self._update_buttons()
        self.message = await self.ctx.send(embed=self.main_embed, view=self)


class GeneralView(nextcord.ui.View):
    def __init__(self, ctx: commands.Context):
        super().__init__()
        self.ctx = ctx
        self.bot = ctx.bot
        self.message = None

    @nextcord.ui.button(label="Help", emoji="❓", style=nextcord.ButtonStyle.blurple, row=1)
    async def help(self, button: Button, interaction: Interaction):
        view = HelpCentre(self.ctx, self)
        await view.start(interaction)

    @nextcord.ui.button(emoji="🗑️", style=nextcord.ButtonStyle.red, row=1)
    async def delete(self, button: Button, interaction: Interaction):
        await interaction.message.delete()
        if self.ctx.channel.permissions_for(self.ctx.me).manage_messages:
            await self.ctx.message.delete()

    @nextcord.ui.button(label="News", emoji="📰", style=nextcord.ButtonStyle.blurple, row=1)
    async def news(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        view = NewsCentre(self.ctx, self)
        await view.start(interaction)

    async def interaction_check(self, interaction: Interaction):
        if interaction.user and interaction.user == self.ctx.author:
            return True

        await interaction.response.defer()
        return False

    async def on_timeout(self):
        self.clear_items()
        await self.message.edit(view=self)

    async def start(self):
        self.build_select()


class WispHelp(commands.HelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        self.context = None

    def get_bot_mapping(self):
        """Retrieves the bot mapping passed to :meth:`send_bot_help`."""
        bot = self.context.bot
        ignored_cogs = ['NSFW', 'Events', 'Levels', 'IPC', 'SignalPvP', 'Help', 'Jishaku', 'Logger']

        if self.context.channel.is_nsfw():
            ignored_cogs = ['Events', 'Levels', 'IPC', 'SignalPvP', 'Help', 'Jishaku', 'Logger']

        mapping = {cog: cog.get_commands() for cog in sorted(bot.cogs.values(), key=lambda c: len(c.get_commands()), reverse=True) if cog.qualified_name not in ignored_cogs}
        return mapping


    def get_minimal_command_signature(self, command):
        if isinstance(command, commands.Group):
            return f"[G] {self.context.clean_prefix}{command.qualified_name} {command.usage if command.usage else command.signature}"

        return f"[c] {self.context.clean_prefix}{command.qualified_name} {command.usage if command.usage else command.signature}"


    async def send_bot_help(self, mapping):
        view = HelpView(self.context, usable_commands=f"{len(await self.filter_commands(list(self.context.bot.commands), sort=True)):,}",
                                                        data=mapping)
        await view.start()


    async def send_cog_help(self, cog):
        entries = [command for command in cog.get_commands()]
        menu = paginator.ViewPaginator(paginator.GroupHelpPageSource(cog, entries, prefix=self.context.clean_prefix,
                                                                total_commands=len(cog.get_commands()),
                                                                usable_commands=len(await self.filter_commands(cog.get_commands()))),
                                                                ctx=self.context, compact=True)
        await menu.start()


    async def send_group_help(self, group):
        entries = [command for command in group.commands]
        menu = paginator.ViewPaginator(paginator.GroupHelpPageSource(group, entries, prefix=self.context.clean_prefix,
                                                                total_commands=len(group.commands),
                                                                usable_commands=len(await self.filter_commands(group.commands, sort=True))),
                                                                ctx=self.context, compact=True)
        await menu.start()


    async def send_command_help(self, command: commands.Command):
        embed = nextcord.Embed(title=f"{self.get_minimal_command_signature(command)}", description=f"""
{command.help if command.help else 'No help given...'}
                              """)

        # <---- Command Information ---->

        aliases = command.aliases

        commandInformation = [f"Category: {command.cog_name}"]

        if aliases:
            aliases = ', '.join(aliases)
            commandInformation.append(f"Aliases: {aliases}")

        commandInformation = '\n'.join(commandInformation)

        # <---- Command Information ---->

        # <---- Command Checks ---->

        commandChecks = []

        with contextlib.suppress(commands.CommandError):
            if await command.can_run(self.context):
                commandChecks.append("Usable by you: Yes")

            else:
                commandChecks.append("Usable by you: No")

        try:
            slowmode = command._buckets._cooldown.per
            commandChecks.append(f"Slowmode: {slowmode}s")

        except:
            pass

        try:
            await command.can_run(self.context)

        except Exception as e:
            try:
                if isinstance(e, nextcord.ext.commands.CheckAnyFailure):
                    for e in e.errors:

                        if not isinstance(e, commands.NotOwner):
                            raise e
                raise e

            except commands.MissingPermissions as error:
                text = ', '.join(error.missing_permissions).replace('_', ' ').replace('guild', 'server').title()
                commandChecks.append(f"Author permissions: {text}")

            except commands.BotMissingPermissions as error:
                text = ', '.join(error.missing_permissions).replace('_', ' ').replace('guild', 'server').title()
                commandChecks.append(f"Bot permissions: {text}")

            except commands.NotOwner:
                commandChecks.append(f"Rank required: Bot Owner")

            except commands.PrivateMessageOnly:
                commandChecks.append(f"Restricted access: Can only be executed in DMs")

            except commands.NoPrivateMessage:
                commandChecks.append(f"Restricted access: Can only be executed in servers")

            except commands.DisabledCommand:
                commandChecks.append(f"Restricted access: This is a slash only command")

            finally:
                pass

        commandChecks = '\n'.join(commandChecks)

        embed.add_field(name="<:info:888768239889424444> Command Information", value=f"""
```yaml
{commandInformation}
```
                        """, inline=False)

        if commandChecks:
            embed.add_field(name="<:greenTick:895688440690147370> Command Checks", value=f"""
```yaml
{commandChecks}
```
                            """, inline=False)

        if command.brief:
            embed.add_field(name="Examples", value=f"""
```yaml
{command.brief}
```
                            """, inline=False)
        embed.set_footer(text="<> = required argument | [] = optional argument\nDo NOT type these when using commands!")

        view = GeneralView(ctx=self.context)
        view.message = await self.context.send(embed=embed, view=view)


    def command_not_found(self, string):
        return string


    def subcommand_not_found(self, command, string):
        if isinstance(command, commands.Group) and len(command.all_commands) > 0:
            return command.qualified_name + string
        return command.qualified_name


    async def send_error_message(self, error):
        ctx = self.context

        error = error.lower().replace("No command called", "", ).replace('"', '').replace("found.", "")

        listOfStuff = list(ctx.bot.cogs.keys()) + [c.qualified_name for c in ctx.bot.commands]
        string = ''.join(difflib.get_close_matches(error, listOfStuff, n=1, cutoff=0.1))

        if "mod" in error:
            return await ctx.send_help(ctx.bot.get_cog("Moderation"))

        elif ctx.bot.get_cog(string):
            return await ctx.send_help(ctx.bot.get_cog(string))

        elif ctx.bot.get_command(string):
            return await ctx.send_help(ctx.bot.get_command(string))

        else:
            raise errors.CommandDoesntExist


    async def on_help_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = nextcord.Embed(description=f"{str(error.original)}")
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))

class Help(commands.Cog):
    """The help command, how did you find this though..."""
    def __init__(self, bot):
        self.bot = bot
        self.hidden = True

        self.select_emoji = "<:info:888768239889424444>"
        self.select_brief = "The help command.. but how did you find this?!"

        help_command = WispHelp(command_attrs=dict(slash_command=True))
        help_command.cog = self
        bot.help_command = help_command