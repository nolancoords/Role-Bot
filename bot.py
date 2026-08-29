import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN           = os.getenv("DISCORD_TOKEN")
intents         = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is ready!")

@bot.event
async def on_member_join(member):
    role_name = "ODG Supporter"

    role = discord.utils.get(
        member.guild.roles,
        name=role_name
    )

    # Role doesn't exist
    if role is None:
        print(
            f"ERROR: Could not find the '{role_name}' role "
            f"in {member.guild.name}."
        )
        return

    # Try to assign the role
    try:
        await member.add_roles(role)

        print(
            f"Assigned '{role_name}' to "
            f"{member} in {member.guild.name}"
        )

    except discord.Forbidden:
        print(
            f"ERROR: I don't have permission to assign "
            f"the '{role_name}' role."
        )

    except discord.HTTPException as error:
        print(
            f"ERROR: Discord API error while assigning "
            f"the role: {error}"
        )

# Make sure the token exists
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing from .env")

bot.run(TOKEN)