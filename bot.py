
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing!")

# Configure intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Connected to {len(bot.guilds)} server(s)")
    print("Bot is ready!")


@bot.event
async def on_member_join(member):

    role_name = "Supporter"

    role = discord.utils.get(
        member.guild.roles,
        name=role_name
    )

    if role is None:
        print(
            f"ERROR: Role '{role_name}' not found "
            f"in {member.guild.name}"
        )
        return

    try:
        await member.add_roles(
            role,
            reason="Automatic supporter role assignment"
        )

        print(
            f"SUCCESS: Assigned '{role_name}' to "
            f"{member} in {member.guild.name}"
        )

    except discord.Forbidden:
        print(
            f"PERMISSION ERROR: Cannot assign "
            f"'{role_name}' in {member.guild.name}"
        )

    except discord.HTTPException as error:
        print(f"DISCORD API ERROR: {error}")


bot.run(TOKEN)
