import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    dankMoon = 710573788856582225

    @nextcord.slash_command(name="staff",guild_ids=[dankMoon])
    async def staff(self, interaction:Interaction):
        pass

    @staff.subcommand(name="promote",description="Promote a member of staff")
    async def promote(self, interaction:Interaction,mos:nextcord.Member=SlashOption(
        name="staff_member",
        description="Who is getting promoted?",
        required=True
    ),oldRank:str=SlashOption(
        name="previous_rank",
        description="What rank was this staff member previously?",
        required=True
    ),newRank:str=SlashOption(
        name="new_rank",
        description="What rank are you promoting this staff member to?",
        required=True
    ),message:str=SlashOption(
        name="message",
        description="What should we send to the user? Why were they promoted?",
        required=True
    )):
        adminRole = interaction.guild.get_role(805719483930771477)
        if adminRole in interaction.user.roles:
            embed = nextcord.Embed(
                title="🌜 Congratulations! 🌛",
                description=f"You have been promoted in {interaction.guild.name}",
                timestamp=datetime.datetime.now(),
                colour=nextcord.Colour.magenta()
            )
            embed.add_field(name="From",value=oldRank,inline=True)
            embed.add_field(name="To",value=newRank,inline=True)
            embed.add_field(name="Message from Admin:",value=message,inline=False)
            embed.set_footer(text=interaction.guild.name,icon_url=interaction.guild.icon.url)
            embed.set_thumbnail(interaction.guild.icon.url)
            try:
                mos.send(embed=embed)
            except:
                interaction.response.send_message(":warning: Could not send DM to user.")
            else:
                interaction.response.send_message("✅ Sent DM")
        else:
            interaction.response.send_message(content=":x: You are not permitted to do this",ephemeral=True)


def setup(bot):
    bot.add_cog(Staff(bot))