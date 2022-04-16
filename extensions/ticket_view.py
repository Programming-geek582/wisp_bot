import nextcord
import aiosqlite
from typing import Optional

class ticket_create_view(nextcord.ui.View):
    def __init__(self, *, timeout: Optional[float] = 180):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Create ticket", style=nextcord.ButtonStyle.grey, emoji="📜")
    async def create_ticket(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        async with aiosqlite.connect('tickets.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT counter FROM tickets WHERE guild_id = ?', (interaction.guild.id,))
                data = await cursor.fetchone()

        await db.commit()
        await interaction.channel.category.create_text_channel(name=f"ticket {data[0]} - {interaction.user.name}")
