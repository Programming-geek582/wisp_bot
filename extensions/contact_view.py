import nextcord
from typing import Optional

class DevForm(nextcord.ui.Modal):
    def __init__(self, ctx):
        super().__init__(
            title="Developer contact",
            timeout=5 * 60
        )
        self.ctx = ctx

        self.name = nextcord.ui.TextInput(
            label="Reason for contacting the developer",
            min_length=2,
            max_length=50,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="The suggestions and other stuff you wanna say",
            required=False,
            max_length=1800,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        embed = nextcord.Embed(title="Dev contact", description="Your message was sent successfully", colour=0xff0000)
        embed.set_footer(text=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        await interaction.response.send_message(embed=embed)
        developer = interaction.client.get_user(837730346874306581)
        embed2 = nextcord.Embed(title=f"New message from {interaction.user}", description=self.description.value, colour=0xff0000)
        embed2.set_footer(text=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        await developer.send(embed=embed2)

    async def interaction_check(self, interaction):
        return self.ctx.author == interaction.user

class DevContactView(nextcord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx

    @nextcord.ui.button(label="Open the developer contact popup", style=nextcord.ButtonStyle.primary, emoji="🔓")
    async def open_popup(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        await interaction.response.send_modal(modal=DevForm(self.ctx))

    async def interaction_check(self, interaction):
        return self.ctx.author == interaction.user