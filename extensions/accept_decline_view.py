import nextcord
import aiosqlite
from nextcord.ext import commands

class confirm_view(nextcord.ui.View):
    def __init__(self, ctx: commands.Context, suggestion: str):
        self.suggestion = suggestion
        self.ctx = ctx
        super().__init__(timeout=10*60)

    @nextcord.ui.button(label="Accept", style=nextcord.ButtonStyle.secondary)
    async def accept(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        async with aiosqlite.connect('bot.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute('CREATE TABLE IF NOT EXISTS suggestions(suggestion TEXT, upvotes INT, downvotes INT, status TEXT)')
                await cursor.execute('SELECT status FROM suggestions WHERE suggestion = ?', (self.suggestion,))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE suggestions SET status = ? WHERE suggestion = ?', ("Accepted", self.suggestion))
                else:
                    pass
                    
            embed = nextcord.Embed(title=self.suggestion, description=f"Suggestion submitted by {self.ctx.author}", colour=0xff0000)
            embed.set_footer(text=self.ctx.author.display_name, icon_url=self.ctx.author.display_avatar)
            embed.add_field(name="Status", value="Accepted")
            await interaction.message.edit(embed=embed)
            await self.ctx.author.send('Your suggestion was accepted')
            for i in self.children:
                i.disabled = True        	
            await db.commit()
            await interaction.message.edit(view=self)

    @nextcord.ui.button(label="Reject", style=nextcord.ButtonStyle.danger)
    async def reject(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        async with aiosqlite.connect('bot.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute('CREATE TABLE IF NOT EXISTS suggestions(suggestion TEXT, upvotes INT, downvotes INT, status TEXT)')
                await cursor.execute('SELECT status FROM suggestions WHERE suggestion = ?', (self.suggestion,))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE suggestions SET status = ? WHERE suggestion = ?', ("Rejected", self.suggestion))
                else:
                    pass
            
            embed = nextcord.Embed(title=self.suggestion, description=f"Suggestion submitted by {self.ctx.author}", colour=0xff0000)
            embed.set_footer(text=self.ctx.author.display_name, icon_url=self.ctx.author.display_avatar)
            embed.add_field(name="Status", value="Rejected")
            await interaction.message.edit(embed=embed)
            await self.ctx.author.send('Your suggestion was rejected')
            await db.commit()
            for i in self.children:
                i.disabled = True
            await interaction.message.edit(view=self)

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        return self.ctx.author.id == 837730346874306581
