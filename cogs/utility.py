import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    dankMoon = 710573788856582225
    
    @nextcord.slash_command(name="avatar",description="View a user's avatar")
    async def avatar(self, interaction:Interaction, user:nextcord.User=None):
        if user == None:
            user = interaction.user
        embed = nextcord.Embed(title=f"Avatar of {user}", color=nextcord.Color.magenta())
        if user.avatar != None:
            embed.set_image(url=str(user.avatar))
        else:
            embed.set_image(url=user.default_avatar)
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name="ping",description="🏓 Shows the bot's latency",force_global=True)
    async def ping(self, interaction:Interaction):
        embed = nextcord.Embed(title="Pong! 🏓",description=f"{round(self.bot.latency * 1000, 1)}ms",color=nextcord.Color.magenta())
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name="userinfo",description="View cool information about a Discord user")
    async def userinfo(self,interaction:Interaction,user:nextcord.User=None):
        if user == None:
            user = interaction.user
        embed = nextcord.Embed(color=nextcord.Color.magenta(),title=user.display_name)
        if user.avatar != None:
            embed.set_author(name=f"{user}",icon_url=str(user.avatar.url))
        else:
            embed.set_author(name=f"{user}",icon_url=str(user.default_avatar.url))
        embed.set_thumbnail(str(user.display_avatar.url))
        if user.banner != None:
            embed.set_image(str(user.banner.url))
        embed.set_footer(text=f"ID: {user.id}")
        embed.add_field(name="Account Created",value=f"{user.created_at.year}-{user.created_at.month}-{user.created_at.day} at {user.created_at.hour}:{user.created_at.minute}:{user.created_at.second} {user.created_at.tzinfo}\n<t:{calendar.timegm([user.created_at.year,user.created_at.month,user.created_at.day,user.created_at.hour,user.created_at.minute,user.created_at.second])}:R>")
        embed.add_field(name="Is a bot?",value=str(user.bot))
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="whois",description="View cool information about another member of the server")
    async def whois(self,interaction:Interaction,member:nextcord.Member=None):
        if member == None:
            member = interaction.user
        embed = nextcord.Embed(color=nextcord.Color.magenta(),title=member.display_name)
        if member.avatar != None:
            embed.set_author(name=member,icon_url=member.avatar.url)
        else:
            embed.set_author(name=member,icon_url=member.default_avatar.url)
        embed.set_thumbnail(member.display_avatar.url)
        if member.banner != None:
            embed.set_image(member.banner.url)
        embed.set_footer(text=f"ID: {member.id}")
        embed.add_field(name="Account Created",value=f"{member.created_at.year}-{member.created_at.month}-{member.created_at.day} at {member.created_at.hour}:{member.created_at.minute}:{member.created_at.second} {member.created_at.tzinfo}\n<t:{calendar.timegm([member.created_at.year,member.created_at.month,member.created_at.day,member.created_at.hour,member.created_at.minute,member.created_at.second])}:R>")
        embed.add_field(name="Joined Server",value=f"{member.joined_at.year}-{member.joined_at.month}-{member.joined_at.day} at {member.joined_at.hour}:{member.joined_at.minute}:{member.joined_at.second} {member.joined_at.tzinfo}\n<t:{calendar.timegm([member.joined_at.year,member.joined_at.month,member.joined_at.day,member.joined_at.hour,member.joined_at.minute,member.joined_at.second])}:R>")
        embed.add_field(name="Is a bot?",value=str(member.bot))
        if len(member.roles) <= 40:
            userroles = f"{str(len(member.roles))}: "
            for role in member.roles:
                userroles = f"{userroles}<@&{role.id}>, "
            embed.add_field(name="Roles",value=userroles,inline=False)
        else:
            embed.add_field(name="Roles",value=f"{str(len(member.roles))}: (Too many to list)",inline=False)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(name="report",description="Report a user for breaking the rules",guild_ids=[dankMoon])
    async def report(self,interaction:Interaction,user:nextcord.Member=SlashOption(
        name = "user",
        description = "Who are you reporting?",
        required = True
    ), reason:str=SlashOption(
        name = "reason",
        description = "What are you reporting them for?",
        required = True
    ), proof:str=SlashOption(
        name = "evidence",
        description = "Link any proof of this user breaking rules here",
        required = True
    )):
        reportsChannel = self.bot.get_channel(1022921093243228281)
        embed = nextcord.Embed(title="User report",color=nextcord.Color.red(),description=f"User reported: {user.mention}\nReported by: {interaction.user.mention}",timestamp=datetime.datetime.now())
        embed.add_field(name="Reason",value=reason,inline=False)
        embed.add_field(name="Evidence",value=proof,inline=False)
        embed.set_author(name=f"{interaction.user.name}{interaction.user.discriminator}",icon_url=interaction.user.avatar)
        embed.set_footer(text="Dank Moon",icon_url="https://images-ext-1.discordapp.net/external/7Ne3WO4lcdhIcP9gw9qvxWFikTYqcsrnDSNwQEZvkzg/%3Fsize%3D4096/https/cdn.discordapp.com/icons/710573788856582225/19fa3e4d220f5d1dd0663f36add1e0ca.png?width=472&height=472")
        embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/1022926691389145148/report.png")
        await reportsChannel.send(content="<@&796430109090250763>",embed=embed)
        await interaction.response.send_message("✅ Your report has been submitted to the staff.",ephemeral=True)


def setup(bot):
    bot.add_cog(Utility(bot))