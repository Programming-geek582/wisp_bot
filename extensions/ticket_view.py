import nextcord
import aiosqlite
import time
from typing import Optional

class ticket_delete_view(nextcord.ui.View):
    def __init__(self, *, timeout: Optional[float] = None):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Delete ticket", style=nextcord.ButtonStyle.danger, emoji="🔒", custom_id="ticket_delete_view:ticketdeletebtn")
    async def delete_ticket(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        channel = interaction.channel
        await channel.delete()

class ticket_create_view(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Create ticket", style=nextcord.ButtonStyle.primary, emoji="📩", custom_id="ticket_create_view:ticketcreatebtn")
    async def create_ticket(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        async with aiosqlite.connect('tickets.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT counter, support_role_id FROM tickets WHERE guild_id = ?', (interaction.guild.id,))
                data = await cursor.fetchone()
                counter = data[0]
                await cursor.execute('UPDATE tickets SET counter = ? WHERE guild_id = ?', (counter + 1, interaction.guild.id,))
                role = data[1]
            await db.commit()
        overwrites = {
            interaction.guild.default_role: nextcord.PermissionOverwrite(view_channel=False),
            interaction.user: nextcord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        support_role = interaction.guild.get_role(role)
        channel = await interaction.channel.category.create_text_channel(name=f"ticket {data[0]} - {interaction.user.name}", overwrites=overwrites)
        embed = nextcord.Embed(title='Ticket created', description="Support will be with you shortly", colour=0xff0000)
        await channel.send(support_role.mention, delete_after=1)
        await channel.send(f"{interaction.user.mention}", embed=embed, view=ticket_delete_view())
