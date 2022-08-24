from sre_constants import SUCCESS
from discord import AllowedMentions
import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
intents.bans = True
nextcord.http._modify_api_version(9)
bot = commands.Bot(command_prefix=["<@999760430052417638> ", "a.", "A."], case_insensitive=True,intents=intents)
dankMoon = 710573788856582225

class verifyButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
    
    @nextcord.ui.button(label="Verify!",style=nextcord.ButtonStyle.green,emoji="✅")
    async def verify(self, button:nextcord.ui.button,interaction:nextcord.Interaction):
        guild = bot.get_guild(710573788856582225)
        verified = guild.get_role(741336292612243603)
        if verified in interaction.user.roles:
            await interaction.response.send_message(ephemeral=True,content="You are already verified...")
        else:
            await interaction.user.add_roles(verified)
            await interaction.response.send_message(ephemeral=True,content="You have been verfied!")
            general = bot.get_channel(710573789309698060)
            mentions = nextcord.AllowedMentions(everyone=False,users=True,roles=False)
            await general.send(f"Everyone welcome {interaction.user.mention} to the server!\nIf you are looking for a heist, it will probably be in <#711435197807067156> :slight_smile:",allowed_mentions=mentions,delete_after=120)
        self.value = True

@bot.event # This event prints in the console when the bot has logged in
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=nextcord.Game(name=".gg/dPgEcaE4TM"),status=nextcord.Status.idle)
    channel = await bot.fetch_channel(996446872451432498)
    startupEmbed = nextcord.Embed(title="The bot has started!", description="Hi **Stones**! The bot has now started. Feel free to use `a.help` to see what I can do!",color=nextcord.Color.magenta())
    startupEmbed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    await channel.send(embed=startupEmbed)
    verificationChannel = bot.get_channel(741336727188144148)
    embed = nextcord.Embed(title="Verification",description="Click the button below to get verified!",color=nextcord.Color.green())
    await verificationChannel.purge(limit=5,check=lambda m:m.author==bot.user)
    view = verifyButtons()
    await verificationChannel.send(embed=embed,view=view)
    await view.wait()

@commands.has_role(805719483930771477)
@bot.command()
async def verification(ctx):
    embed = nextcord.Embed(title="Verification",description="Click the button below to get verified!",color=nextcord.Color.green())
    await ctx.channel.purge(limit=1)
    view = verifyButtons()
    await ctx.send(embed=embed,view=view)
    await view.wait()

@bot.slash_command(name="avatar",description="View a user's avatar")
async def avatar(interaction:Interaction,user:nextcord.User=None):
    if user == None:
        user = interaction.user
    embed = nextcord.Embed(title=f"Avatar of {user}", color=nextcord.Color.magenta())
    if user.avatar != None:
        embed.set_image(url=str(user.avatar))
    else:
        embed.set_image(url=user.default_avatar)
    await interaction.response.send_message(embed=embed)

@bot.slash_command(name="ping",description="🏓 Shows the bot's latency",force_global=True)
async def ping(interaction:Interaction):
    embed = nextcord.Embed(title="Pong! 🏓",description=f"{round(bot.latency * 1000, 1)}ms",color=nextcord.Color.magenta())
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_member_join(member):
    embed = nextcord.Embed(title=f"Welcome to Dank Moon, {member}!",description=f"To get started in the server, read the rules in <#710840207808659517> and verify in <#741336727188144148>",color=nextcord.Color.magenta())
    embed.add_field(name="Once you have verified...",value="+ Get pings and other roles from <#711952053433401375>!\n+ Select your colour role in <#710847274988732507>!\n+ Chat with us in <#710573789309698060>!\n+ Our heists take place in <#711435197807067156>!\n+ See what we are giving away in <#711435312332537889> and <#809422611452919818>!")
    embed.set_footer(text="If you are here for a heist, don't freeload! We ban freeloaders :P")
    embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    await member.send(embed=embed)
    rulesChan = bot.get_channel(710840207808659517)
    await rulesChan.send(f"{member.mention}",delete_after=1)

@bot.slash_command(name="userinfo",description="View cool information about a Discord user")
async def userinfo(interaction:Interaction,user:nextcord.User=None):
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

@bot.slash_command(name="whois",description="View cool information about another member of the server")
async def whois(interaction:Interaction,member:nextcord.Member=None):
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

@bot.slash_command(name="giveaway",guild_ids=[dankMoon])
async def giveaway(interaction:Interaction):
    pass

@giveaway.subcommand(name="donate",description="Donate to a Dank Memer Giveaway!")
async def donate(interaction:Interaction, duration:int=SlashOption(
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
    donationChannel = bot.get_channel(741054074740539413)
    await interaction.response.send_message(content="✅ <#741054074740539413>",ephemeral=True)
    await donationChannel.send(content="<@&766651025364746260>",embed=embed)

@giveaway.subcommand(name="ping", description="Ping the giveaway ping role (For staff)")
async def gping(interaction:Interaction,donor:nextcord.Member=SlashOption(
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

@bot.slash_command(name="heist",guild_ids=[dankMoon])
async def heist(interaction:Interaction):
    pass

@heist.subcommand(name="donate",description="Donate to a Dank Memer friendly heist!")
async def hdonate(interaction:Interaction, amount:int=SlashOption(
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
#    donationChannel = bot.get_channel(741054074740539413)
#    await interaction.response.send_message(content="✅ <#741054074740539413>",ephemeral=True)
#    await donationChannel.send(content="<@&715270049350549524>",embed=embed)
    await interaction.response.send_message(content=":x: This command has temporarily been disabled.",ephemeral=True)

@heist.subcommand(name="ping", description="Ping the giveaway ping role (For staff)")
async def hping(interaction:Interaction,amount:int=SlashOption(
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

@bot.slash_command(name="freeloader",guild_ids=[dankMoon])
async def freeloader(interaction:Interaction):
    pass

@freeloader.subcommand(name="perks")
async def freeloaderperks(interaction:Interaction):
    channel = interaction.channel
    embed = nextcord.Embed(title="🙅 Don't freeload! 🙅",description="Freeloading will result in your account being banned, meaning you miss out on all the future heists, giveaways, and other events we host on the server!",colour=nextcord.Color.magenta())
    embed.set_footer(text="Dank Moon",icon_url="https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/1009198409741250630/1000681054119673856.gif")
    await interaction.response.send_message(embed=embed)

@freeloader.subcommand(name="catch")
async def catchfreeloader(interaction:Interaction,freeloader:nextcord.User=SlashOption(name="freeloader",description="Who did you catch freeloading?",required=True)):
    if interaction.user.guild_permissions.ban_members == True:
        if freeloader == interaction.user:
            await interaction.response.send_message(content="https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/")
        else:
            await interaction.guild.ban(user=freeloader,reason=f"Got caught freeloading by {interaction.user}... imagine")
            await interaction.response.send_message(content=f"Banned {freeloader} for freeloading")
    else:
        await interaction.response.send_message(content="❌ You cannot ban members",ephemeral=True)

@bot.event
async def on_member_ban(guild, user):
    if guild == bot.get_guild(710573788856582225):
        embed = nextcord.Embed(title=f"{user} broke the rules and got banned... imagine",color=nextcord.Color.magenta())
        # embed.set_thumbnail("https://cdn.discordapp.com/attachments/710864896153354301/1003965509299077140/712072450900230144.png")
        embed.set_image("https://cdn.discordapp.com/attachments/710864896153354301/1003845313842401350/unknown.jpeg")
        general = bot.get_channel(710573789309698060)
        await general.send(embed=embed)


bot.run("OTk5NzYwNDMwMDUyNDE3NjM4.GOfJE9.SzY__65AkGeN6rWRaTp4egYhl3gdWN6pm5my1g")