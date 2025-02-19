import discord
import os
import sys
import asyncio
import aiohttp
from discord.ext import commands
import requests
import colorama
from colorama import Fore

# Config options 

PREFIX = "b!"
TOKEN = ""

# Main

intents = discord.Intents.default()

intents.members = True
intents.presences = True 
intents.message_content = True
    
bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents) 
version = "v1.0"
help_message = "" # modified later when the bot starts according to command info
support = f"OpenBTools {version}. DM @ainselu on Discord for support, and report any issues with the bot to our GitHub at https://github.com/ainselu/OpenBTools"

fonts = {
    "double-struck": {
        "a": "𝕒", "A": "𝔸",
        "b": "𝕓", "B": "𝔹",
        "c": "𝕔", "C": "ℂ",
        "d": "𝕕", "D": "𝔻",
        "e": "𝕖", "E": "𝔼",
        "f": "𝕗", "F": "𝔽",
        "g": "𝕘", "G": "𝔾",
        "h": "𝕙", "H": "ℍ",
        "i": "𝕚", "I": "𝕀",
        "j": "𝕛", "J": "𝕁",
        "k": "𝕜", "K": "𝕂",
        "l": "𝕝", "L": "𝕃",
        "m": "𝕞", "M": "𝕄",
        "n": "𝕟", "N": "ℕ",
        "o": "𝕠", "O": "𝕆",
        "p": "𝕡", "P": "ℙ",
        "q": "𝕢", "Q": "ℚ",
        "r": "𝕣", "R": "ℝ",
        "s": "𝕤", "S": "𝕊",
        "t": "𝕥", "T": "𝕋",
        "u": "𝕦", "U": "𝕌",
        "v": "𝕧", "V": "𝕍",
        "w": "𝕨", "W": "𝕎",
        "x": "𝕩", "X": "𝕏",
        "y": "𝕪", "Y": "𝕐",
        "z": "𝕫", "Z": "ℤ",
        "0": "𝟘", "1": "𝟙",
        "2": "𝟚", "3": "𝟛",
        "4": "𝟜", "5": "𝟝",
        "6": "𝟞", "7": "𝟟",
        "8": "𝟠", "9": "𝟡"
    },
    "sans-serif": {
        "a": "𝐚", "A": "𝐀",
        "b": "𝐛", "B": "𝐁",
        "c": "𝐜", "C": "𝐂",
        "d": "𝐝", "D": "𝐃",
        "e": "𝐞", "E": "𝐄",
        "f": "𝐟", "F": "𝐅",
        "g": "𝐠", "G": "𝐆",
        "h": "𝐡", "H": "𝐇",
        "i": "𝐢", "I": "𝐈",
        "j": "𝐣", "J": "𝐉",
        "k": "𝐤", "K": "𝐊",
        "l": "𝐥", "L": "𝐋",
        "m": "𝐦", "M": "𝐌",
        "n": "𝐧", "N": "𝐍",
        "o": "𝐨", "O": "𝐎",
        "p": "𝐩", "P": "𝐏",
        "q": "𝐪", "Q": "𝐐",
        "r": "𝐫", "R": "𝐑",
        "s": "𝐬", "S": "𝐒",
        "t": "𝐭", "T": "𝐓",
        "u": "𝐮", "U": "𝐔",
        "v": "𝐯", "V": "𝐕",
        "w": "𝐰", "W": "𝐖",
        "x": "𝐱", "X": "𝐗",
        "y": "𝐲", "Y": "𝐘",
        "z": "𝐳", "Z": "𝐙",
        "0": "𝟎", "1": "𝟏",
        "2": "𝟐", "3": "𝟑",
        "4": "𝟒", "5": "𝟓",
        "6": "𝟔", "7": "𝟕",
        "8": "𝟖", "9": "𝟗"
    },
    "sans-serif-bold": {
        "a": "𝗮", "A": "𝗔",
        "b": "𝗯", "B": "𝗕",
        "c": "𝗰", "C": "𝗖",
        "d": "𝗱", "D": "𝗗",
        "e": "𝗲", "E": "𝗘",
        "f": "𝗳", "F": "𝗙",
        "g": "𝗴", "G": "𝗚",
        "h": "𝗵", "H": "𝗛",
        "i": "𝗶", "I": "𝗜",
        "j": "𝗷", "J": "𝗝",
        "k": "𝗸", "K": "𝗞",
        "l": "𝗹", "L": "𝗟",
        "m": "𝗺", "M": "𝗠",
        "n": "𝗻", "N": "𝗡",
        "o": "𝗼", "O": "𝗢",
        "p": "𝗽", "P": "𝗣",
        "q": "𝗾", "Q": "𝗤",
        "r": "𝗿", "R": "𝗥",
        "s": "𝘀", "S": "𝗦",
        "t": "𝘁", "T": "𝗧",
        "u": "𝘂", "U": "𝗨",
        "v": "𝘃", "V": "𝗩",
        "w": "𝘄", "W": "𝗪",
        "x": "𝘅", "X": "𝗫",
        "y": "𝘆", "Y": "𝗬",
        "z": "𝘇", "Z": "𝗭",
        "0": "𝟬", "1": "𝟭",
        "2": "𝟮", "4": "𝟯",
        "4": "𝟰", "5": "𝟱",
        "6": "𝟲", "7": "𝟳",
        "8": "𝟴", "9": "𝟵",  
    },
    "italic": {
        "a": "𝘢", "A": "𝘈",
        "b": "𝘣", "B": "𝘉",
        "c": "𝘤", "C": "𝘊",
        "d": "𝘥", "D": "𝘋",
        "e": "𝘦", "E": "𝘌",
        "f": "𝘧", "F": "𝘍",
        "g": "𝘨", "G": "𝘎",
        "h": "𝘩", "H": "𝘏",
        "i": "𝘪", "I": "𝘐",
        "j": "𝘫", "J": "𝘑",
        "k": "𝘬", "K": "𝘒",
        "l": "𝘭", "L": "𝘓",
        "m": "𝘮", "M": "𝘔",
        "n": "𝘯", "N": "𝘕",
        "o": "𝘰", "O": "𝘖",
        "p": "𝘱", "P": "𝘗",
        "q": "𝘲", "Q": "𝘘",
        "r": "𝘳", "R": "𝘙",
        "s": "𝘴", "S": "𝘚",
        "t": "𝘵", "T": "𝘛",
        "u": "𝘶", "U": "𝘜",
        "v": "𝘷", "V": "𝘝",
        "w": "𝘸", "W": "𝘞",
        "x": "𝘹", "X": "𝘟",
        "y": "𝘺", "Y": "𝘠",
        "z": "𝘻", "Z": "𝘡",
    },
    "monospace": {
        "a": "𝚊", "A": "𝙰",
        "b": "𝚋", "B": "𝙱",
        "c": "𝚌", "C": "𝙲",
        "d": "𝚍", "D": "𝙳",
        "e": "𝚎", "E": "𝙴",
        "f": "𝚏", "F": "𝙵",
        "g": "𝚐", "G": "𝙶",
        "h": "𝚑", "H": "𝙷",
        "i": "𝚒", "I": "𝙸",
        "j": "𝚓", "J": "𝙹",
        "k": "𝚔", "K": "𝙺",
        "l": "𝚕", "L": "𝙻",
        "m": "𝚖", "M": "𝙼",
        "n": "𝚗", "N": "𝙽",
        "o": "𝚘", "O": "𝙾",
        "p": "𝚙", "P": "𝙿",
        "q": "𝚚", "Q": "𝚀",
        "r": "𝚛", "R": "𝚁",
        "s": "𝚜", "S": "𝚂",
        "t": "𝚝", "T": "𝚃",
        "u": "𝚞", "U": "𝚄",
        "v": "𝚟", "V": "𝚅",
        "w": "𝚠", "W": "𝚆",
        "x": "𝚡", "X": "𝚇",
        "y": "𝚢", "Y": "𝚈",
        "z": "𝚣", "Z": "𝚉",
        "0": "𝟶", "1": "𝟷",
        "2": "𝟸", "3": "𝟹",
        "4": "𝟺", "5": "𝟻",
        "6": "𝟼", "7": "𝟽",
        "8": "𝟾", "9": "𝟿",
    }
}
    
@bot.event
async def on_ready():
    print(f"{Fore.LIGHTWHITE_EX}[{Fore.GREEN}INFO{Fore.LIGHTWHITE_EX}] | Bot ready.{Fore.RESET}")

@bot.command(description="Displays bot latency.")
async def ping(ctx):
    await ctx.message.reply(f"Pong!\nLatency: {str(bot.latency)[:5]}")

@bot.command(description="Shows a list of commands")
async def help(ctx):
    await ctx.message.reply(help_message)

@bot.command(description=f"Clones a category. Usage: {PREFIX}cloneCategory (category id)")
@commands.has_permissions(manage_channels=True)
async def cloneCategory(ctx, category_id: int):
    category: discord.CategoryChannel = await bot.fetch_channel(category_id)
    await category.clone()
    await ctx.message.reply("Successfully cloned category")
    
@bot.command(description=f"Clones a category, including its channels. Usage: {PREFIX}cloneCategoryWithChannels (category id)")
@commands.has_permissions(manage_channels=True)
async def cloneCategoryWithChannels(ctx, category_id: int):
    category: discord.CategoryChannel = await bot.fetch_channel(category_id)
    new = await category.clone()
    for channel in category.channels:
        newChannel = await channel.clone()
        await newChannel.edit(category=new)
    await ctx.message.reply("Successfully cloned category with channels")

@bot.command(description=f"Prefixes all channels in a category with the given string. Usage: {PREFIX}prefixCategoryChannels (category id) (string)")
@commands.has_permissions(manage_channels=True)
async def prefixCategoryChannels(ctx, category_id: int, prefix: str):
    category: discord.CategoryChannel = await bot.fetch_channel(category_id)
    if not category:
        await ctx.message.reply("Category not found")
        return
    for channel in category.channels:
        await asyncio.create_task(channel.edit(name=prefix+channel.name))
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Suffixes all channels in a category with the given string. Usage: {PREFIX}suffixCategoryChannels (category id) (string)")
@commands.has_permissions(manage_channels=True)
async def suffixCategoryChannels(ctx, category_id: int, prefix: str):
    category = await bot.fetch_channel(category_id)
    if not category:
        await ctx.message.reply("Category not found")
        return
    for channel in category.channels:
        await asyncio.create_task(channel.edit(name=channel.name+prefix))
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Suffixes the given channel with the given string. Works for category channels also. Usage: {PREFIX}suffixChannel (channel id) (string)")
@commands.has_permissions(manage_channels=True)
async def suffixChannel(ctx, category_id: int, suffix: str):
    channel = await bot.fetch_channel(category_id)
    if not channel:
        await ctx.message.reply("Channel not found")
        return
    await asyncio.create_task(channel.edit(name=channel.name+suffix))
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Prefixes the given channel with the given string. Works for category channels also. Usage: {PREFIX}prefixChannel (channel id) (string)")
@commands.has_permissions(manage_channels=True)
async def prefixChannel(ctx, category_id: int, prefix: str):
    channel = await bot.fetch_channel(category_id)
    if not channel:
        await ctx.message.reply("Channel not found")
        return
    await asyncio.create_task(channel.edit(name=prefix+channel.name))
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Applies a font to the name of the given channel. Works for category channels also. Usage: {PREFIX}fontifyChannel (channel id) (font)")
@commands.has_permissions(manage_channels=True)
async def fontifyChannel(ctx, channel_id: int, font: str):
    if font not in fonts:
        await ctx.message.reply("Font not supported")
        return
    channel = await bot.fetch_channel(channel_id)
    new_name = ""
    for char in channel.name:
        if char in fonts[font]:
            new_name += fonts[font][char]
        else:
            new_name += char
    await channel.edit(name=new_name)
    await ctx.message.reply("Done!")
    return
    
@bot.command(description=f"Applies a font to all channels in the given category. Usage: {PREFIX}fontifyCategoryChannels (category id) (font)")
@commands.has_permissions(manage_channels=True)
async def fontifyCategoryChannels(ctx, category_id: int, font: str):
    if font not in fonts:
        await ctx.message.reply("Font not supported")
        return
    category = await bot.fetch_channel(category_id)
    for channel in category.channels:
        new_name = ""
        for char in channel.name:
            if char in fonts[font]:
                new_name += fonts[font][char]
            else:
                new_name += char
    await channel.edit(name=new_name)
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Clones a role. Usage: {PREFIX}cloneRole (role id)")
@commands.has_permissions(manage_roles=True)
async def cloneRole(ctx, role_id: int):
    role: discord.Role = ctx.guild.get_role(role_id)
    if not role:
        ctx.message.send("Role not found")
        return
    await ctx.guild.create_role(name=role.name, color=role.color, permissions=role.permissions, display_icon=role.display_icon, mentionable=role.mentionable)
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Applies a font to a role. Usage: {PREFIX}fontifyRole (role id) (font)")
@commands.has_permissions(manage_roles=True)
async def fontifyRole(ctx, role_id: int, font: str):
    role: discord.Role = ctx.guild.get_role(role_id)
    if not role:
        ctx.message.send("Role not found")
        return
    new_name = ""
    for char in role.name:
        if char in fonts[font]:
            new_name += fonts[font][char]
        else:
            new_name += char
    await role.edit(name=new_name)
    await ctx.message.reply("Done!")
    return

@bot.command(description=f"Displays all available fonts.")
async def listFonts(ctx):
    await ctx.message.reply("""```
=========================
| > Fonts List
=========================
| > double-struck : "𝔽𝕠𝕟𝕥 𝔼𝕩𝕒𝕞𝕡𝕝𝕖"
| > sans-serif : "𝐅𝐨𝐧𝐭 𝐄𝐱𝐚𝐦𝐩𝐥𝐞"
| > sans-serif-bold : "𝗙𝗼𝗻𝘁 𝗘𝘅𝗮𝗺𝗽𝗹𝗲"
| > italic : "𝘍𝘰𝘯𝘵 𝘌𝘹𝘢𝘮𝘱𝘭𝘦"
| > monospace : "𝙵𝚘𝚗𝚝 𝙴𝚡𝚊𝚖𝚙𝚕𝚎"
=========================```""")

@bot.command(description=f"Tech support.")
async def support(ctx):
    await ctx.message.reply(support)
    
print(f"{Fore.LIGHTWHITE_EX}[{Fore.GREEN}INFO{Fore.LIGHTWHITE_EX}] | Getting ready...{Fore.RESET}")
help_message = f"""```
=========================
| > OpenBTools {version}
=========================\n"""
for command in bot.commands:
    help_message += f"| > {PREFIX}{command.name} : {command.description}\n"
help_message += "=========================```"
    
bot.run(TOKEN)