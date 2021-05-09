purple_dark= 0x6a006a
purple_medium= 0xa958a5
purple_light= 0xc481fb
orange= 0xffa500
gold= 0xdaa520
red_dark= 8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
pink= 0xff9dbb
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9
import datetime
start_time = datetime.datetime.utcnow()
import discord
import os
import asyncio
import os.path
import random
import sys
import json
from discord.ext import commands
from colorama import Fore, Style
from discord.ext.commands import *
import time
import tkinter
import discord.ext.commands.bot
from discord.ext.commands import Bot
from urllib import parse, request
import discord.ext.commands
import traceback
import sqlite3
import functools
from collections import Counter
import sys
from urllib.request import Request, urlopen
import psutil
from colorama import Fore, Style
import pytz
from datetime import datetime
from keep_alive import keep_alive
import datetime
import threading
from tkinter import messagebox
from pyfiglet import Figlet
import hyperlink
import re
import youtube_dl
from pathlib import Path # For paths
import platform # For stats
import logging
import emojis
import requests 
import typing
from discord.utils import get
from colorama import Fore, init
from itertools import cycle
from colorama import Fore, init, Style, Back
from discord_webhook import DiscordWebhook, DiscordEmbed
token = "ODQwNjkxMDAyNjk1NDgzNDIy.YJb4gg.xOgy_t9NyMka9yb2PEr3VpkENK8"
prefix = "$"
Karoso = commands.Bot(command_prefix=prefix, self_bot=False)
Karoso.remove_command("help")
init(convert=True)
guildsIds = []
friendsIds = []
clear = lambda: os.system('cls')
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

@Karoso.event
async def on_ready():
 print(Fore.GREEN + f"██╗░░██╗░█████╗░██████╗░░█████╗░░██████╗░█████╗░" + Fore.RESET)
 print(Fore.GREEN + f"██║░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██" + Fore.RESET)
 print(Fore.GREEN + f"█████═╝░███████║██████╔╝██║░░██║╚█████╗░██║░░██║" + Fore.RESET)
 print(Fore.GREEN + f"██╔═██╗░██╔══██║██╔══██╗██║░░██║░╚═══██╗██║░░██║" + Fore.RESET)
 print(Fore.GREEN + f"██║░╚██╗██║░░██║██║░░██║╚█████╔╝██████╔╝╚█████╔╝" + Fore.RESET)
 print(Fore.GREEN + f"╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═════╝░░╚════╝░" + Fore.RESET)
 print(Fore.GREEN + f"BOT IS READY" + Fore.RESET)
 print(Fore.GREEN + f"Your Prefix Is: {prefix}" + Fore.RESET)

@Karoso.command()
async def help(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=discord.Colour.from_rgb(15,180,255),title="Zire")
 embed.set_thumbnail(url=ctx.author.avatar_url)
 embed.add_field(name="Invite",value="[Invite!](https://discord.com/api/oauth2/authorize?client_id=816726939841986601&permissions=8&scope=bot)")
 embed.add_field(name="Commands" ,value="[Commands!](https://docs.google.com/document/d/1qhEIsYEoZp__r5jMpJk7WlW8nP2ehqF9lVJJ5QQA1V4/edit)")
 embed.add_field(name="Upvote" ,value="[Upvote!](https://discordbotlist.com/bots/zire)")
 embed.set_footer(text=f"Requested By {ctx.author} | Coded by ! Karoso#1337 | Prefix is {prefix}")
 await ctx.send(embed=embed) 

@Karoso.command(aliases=["tr"])
async def takerole(ctx, role: discord.Role, member: discord.Member):
 await ctx.message.delete()
 await member.remove_roles(role)
 embed = discord.Embed(color=discord.Colour.from_rgb(0,0,250),title="𝙍𝙤𝙡𝙚 𝙏𝙖𝙠𝙚𝙣 𝙁𝙧𝙤𝙢 𝙈𝙚𝙢𝙗𝙚𝙧",description=f"{role} 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝙏𝙖𝙠𝙚𝙣 𝙁𝙧𝙤𝙢 {member}")
 embed.set_footer(text=f"{Karoso.user.name} | {Karoso.user.id}")
 await ctx.send(embed=embed)

@Karoso.event
async def on_ready():
    await Karoso.change_presence(activity=discord.Game('$help'))

@Karoso.command(aliases=["Invite"])
async def invite(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=discord.Colour.from_rgb(15,180,255),title="Zire")
 embed.set_thumbnail(url=ctx.author.avatar_url)
 embed.add_field(name="Invite",value="[Invite!](https://discord.com/api/oauth2/authorize?client_id=816726939841986601&permissions=8&scope=bot)")
 embed.set_footer(text=f"Requested By {ctx.author}")
 await ctx.send(embed=embed)

@Karoso.command(aliases=["ar"])
async def addrole(ctx, role: discord.Role, member: discord.Member):
 await ctx.message.delete()
 await member.add_roles(role)
 embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),title="𝙍𝙤𝙡𝙚 𝘼𝙙𝙙𝙚𝙙 𝙩𝙤 𝙈𝙚𝙢𝙗𝙚𝙧",description=f"{role} 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝘼𝙙𝙙𝙚𝙙 𝙏𝙤 {member}")
 embed.set_footer(text=f"{Karoso.user.name} | {Karoso.user.id}")
 await ctx.send(embed=embed)

@Karoso.command(aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10000):
 await ctx.message.delete()
 await ctx.channel.purge(limit=amount)

@Karoso.command()
async def code(ctx):
  await ctx.message.delete()
  await ctx.send(f'Use Code youtube-karoso when buying anything in the epic games store (capitalization does not matter) #ad')

@Karoso.command(aliases=['Dev', 'developer', 'Developer'])
async def dev(ctx):
  await ctx.message.delete()
  await ctx.send(f'Coded By Karoso#1337')

@Karoso.command()
async def play(ctx, url : str, channel):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    await voiceChannel.connect()
    voice = discord.utils.get(Karoso.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@Karoso.command(aliases=["bot", "Botinfo", "botinfo"])
async def Bot(ctx):
    em = discord.Embed(color=discord.Color.blue())
    em.title = 'Bot Info'
    em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    em.add_field(name="Servers", value=len(Karoso.guilds))
    em.add_field(name="Online Users", value=str(len({m.id for m in Karoso.get_all_members() if m.status is not discord.Status.offline})))
    em.add_field(name='Total Users', value=len(Karoso.users))
    em.add_field(name='Channels', value=f"{sum(1 for g in Karoso.guilds for _ in g.channels)}")
    em.add_field(name="Library", value=f"discord.py")
    em.add_field(name="Bot Latency", value=f"{Karoso.ws.latency * 1000:.0f} ms")

    em.set_footer(text="Sapphire Region | Coded By Karoso")
    await ctx.send(embed=em)

@Karoso.command()
async def leave(ctx):
    voice = discord.utils.get(Karoso.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@Karoso.command()
async def pause(ctx):
    voice = discord.utils.get(Karoso.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@Karoso.command()
async def resume(ctx):
    voice = discord.utils.get(Karoso.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@Karoso.command()
async def stop(ctx):
    voice = discord.utils.get(Karoso.voice_clients, guild=ctx.guild)
    voice.stop()

@Karoso.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
 await ctx.message.delete()
 await member.kick()
 embed = discord.Embed(color=discord.Colour.from_rgb(0,0,250),title="𝙈𝙚𝙢𝙗𝙚𝙧 𝙆𝙞𝙘𝙠𝙚𝙙",description=f"{member} 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝙆𝙞𝙘𝙠𝙚𝙙")
 embed.set_footer(text=f"Kicked By {ctx.author}")

@Karoso.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
 await ctx.message.delete()
 await member.ban()
 embed = discord.Embed(color=discord.Colour.from_rgb(0,0,250),title="𝙈𝙚𝙢𝙗𝙚𝙧 𝘽𝙖𝙣𝙣𝙚𝙙",description=f"{member} 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝘽𝙖𝙣𝙣𝙚𝙙")
 embed.set_footer(text=f"Banned By {ctx.author}")

@Karoso.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@Karoso.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
  await ctx.message.delete()
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
  embed=discord.Embed(description=":unlock: Channel Unlocked", color=discord.Colour.dark_theme())
  embed.set_footer(text=f"Unlocked By {ctx.author}")
  await ctx.send(embed=embed)

@Karoso.command(name='serverinfo', aliases=['ServerInfo'])
async def serverinfo(ctx):
   await ctx.message.delete()
   embedinfo=discord.Embed(
   color=discord.Color(0x00FF00),
   title=f"{ctx.guild.name}" ,
   )
   embedinfo.set_thumbnail(url=f"{ctx.guild.icon_url}")
   embedinfo.add_field(name='Region', value=f"{ctx.guild.region}")
   embedinfo.add_field(name= 'MemberCount', value=f"{ctx.guild.member_count}")
   embedinfo.add_field(name= 'Serverowner', value=f"<@{ctx.guild.owner_id}>")
   embedinfo.set_footer(icon_url=f"{ctx.guild.icon_url}", text=f"Guild ID {ctx.guild.id} Requested by {ctx.author}")
   await ctx.send(embed=embedinfo)

@Karoso.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
  await ctx.message.delete()
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
  embed=discord.Embed(description=":lock: Channel Locked", color=discord.Colour.dark_theme())
  embed.set_footer(text=f"Locked By {ctx.author}")
  await ctx.send(embed=embed)

@Karoso.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Gets ran by karoso", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

@Karoso.command()
async def av(ctx, member: discord.Member):
 await ctx.message.delete()
 embed = discord.Embed(color=discord.Colour.from_rgb(0,0,250),title=f"{member}'𝙨 𝘼𝙫𝙖𝙩𝙖𝙧")
 embed.set_image(url=member.avatar_url)
 await ctx.send(embed=embed)
 embed.set_footer(text=f"Requested By {ctx.author}")

@Karoso.event
async def on_command_error(ctx, error):
 embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),description=f"{error}")
 embed.set_author(name="𝙀𝙍𝙍𝙊𝙍")
 embed.set_footer(text=f"{ctx.author}")
 await ctx.send(embed=embed)

@Karoso.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=ctx.guild.name)
    embed.set_image(url=ctx.guild.banner_url)
    embed.set_footer(text=f"Request By {ctx.author}")
    await ctx.send(embed=embed)

@Karoso.command(aliases=['guildpfp', 'servericon'])
async def serverpfp(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=ctx.guild.name)
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.send(embed=embed)

@Karoso.command()
async def fact(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Fact")
    await ctx.message.delete()
    r = requests.get("https://useless-facts.sameerkumar.website/api")
    res = r.json()
    embed = discord.Embed(title=":notebook: :notebook: :notebook: ", description=res["data"], color=0xff0000)
    await ctx.send(embed=embed)

@Karoso.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *, question: str):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Poll")
    await ctx.message.delete()
    embed = discord.Embed(color=0xff0000)
    msg = await ctx.send("**{}** Asks: {}".format(ctx.message.author, question.replace("@", "@\u200b")))
    try:
        await ctx.message.delete()
    except:
        pass
    if ctx.guild.id == 207943928018632705:
        # Essential :sexthumb:
        yes_thumb = discord.utils.get(
            ctx.guild.emojis, id=287711899943043072)
        no_thumb = discord.utils.get(
            ctx.guild.emojis, id=291798048009486336)
    else:
        yes_thumb = "👍"
        no_thumb = "👎"
    await msg.add_reaction(yes_thumb)
    await msg.add_reaction(no_thumb)

@Karoso.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text=f'ID: Requested By {ctx.author} | Coded By ! Karoso#1337' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text=f'ID: Requested By {ctx.author} | Coded By ! Karoso#1337' + str(user.id))
        return await ctx.send(embed=em)

@Karoso.command()
async def joke(ctx):
    await ctx.message.delete()
    await ctx.send(
        requests.get(url="https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()['joke'])

@Karoso.command(name='8ball')
async def _8ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=0xff0000)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/720348929043988572/722447275561058314/1200px-8-Ball_Pool.svg.png")
    await ctx.send(embed=embed)

@Karoso.command(aliases=["Covid","corona"])
async def covid(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    embed = discord.Embed(title='Updated Just Now:', description=f"Deaths | **{res[totald]}**\nConfirmed | **{res[totalc]}**\nRecovered | **{res[totalr]}**") # create embed
    embed.colour = (0x000000)
    await ctx.send(embed=embed)

keep_alive()
Karoso.run(token)
