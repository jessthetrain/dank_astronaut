from sre_constants import SUCCESS
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord import Intents
import os
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
nextcord.http._modify_api_version(9)
bot = commands.Bot(command_prefix=["<@999760430052417638> ", "a.", "A."], case_insensitive=True,intents=intents)
dankMoon = 710573788856582225

@bot.event # This event prints in the console when the bot has logged in
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = await bot.fetch_channel(996446872451432498)
    startupEmbed = nextcord.Embed(title="The bot has started!", description="Hi **Stones**! The bot has now started. Feel free to use `a.help` to see what I can do!",color=nextcord.Color.magenta())
    startupEmbed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    await channel.send(embed=startupEmbed)

@bot.command(aliases = ["av", "pfp"]) # Avatar command
async def avatar(ctx, user: nextcord.Member=None):
    if user == None:
        user = ctx.message.author
    embed = nextcord.Embed(title=f"Avatar of {user}", color=nextcord.Color.random())
    embed.set_image(url=str(user.avatar))
    await ctx.send(embed=embed)

@bot.command() # Command to see the bot's ping in an embed
async def ping(ctx):
    embed = nextcord.Embed(title="Pong! 🏓", description=f"{round(bot.latency * 1000, 1)}ms", color=nextcord.Color.magenta())
    await ctx.reply(embed=embed)

@bot.event
async def on_member_join(member):
    embed = nextcord.Embed(title=f"Welcome to Dank Moon, {member}!",description=f"To get started in the server, read the rules in <#710840207808659517> and verify in <#741336727188144148>",color=nextcord.Color.magenta())
    embed.add_field(name="Once you have verified...",value="+ Get pings and other roles from <#711952053433401375>!\n+ Select your colour role in <#710847274988732507>!\n+ Chat with us in <#710573789309698060>!\n+ Our heists take place in <#711435197807067156>!\n+ See what we are giving away in <#711435312332537889> and <#809422611452919818>!")
    embed.set_footer(text="If you are here for a heist, don't freeload! We ban freeloaders :P")
    embed.set_thumbnail("https://cdn.discordapp.com/attachments/996446872451432498/999801982770491522/dank_moon.png")
    await member.send(embed=embed)
    rulesChan = bot.get_channel(710840207808659517)
    await rulesChan.send(f"{member.mention}",delete_after=1)

class verifyButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value=None
    
    @nextcord.ui.button(label="Verify!",style=nextcord.ButtonStyle.green,emoji="✅")
    async def verify(self, button:nextcord.ui.button,interaction:nextcord.Interaction):
        guild = bot.get_guild(710573788856582225)
        verified = guild.get_role(741336292612243603)
        await interaction.user.add_roles(verified)
        await interaction.response.send_message(ephemeral=True,content="You have been verfied successfully!")
        self.value = True
        self.stop

@commands.has_role(805719483930771477)
@bot.command()
async def verification(ctx):
    embed = nextcord.Embed(title="Verification",description="Click the button below to get verified!",color=nextcord.Color.green())
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=1,check=lambda m:m.author==bot.user)
    view = verifyButtons()
    await ctx.send(embed=embed,view=view)
    await view.wait()

bot.run("OTk5NzYwNDMwMDUyNDE3NjM4.GOfJE9.SzY__65AkGeN6rWRaTp4egYhl3gdWN6pm5my1g")