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

    @nextcord.slash_command(name="freeloader",description="What happens to the freeloaders..?",guild_ids=[dankMoon])
    async def freeloader(self,interaction:Interaction):
        channel = interaction.channel
        embed = nextcord.Embed(title="🙅 Don't freeload! 🙅",description="Freeloading will result in your account being banned, meaning you miss out on all the future heists, giveaways, and other events we host on the server!",colour=nextcord.Color.magenta())
        embed.set_footer(text="Dank Moon",icon_url="https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/1009198409741250630/1000681054119673856.gif")
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="perks",guild_ids=[dankMoon])
    async def perks(self, interaction:Interaction):
        pass

    @perks.subcommand(name="donator",description="Awesome perks you can unlock by donating to the server!")
    async def donorperks(self, interaction:Interaction):
        embed = nextcord.Embed(title="💸 Donator Perks 💸",description="<@&830118344840970290>: Donator role, access to all Donor channels, one private channel, custom auto-react (carl-bot) and custom role of your choice.\n\n<@&805778150474776587>: Donator role, access to all Donor channels, custom auto-react (carl-bot) and custom role of your choice.\n\n<@&805778060673548288>: Donator role, access to <#805782701982220288> + <#805780935043842088>\n\n<@&805777932340953088>: Donator role + access to <#805782701982220288>",color="3EBA9A")
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999472647744274482/929993645984206928.gif")
        embed.add_field(name="Donator Exclusive Channels",value="<#805782701982220288>\n<#805780935043842088>\n<#805782302608457739>")
        embed.set_footer(text="Thank you so much to all our donators!",icon_url="https://images-ext-1.discordapp.net/external/s4c9yiEAUrRGEj8sxoFSu-yDoz7d6VxSPt-qsdr9n58/%3Fsize%3D1024/https/cdn.discordapp.com/icons/710573788856582225/19fa3e4d220f5d1dd0663f36add1e0ca.png?width=472")
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))