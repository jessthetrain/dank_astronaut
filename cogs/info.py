import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime

class ApplicationLinks(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url="https://dyno.gg/form/43615c90", label="Grinder"))
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url="https://dyno.gg/form/82afebe4", label="Partnership Manager"))

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
        embed = nextcord.Embed(title="💸 Donator Perks 💸",description="<@&830118344840970290>: Donator role, access to all Donor channels, one private channel, custom auto-react (carl-bot) and custom role of your choice.\n\n<@&805778150474776587>: Donator role, access to all Donor channels, custom auto-react (carl-bot) and custom role of your choice.\n\n<@&805778060673548288>: Donator role, access to <#805782701982220288> + <#805780935043842088>\n\n<@&805777932340953088>: Donator role + access to <#805782701982220288>",color=nextcord.Color.from_rgb(62,186,154))
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999472647744274482/929993645984206928.gif")
        embed.add_field(name="Donator Exclusive Channels",value="<#805782701982220288>\n<#805780935043842088>\n<#805782302608457739>")
        embed.set_footer(text="Thank you so much to all our donators!",icon_url="https://images-ext-1.discordapp.net/external/s4c9yiEAUrRGEj8sxoFSu-yDoz7d6VxSPt-qsdr9n58/%3Fsize%3D1024/https/cdn.discordapp.com/icons/710573788856582225/19fa3e4d220f5d1dd0663f36add1e0ca.png?width=472")
        await interaction.response.send_message(embed=embed)

    @perks.subcommand(name="grinder",description="Awesome perks you can unlock by becoming a grinder!")
    async def grinderperks(self, interaction:Interaction):
        embed = nextcord.Embed(title="🐸 Dank Grinder Perks 🐸",description="**-** <@&1008502007042150532> role\n**-** Access to <#1008504637097263154> with 4x amari multi\n**-** Custom private channel with up to 4 friends and all the bots\n**-** 2 ARs via carl-bot (First one claimed after 7m grinder payments, and second one after 21m)\n**-** Grinder exclusive giveaways!\n\n**How to become grinder?**\nThe requirement is 1m daily **or** 7m weekly. You can apply by filling out [this form.](https://dyno.gg/form/43615c90)",color=nextcord.Color.from_rgb(65,117,5))
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/1008507712788779107/855478199151493122.gif")
        embed.set_footer(text="Thank you so much to all our grinders!",icon_url="https://cdn.discordapp.com/icons/710573788856582225/19fa3e4d220f5d1dd0663f36add1e0ca.png?size=4096")
        await interaction.response.send_message(embed=embed)
    
    @perks.subcommand(name="booster",description="Awesome perks you can unlock by boosting the server!")
    async def boosterperks(self,interaction:Interaction):
        embed = nextcord.Embed(title="<a:boostingtop:711918594249719889> Booster Perks <a:boostingtop:711918594249719889>",description="<@&713048063005950034>: Access to all Booster channels, private channel +10 friends, custom auto-reaction (carl-bot) and a *permanent* custom role of your choice.\n\n<@&713047939471114290>: Private channel +5 friends, custom auto-react from Carl-bot and access to all Booster channels.\n\n<@&710881557283471362>: Private channel +3 friends, custom auto-react from Carl, and access to Booster only chat channel.",color=nextcord.Colour.from_rgb(244,127,255))
        embed.add_field(name="Booster Exclusive Channels",value="<#713047284237074464> - 3x amari\n<#713046510572535884>\n<#713046635118329889> - 5x amari")
        embed.set_thumbnail("https://cdn.discordapp.com/emojis/997916322098856028.gif?size=96&quality=lossless")
        embed.set_footer(text="Thank you so much to all our boosters!",icon_url="https://images-ext-1.discordapp.net/external/s4c9yiEAUrRGEj8sxoFSu-yDoz7d6VxSPt-qsdr9n58/%3Fsize%3D1024/https/cdn.discordapp.com/icons/710573788856582225/19fa3e4d220f5d1dd0663f36add1e0ca.png?width=472")
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="membercount",description="Shows you how many members are in the server!")
    async def membercount(self, interaction:Interaction):
        memberCount = interaction.guild.member_count
        embed = nextcord.Embed(
            title=interaction.guild.name,
            timestamp=datetime.datetime.now(),
            colour=nextcord.Colour.magenta()
        )
        embed.add_field(name="Member Count",value=f"`{memberCount}` members")
        embed.set_thumbnail(interaction.guild.icon.url)
        embed.set_footer(text=str(interaction.user),icon_url=interaction.user.display_avatar.url)
        if interaction.guild_id == 710573788856582225:
            embed.add_field(name="Goal",value=f"`750` Members\n`{round(memberCount/750*100,2)}%` complete")
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name="applications",description="Apply to become a staff member in Dank Moon!",guild_ids=[dankMoon])
    async def applications(self, interaction:Interaction):
        embed = nextcord.Embed(title="Applications!",colour=nextcord.Colour.magenta(),description="Check out the `/perks` command group!",timestamp=datetime.datetime.now())
        embed.add_field(name="Grinder",value="[Click here to apply!](https://dyno.gg/form/43615c90)")
        embed.add_field(name="Partnership Manager",value="[Click here to apply!](https://dyno.gg/form/82afebe4)")
        embed.add_field(name="Trial Moderator",value="Currently Closed")
        embed.add_field(name="Giveaway Manager",value="Currently Closed")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/996446872451432498/1038885056585945188/my-icon.png")
        embed.set_footer(text=interaction.guild.name,icon_url=interaction.guild.icon.url)
        view = ApplicationLinks()
        await interaction.response.send_message(embed=embed,view=view)


def setup(bot):
    bot.add_cog(Info(bot))