from discord import Embed
import config
from logging import getLogger, DEBUG, FileHandler, Formatter
from nextcord import Intents, Status, Streaming,ButtonStyle,Interaction
from nextcord.ext import commands
from nextcord.ui import button, Button, View

from os import listdir
from asyncio import run

class Verify(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="💙", style=ButtonStyle.blurple, custom_id="verify", row=1)
    async def Verify(self, button: Button, interaction: Interaction):
        await interaction.user.add_roles(interaction.guild.get_role(config.Verify))
        

logger = getLogger("nextcord")
logger.setLevel(DEBUG)
handler = FileHandler(filename="log/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

intent = Intents.default()
intent.members = True
React = commands.Bot(
    command_prefix=config.Bot_prefix,
    case_insensitive=True,
    help_command=None,
    intents=intent,
    strip_after_prefix=True,
)

@React.command()
async def setup(ctx: commands.Context):
    if ctx.author.guild_permissions.administrator:
        embed = Embed(
            title = "ยืนยันตัวตน",
            color= 0xfed000,
            description="""
> **กดปุ่มสีฟ้าเพื่อยืนยันตัวตนเเละเข้าสู่เซิฟเวอร์**    
            """
        )
        await ctx.send(embed=embed,view=Verify())
@React.event
async def on_connect():
    print("Connected to discord API")


@React.event
async def on_ready():
    React.add_view(Verify())
    print(f"{React.user} is online")
    await React.change_presence(
        status=Status.idle,
        activity=Streaming(
            name="บอทร้านค้าระบบสุดเเน่นโดย𝘾𝘼𝙎𝙏𝙇𝙀 𝙊𝙁 𝘿𝘼𝙍𝙆",
            url="https://www.twitch.tv/smilewinbot",
        ),
    )


if __name__ == "__main__":
    React.run(config.Bot_token, reconnect=True)
