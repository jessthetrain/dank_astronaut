from nextcord import AllowedMentions
import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
import calendar
import datetime
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = Intents.default()
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
            await general.send(f"Everyone welcome {interaction.user.mention} to the server!\nOur next heist will be in <#1033765350006865930> :slight_smile:",allowed_mentions=mentions,delete_after=120)
        self.value = True

@bot.event
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

for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 688330308688543744:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"⚙ Loaded {extension} cog!")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(":x: This is an owner only command",delete_after=5)

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 688330308688543744:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"⚙ Unloaded {extension} cog!")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(":x: This is an owner only command",delete_after=5)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 688330308688543744:
        bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"⚙ Reloaded {extension} cog!")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(":x: This is an owner only command",delete_after=5)

@commands.has_role(805719483930771477)
@bot.command()
async def verification(ctx):
    embed = nextcord.Embed(title="Verification",description="Click the button below to get verified!",color=nextcord.Color.green())
    await ctx.channel.purge(limit=1)
    view = verifyButtons()
    await ctx.send(embed=embed,view=view)
    await view.wait()

@bot.event
async def on_member_join(member):
    embed = nextcord.Embed(title=f"Welcome to Dank Moon, {member}!",description=f"To get started in the server, read the rules in <#710840207808659517> and verify in <#741336727188144148>",color=nextcord.Color.magenta())
    embed.add_field(name="Once you have verified...",value="+ Get pings and other roles from <#711952053433401375>!\n+ Select your colour role in <#710847274988732507>!\n+ Chat with us in <#710573789309698060>!\n+ Our heists take place in <#711435197807067156>!\n+ See what we are giving away in <#711435312332537889> and <#809422611452919818>!")
    embed.set_footer(text="If you are here for a heist, don't freeload! We ban freeloaders :P")
    embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    await member.send(embed=embed)
    rulesChan = bot.get_channel(710840207808659517)
    await rulesChan.send(f"{member.mention}",delete_after=1)

@bot.event
async def on_member_ban(guild, user):
    if guild == bot.get_guild(710573788856582225):
        embed = nextcord.Embed(title=f"{user} broke the rules and got banned... imagine",color=nextcord.Color.magenta())
        # embed.set_thumbnail("https://cdn.discordapp.com/attachments/710864896153354301/1003965509299077140/712072450900230144.png")
        embed.set_image("https://cdn.discordapp.com/attachments/710864896153354301/1003845313842401350/unknown.jpeg")
        general = bot.get_channel(710573789309698060)
        await general.send(embed=embed)


bot.run(TOKEN)