import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    dankMoon = 710573788856582225

    @nextcord.slash_command(name="freeloader",guild_ids=[dankMoon])
    async def freeloader(self,interaction:Interaction):
        channel = interaction.channel
        embed = nextcord.Embed(title="🙅 Don't freeload! 🙅",description="Freeloading will result in your account being banned, meaning you miss out on all the future heists, giveaways, and other events we host on the server!",colour=nextcord.Color.magenta())
        embed.set_footer(text="Dank Moon",icon_url="https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/1009198409741250630/1000681054119673856.gif")
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))