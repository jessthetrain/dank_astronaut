import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime

class Heists(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    dankMoon = 710573788856582225

    @nextcord.slash_command(name="heist",guild_ids=[dankMoon])
    async def heist(self,interaction:Interaction):
        pass

    @heist.subcommand(name="donate",description="Donate to a Dank Memer friendly heist!")
    async def hdonate(self,interaction:Interaction, amount:int=SlashOption(
        name="amount",
        description="How much are you donating to the heist?",
        required=True
    ), requirements:str=SlashOption(
        name="requirements",
        description="Do you want to add a requirement for people to enter the heist?",
        required=False,
        default="None"
    ), message:str=SlashOption(
        name="message",
        description="Would you like to add a message to your heist?",
        required=False,
        default="None"
    )):
    #    embed = nextcord.Embed(
    #        title="💸 Heist Donation! 💸",
    #        description=f"<:pink_arrow_right:1001505500296396890> **Amount** <:purple_arrow_right:1001506139109863576> {amount}\n<:pink_arrow_right:1001505500296396890> **Requirements** <:purple_arrow_right:1001506139109863576> {requirements}\n<:pink_arrow_right:1001505500296396890> **Message** <:purple_arrow_right:1001506139109863576> {message}\n\n<:pink_arrow_right:1001505500296396890> Donated by {interaction.user.mention}",
    #        color=nextcord.Color.magenta()
    #    )
    #    embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    #    embed.set_author(name=interaction.user,icon_url=interaction.user.display_avatar)
    #    donationChannel = self.bot.get_channel(741054074740539413)
    #    await interaction.response.send_message(content="✅ <#741054074740539413>",ephemeral=True)
    #    await donationChannel.send(content="<@&715270049350549524>",embed=embed)
        await interaction.response.send_message(content=":x: This command has temporarily been disabled.",ephemeral=True)

    @heist.subcommand(name="ping", description="Ping the heist ping role (For staff)")
    async def hping(self,interaction:Interaction,amount:int=SlashOption(
        name="amount",
        description="How much is the heist?",
        required=True
    ),donor=SlashOption(
        name="donator",
        description="Who donated to the heist?",
        required=False,
        default="None"
    ), message:str=SlashOption(
        name="message",
        description="Message for the heist",
        required=False,
        default="None"
    ), requirement:str=SlashOption(
        name="requirement",
        description="Is there a requirement to join this heist?",
        required=False,
        default="None"
    )):
        hman = interaction.guild.get_role(715270049350549524)
        if hman in interaction.user.roles:
            channel = interaction.channel
            embed = nextcord.Embed(
                title="💸 Friendly Heist! 💸",
                description=f"<:pink_arrow_right:1001505500296396890> **Amount:** {amount}\n<:pink_arrow_right:1001505500296396890> **Donator:** {donor}\n<:pink_arrow_right:1001505500296396890> **Message:** {message}\n<:pink_arrow_right:1001505500296396890> **Requirement:** {requirement}\n\n<:pink_arrow_right:1001505500296396890> Thank the donor in <#710573789309698060>",
                color=nextcord.Color.magenta()
            )
            embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
            await interaction.response.send_message(content="✅",ephemeral=True)
            await channel.send(content="<@&711954189974241337>",embed=embed)
        else:
            await interaction.response.send_message(content="❌ You are not a heist manager",ephemeral=True)


def setup(bot):
    bot.add_cog(Heists(bot))