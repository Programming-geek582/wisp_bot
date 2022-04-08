from nextcord.ext import commands
import nextcord
import datetime
import random
from typing import List, Optional

class Stuff(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        url = "https://nextcord.com/api/oauth2/authorize?bot_id=760179628122964008&permissions=8&scope=bot"
        self.add_item(nextcord.ui.Button(emoji="<:invite_art:943174795674157056>", label='Invite me', url=url))

class MyHelp(commands.HelpCommand):
		
    def get_minimal_command_signature(self, command):
        return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    def get_command_name(self, command):
        return '%s' % (command.qualified_name)

    async def send_bot_help(self, mapping):
        ctx = self.context
        prefix = self.context.clean_prefix
        embed = nextcord.Embed(title="Help", description=f"""
Prefix: `{prefix}`
Total commands: `{len(list(self.context.bot.commands))}`
Commands usable by you (in this server): `{len(await self.filter_commands(list(self.context.bot.commands), sort=True))}`
```diff
+ Type {prefix}help [command/category] for help on a command/category
- <> = required argument
- [] = optional argument
```
                              """, colour=0xff0000)

        allcogs = []
        cogindex = []
        ignored_cogs = ['Help', 'Jishaku', 'events']
        iter = 1
        for cog, commands in mapping.items():
            if cog is None or cog.qualified_name in ignored_cogs: continue
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_name(c) for c in filtered]
            if command_signatures:
                num = f"{iter}\U0000fe0f\U000020e3" if iter < 10 else "\U0001f51f"
                cogindex.append(cog.qualified_name)
                allcogs.append(f"{getattr(cog, 'COG_EMOJI', None)}{cog.description.split('|')[0]} `{prefix}help {cog.qualified_name}`")
                iter+=1
        nl = '\n'
        embed.add_field(name=f"<:menu:959400425507921930> __**Available categories**__ **[{len(allcogs)}]**", value=f"""
{nl.join(allcogs)}
        """)
        embed.set_footer(text=f"Suggested command: {prefix}{random.choice(list(self.context.bot.commands))} • Credits given in {prefix}credits")
        await ctx.send(embed=embed, view=Stuff())


    async def send_command_help(self, command):
        ctx : commands.Context = self.context
        alias = command.aliases
        description = command.help
        aliastext = "Aliases: ❌ This command has no aliases."
        descriptiontext = "Description: ❌ This command has no description."
        if alias:
            aliastext = f"Aliases: {', '.join(alias)}"
        if description:
            descriptiontext = f"Description: {command.help}"
        embed = nextcord.Embed(title=f"Help - {command}", description=f"""
```diff
- <> = required argument
- [] = optional argument
```
```yaml
Usage: {self.get_minimal_command_signature(command)}
{aliastext}
{descriptiontext}
```
                                  """, colour=0xff0000)

        if command.brief:
            embed.set_image(url=command.brief)

        embed.set_footer(text=f"Command requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)


    async def send_cog_help(self, cog : commands.Cog):
        ctx = self.context
        prefix = self.context.clean_prefix
        entries = cog.get_commands()
        command_signatures = [self.get_minimal_command_signature(c) for c in entries]
        if command_signatures:
            val = "\n".join(command_signatures)
            embed=nextcord.Embed(title=f"{getattr(cog, 'COG_EMOJI')}Help - {cog.qualified_name}", description=f"""
Total commands: {len(cog.get_commands())}
Commands usable by you (in this server): {len(await self.filter_commands(cog.get_commands(), sort=True))}
```diff
- <> = required argument
- [] = optional argument
+ Type {prefix}help [command] for help on a command
```
Description: {cog.description}


__**Available commands**__ **[{len(cog.get_commands())}]**
```fix
{val}
```
                                """, colour=0xff0000)
            embed.set_footer(text=f"Command requested by {ctx.author}", icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed)
        else:
            embed=nextcord.Embed(title=f"Help - {cog.qualified_name}", description=f"""
Total commands: {len(cog.get_commands())}
Commands usable by you (in this server): {len(await self.filter_commands(cog.get_commands(), sort=True))}
```diff
- <> = required argument
- [] = optional argument
+ Type {prefix}help [command] for help on a command
+ Description: {cog.description}
```
__**Available commands**__ **[{len(cog.get_commands())}]**
```fix
This cog has no commands
```
                                """, colour=0xff0000)
            await ctx.send(embed=embed)

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = nextcord.Embed(description=f"{str(error.original)}")
            embed.set_footer(text=f"Command requested by {ctx.author}", icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed, colour=0xff0000)


class Help(commands.Cog):
    ":question: | The help command, how did you find this though..."
    def __init__(self, bot):
        self.bot = bot
        self.hidden = True
        help_command = MyHelp()
        help_command.cog = self
        bot.help_command = help_command

def setup(bot):
    bot.add_cog(Help(bot))
