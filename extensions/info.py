import nextcord
from nextcord import UserFlags
from nextcord.ext import commands

UNITS_MAPPING = [
    (1<<50, ' PB'),
    (1<<40, ' TB'),
    (1<<30, ' GB'),
    (1<<20, ' MB'),
    (1<<10, ' KB'),
    (1, (' byte', ' bytes')),
]

def pretty_size(bytes, units=UNITS_MAPPING):
    """Get human-readable file sizes.
    simplified version of https://pypi.python.org/pypi/hurry.filesize/
    """
    for factor, suffix in units:
        if bytes >= factor:
            break
    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix

class Info(commands.Cog, description="Information cog for wisp bot", name="info"):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
		
    COG_EMOJI = "ℹ️"
	
    @commands.command(help="Shows information about a given user or yourself", aliases=['whois'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def userinfo(self, ctx : commands.Context, *, member: nextcord.Member = None):
        try:
            if member == None:
                member = ctx.author
            if member.premium_since == None:
                premiumText = "Not boosting"
            else:
                time = nextcord.utils.format_dt(member.premium_since, style="R")
                premiumText = f"{time}"

            print('Got status')
            if str(member.status).title() == "Online":
                statusEmote = "<:online_status:943147312216145950>"
                statusTitle = "Online"
            elif str(member.status).title() == "Idle":
                statusEmote = "<:idle_status:943150109468807239>"
                statusTitle = "Idle"
            elif str(member.status).title() == "Dnd":
                statusEmote = "<:dnd_status:943150033388339220>"
                statusTitle = "Do not disturb"
            elif str(member.status).title() == "Streaming":
                statusEmote = "<:streaming:943150241664880701>"
                statusTitle = "Streaming"
            else:
                statusEmote = "<:offline_status:943150177924055090>"
                statusTitle = "Offline"

            desktopStatus = ":desktop: <a:tickred:952553470689411102>"
            webStatus = ":globe_with_meridians: <a:tickred:952553470689411102>"
            mobileStatus = ":mobile_phone: <a:tickred:952553470689411102>"

            if str(member.desktop_status) == "online" or str(member.desktop_status) == "idle" or str(member.desktop_status) == "dnd" or str(member.desktop_status) == "streaming":
                desktopStatus = ":desktop: <a:tickgreen:952554840456847360>"

            if str(member.web_status) == "online" or str(member.web_status) == "idle" or str(member.web_status) == "dnd" or str(member.web_status) == "streaming":
                webStatus = ":globe_with_meridians: <a:tickgreen:952554840456847360>"

            if str(member.mobile_status) == "online" or str(member.mobile_status) == "idle" or str(member.mobile_status) == "dnd" or str(member.mobile_status) == "streaming":
                mobileStatus = ":mobile_phone: <a:tickgreen:952554840456847360>"

            print('made embed')
            perm_string = ','.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
            role_string = ' '.join([r.mention for r in member.roles][1:])
			
            joined = sorted(ctx.guild.members, key=lambda mem: mem.joined_at)
            pos = joined.index(member)
            positions = []
            for i in range(-3, 4):
                line_pos = pos + i
                if line_pos < 0:
                    continue
                if line_pos >= len(joined):
                    break
                positions.append("{0:<4}{1}{2:<20}".format(str(line_pos + 1) + ".", " " * 4 + (">" if joined[line_pos] == member else " "), str(joined[line_pos])))
            join_seq = "{}".format("\n".join(positions))

            members = [*sorted(ctx.guild.members, key=lambda m: m.joined_at)]
            x = members.index(ctx.author)
            join_pos = "\n".join(map(str, members[x - 3: x + 3]))
            badges = []
            badge_dict = {
                UserFlags.verified_bot_developer : "<a:Discord_Developer_Badge_Shimmer:952532463706574848>",
                UserFlags.staff : "<:DiscordStaff:952528715978518548>",
                UserFlags.early_supporter : "<:earlysupporter:954667278186721340>",
                UserFlags.partner : "<:blurple_partner:952529693670797314>",
                UserFlags.hypesquad_brilliance : "<:HypeSquadBrilliance:952531074209181716>",
                UserFlags.hypesquad_bravery : "<:bravery:952530830377484338>",
                UserFlags.hypesquad_balance : "<:HypeSquadBalance:952531286197665793>",
                UserFlags.hypesquad : "<:blurple_hypsquad_event:952529922184855602>",
                UserFlags.discord_certified_moderator : "<:blurple_moderator:952536959874633808>",
                UserFlags.bug_hunter : "<:blurple_bug_hunter_1:952530158563233832>",
                UserFlags.bug_hunter_level_2 : "<:BugHunterLvl2:952530300720787486>"
            }
            if member.premium_since:
                badges.append('<:WumpusNitro:943175214999674910><:server_boost_emoji:943158590468915220>')
            for flag in member.public_flags.all():
                f = badge_dict.get(flag, "?")
                badges.append(f)
                
            emoji_badges = " ".join(badges)
            embed = nextcord.Embed(
                title=f"Information about {member.display_name}", 
                description=f"""<:Verified_Grey:943160907285020722> Nickname: {member.display_name}
                :hash: Discriminator:  #{member.discriminator}
                Mention: {member.mention}
                <:Verified_Grey:943160907285020722> ID: {member.id}
                <:WumpusNitro:943175214999674910> Boosting: {premiumText}
                <:invite_art:943174795674157056> Created: {nextcord.utils.format_dt(member.created_at, style="R")}
                <:discord_invite_user:943174397731168356> Joined: {nextcord.utils.format_dt(member.joined_at, style="R")}
                {statusEmote} Status: {statusTitle}
                <:discord:943758114107293717> Client: {desktopStatus} **|** {webStatus} **|** {mobileStatus}
                Mutual guilds: {len(member.mutual_guilds)}
                Join position: 
				```yaml
{join_seq}
				```
                :video_game: Current activity: {str(member.activity.type).split('.')[-1].title() if member.activity else 'Not playing'}: {member.activity.name if member.activity else ''}
                <:IconRoleGreen:943151451327299645> Top Role: {member.top_role.mention}
                <:IconRoleGreen:943151451327299645> Roles: {role_string}
                :hammer_pick: Guild permissions: 
				```yaml
{perm_string}
				```
                Badges: {emoji_badges}
                """, 
                colour=0xff0000
            )
            embed.set_thumbnail(url=member.display_avatar)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            badges.clear()
        except Exception as e:
            print(e)

    @commands.command(help="Shows information about the current guild")
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def serverinfo(self, ctx : commands.Context):

        if ctx.me.guild_permissions.ban_members:
            bannedMembers = len(await ctx.guild.bans())
        else:
            bannedMembers = "Couldn't get banned members."

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "streaming", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        last_boost = max(ctx.guild.members, key=lambda m : m.premium_since or ctx.guild.created_at)
        if last_boost.premium_since is not None:
            boost = f"{last_boost} {nextcord.utils.format_dt(last_boost.premium_since)}"
        else:
            boost = "No boosters exist."

        if ctx.guild.description:
            description = ctx.guild.description
        else:
            description = "This guild doesn't have a description"

        enabled_features = []
        features = set(ctx.guild.features)
        all_features = {
            'COMMUNITY': 'Community guild',
            'VERIFIED': 'Verified',
            'DISCOVERABLE': 'Discoverable',
            'PARTNERED': 'Partnered',
            'FEATURABLE': 'Featured',
            'COMMERCE': 'Commerce',
            'MONETIZATION_ENABLED': 'Monetization',
            'NEWS': 'News Channels',
            'PREVIEW_ENABLED': 'Preview Enabled',
            'INVITE_SPLASH': 'Invite Splash',
            'VANITY_URL': 'Vanity Invite URL',
            'ANIMATED_ICON': 'Animated guild Icon',
            'BANNER': 'ctx.guild Banner',
            'MORE_EMOJI': 'More Emoji',
            'MORE_STICKERS': 'More Stickers',
            'WELCOME_SCREEN_ENABLED': 'Welcome Screen',
            'MEMBER_VERIFICATION_GATE_ENABLED': 'Membership Screening',
            'TICKETED_EVENTS_ENABLED': 'Ticketed Events',
            'VIP_REGIONS': 'VIP Voice Regions',
            'PRIVATE_THREADS': 'Private Threads',
            'THREE_DAY_THREAD_ARCHIVE': '3 Day Thread Archive',
            'SEVEN_DAY_THREAD_ARCHIVE': '1 Week Thread Archive',
        }

        for feature, label in all_features.items():
            if feature in features:
                enabled_features.append(f"<:Tick:943160026669912065> {label}")

        features = '\n'.join(enabled_features)

        if features == "":
            features = "This guild doesn't have any features."

        verification_level1 = str(ctx.guild.verification_level)
        verification_level = verification_level1.capitalize()

        if verification_level == "Low":
            verificationEmote = "<:Verified_Seagull:943156472102142063>"
        elif verification_level == "Medium":
            verificationEmote = "<:Verified_Orange:943156339037855754>"
        elif verification_level == "High":
            verificationEmote = "<:Verified_Yellow:943156056115273748>"
        elif verification_level == "Highest":
            verificationEmote = "<:Verified_Seagull:943156472102142063>"
        else:
            verificationEmote = "<:Verified_Black:943156976127451138>"

        if str(ctx.guild.explicit_content_filter) == "no_role":
            explictContentFilter = "Scan media content from members without a role."
        elif str(ctx.guild.explicit_content_filter) == "all_members":
            explictContentFilter = "Scan media from all members."
        else:
            explictContentFilter = "Don't scan any media content."

        embed = nextcord.Embed(title=f"{ctx.guild}", description=f"""
        <:Verified_Grey:943160907285020722> ID: {ctx.guild.id}
        :information_source: Description: {description}

        <:Members:943161161627598889> Members: {len(ctx.guild.members)} (:robot: {len(list(filter(lambda m : m.bot, ctx.guild.members)))})
        :robot: Bots: {len(list(filter(lambda m: m.bot, ctx.guild.members)))}
        :crown: Owner: {ctx.guild.owner}
        <:Members:943161161627598889> Max members: {ctx.guild.max_members}
        <:BanHammer:943140661660643369> Banned members: {bannedMembers}

        {verificationEmote} Verification level: {verification_level}
        <:nsfw_channel:943142110457114644> Explicit content filter: {explictContentFilter}
        :file_folder: Filesize limit: {pretty_size(ctx.guild.filesize_limit)}
        Created: {nextcord.utils.format_dt(ctx.guild.created_at, style="R")}

        <:offline_status:943150177924055090> Statuses: <:online_status:943147312216145950> {statuses[0]} <:idle_status:943150109468807239> {statuses[1]} <:dnd_status:943150033388339220> {statuses[2]} <:streaming:943150241664880701> {statuses[3]} <:offline_status:943150177924055090> {statuses[4]}
        <:Channel:943142478914125874> Channels: <:Channel:943142478914125874> {len(ctx.guild.text_channels)} <:blurple_voicechannel:943144093687619664> {len(ctx.guild.voice_channels)} <:Stage:943145124995686420> {len(ctx.guild.stage_channels)} <:thread_channel:943146501050363904> {len(ctx.guild.threads)}
        <:IconRoleGreen:943151451327299645> Roles: {len(ctx.guild.roles)}

        ☺️ Animated emojis: {len([x for x in ctx.guild.emojis if x.animated])}/{ctx.guild.emoji_limit}
        ☺️ Non animated emojis: {len([x for x in ctx.guild.emojis if not x.animated])}/{ctx.guild.emoji_limit}

        <:server_boost_emoji:943158590468915220> Level: {ctx.guild.premium_tier}
        <:nitro_boost:943158960196841523> Boosts: {ctx.guild.premium_subscription_count}
        <:nitro_boost:943158960196841523> Latest booster: {boost}

        Features:
        {features}
                """, colour=0xff0000)

        if ctx.guild.banner:
            embed.set_image(url=ctx.guild.banner)

        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon)

        await ctx.send(embed=embed)

    @commands.command(help="Shows information about the bot")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def botinfo(self, ctx : commands.Context):
        try:
            embed = nextcord.Embed(
                title="Information about myself", 
                description=f"""<:Verified_Grey:943160907285020722> Name: {self.bot.user.name}
                :hash: Discriminator: {self.bot.user.discriminator}
                <:Verified_Grey:943160907285020722> ID: {self.bot.user.id}
                <:invite_art:943174795674157056> Created: {nextcord.utils.format_dt(self.bot.user.created_at, style="R")}
                <:slashcommand:952856911655616532> Command count: {len(self.bot.commands)}
                <:plugin:952857159597715466> Extension count: 10
                <a:Tick:952856460721786900> Verified: False
                <:Python:952856071997882490> Python version: Python 3.8
                <:developer:943758428415877131> Developer: Programming geek#5593
				<:discord_invite_user:943174397731168356> User count: {len(self.bot.users)}
                """, 
                colour=0xff0000
            )
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
			
    @commands.command(help="Shows the avatar of the person you mentioned or yourself")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def avatar(self, ctx : commands.Context, member : nextcord.Member = None):
        if member == None:
            member = ctx.author

        embed = nextcord.Embed(title=f"Avatar of {member.display_name}", colour=0xff0000)
        embed.set_image(url=member.display_avatar)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

    @commands.command(help="Shows the badges of the person you mentioned or yourself")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def badges(self, ctx : commands.Context, member : nextcord.Member = None):
        await ctx.send(member.public_flags.all())
        
		
def setup(bot : commands.Bot):
    bot.add_cog(Info(bot))