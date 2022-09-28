import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    dankMoon = 710573788856582225
    
    @nextcord.slash_command(name="giveaway",guild_ids=[dankMoon])
    async def giveaway(self,interaction:Interaction):
        pass

    @giveaway.subcommand(name="donate",description="Donate to a Dank Memer Giveaway!")
    async def donate(self,interaction:Interaction, duration:int=SlashOption(
        name="hours",
        description="How long do you want the giveaway to last?",
        required=True,
        min_value=1,
        max_value=12
    ), winners:int=SlashOption(
        name="winners",
        description="How many winners should the bot choose?",
        required=True,
        min_value=1,
        max_value=5
    ), prize:str=SlashOption(
        name="prize",
        description="What are you giving away?",
        required=True
    ), requirements:str=SlashOption(
        name="requirements",
        description="Do you want to add a requirement for people to enter the giveaway?",
        required=False,
        default="None",
        choices=["Grinder","Booster"]
    ), message:str=SlashOption(
        name="message",
        description="Would you like to add a message to your giveaway?",
        required=False,
        default="None"
    )):
        embed = nextcord.Embed(
            title="🎉 Giveaway Donation! 🎉",
            description=f"<:pink_arrow_right:1001505500296396890> **Time** <:purple_arrow_right:1001506139109863576> {duration} hour(s)\n<:pink_arrow_right:1001505500296396890> **Winners** <:purple_arrow_right:1001506139109863576> {winners}\n<:pink_arrow_right:1001505500296396890> **Requirements** <:purple_arrow_right:1001506139109863576> {requirements}\n<:pink_arrow_right:1001505500296396890> **Prize** <:purple_arrow_right:1001506139109863576> {prize}\n<:pink_arrow_right:1001505500296396890> **Message** <:purple_arrow_right:1001506139109863576> {message}\n\n<:pink_arrow_right:1001505500296396890> Donated by {interaction.user.mention}",
            color=nextcord.Color.magenta()
        )
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
        embed.set_author(name=interaction.user,icon_url=interaction.user.display_avatar)
        donationChannel = self.bot.get_channel(741054074740539413)
        await interaction.response.send_message(content="✅ <#741054074740539413>",ephemeral=True)
        await donationChannel.send(content="<@&766651025364746260>",embed=embed)

    @giveaway.subcommand(name="ping", description="Ping the giveaway ping role (For staff)")
    async def gping(self,interaction:Interaction,donor:nextcord.Member=SlashOption(
        name="donator",
        description="Who donated to the giveaway?",
        required=False
    ), message:str=SlashOption(
        name="message",
        description="Message for the giveaway",
        required=False
    )):
        gman = interaction.guild.get_role(766651025364746260)
        if gman in interaction.user.roles:
            channel = interaction.channel
            if donor==None and message==None:
                await channel.send(content="<@&711954068578500638> Thank the donor in <#710573789309698060>")
                await interaction.response.send_message(content="✅",ephemeral=True)
            elif donor==None:
                embed = nextcord.Embed(
                    title="🎉 Giveaway! 🎉",
                    description=f"<:pink_arrow_right:1001505500296396890> **Message:** {message}\n\n<:pink_arrow_right:1001505500296396890> Thank the donor in <#710573789309698060>",
                    color=nextcord.Color.magenta()
                )
                embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
                await interaction.response.send_message(content="✅",ephemeral=True)
                await channel.send(content="<@&711954068578500638>",embed=embed)
            elif message==None:
                embed = nextcord.Embed(
                    title="🎉 Giveaway! 🎉",
                    description=f"<:pink_arrow_right:1001505500296396890> **Donator:** {donor.mention}\n\n<:pink_arrow_right:1001505500296396890> Thank the donor in <#710573789309698060>",
                    color=nextcord.Color.magenta()
                )
                embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
                await interaction.response.send_message(content="✅",ephemeral=True)
                await channel.send(content="<@&711954068578500638>",embed=embed)
            else:
                embed = nextcord.Embed(
                    title="🎉 Giveaway! 🎉",
                    description=f"<:pink_arrow_right:1001505500296396890> **Donator:** {donor.mention}\n<:pink_arrow_right:1001505500296396890> **Message:** {message}\n\n<:pink_arrow_right:1001505500296396890> Thank the donor in <#710573789309698060>",
                    color=nextcord.Color.magenta()
                )
                embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
                await interaction.response.send_message(content="✅",ephemeral=True)
                await channel.send(content="<@&711954068578500638>",embed=embed)
        else:
            await interaction.response.send_message(content="❌ You are not a giveaway manager",ephemeral=True)


def setup(bot):
    bot.add_cog(Giveaways(bot))