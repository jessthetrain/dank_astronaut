import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime
uptime = round(time.time())

class HelpfulButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url="https://github.com/stones8000/dank_astronaut", label="GitHub Repo"))
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url="https://discord.gg/dPgEcaE4TM", label="Dank Moon"))

class BotStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    dankMoon = 710573788856582225

    @nextcord.slash_command(name="botstats",description="Information about the bot!")
    async def botstats(self, interaction:Interaction):
        embed = nextcord.Embed(
            title="Dank Astronaut",
            description="Dank Astronaut is a Discord bot custom coded for the Dank Moon guild!",
            colour=nextcord.Colour.magenta()
        )
        embed.set_thumbnail(self.bot.user.avatar.url)
        embed.add_field(name="Latency",value=f"{round(self.bot.latency * 1000, 1)}ms")
        embed.add_field(name="Uptime",value=f"<t:{uptime}:R>")
        embed.add_field(name="Developer",value="Stones#1617 <@!688330308688543744>")
        embed.add_field(name="Library",value="[Nextcord](https://github.com/nextcord/nextcord)")
        embed.add_field(name=interaction.guild.name,value=f"`{str(interaction.guild.member_count)}` members")
        view = HelpfulButtons()
        await interaction.response.send_message(embed=embed,view=view)


def setup(bot):
    bot.add_cog(BotStats(bot))