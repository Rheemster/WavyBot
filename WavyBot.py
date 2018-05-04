import Translate as tl

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
if not discord.opus.is_loaded():
	discord.opus.load_opus('opus')

client = commands.Bot(command_prefix = "!")

#Variable to prevent loops in changing nicknames
changed = 0

@client.event
async def on_ready():
	print("Bot is ready")
	voiceChannel = client.get_channel("411703796700413952")

#Update new members' nicknames and roles
@client.event
async def on_member_join(member):
	await client.change_nickname(member, tl.fullwidth(member.display_name))
	role = discord.utils.get(server.roles, "243126303551782912")
	await client.add_roles(member, role)

#Make all nicknames Ａ Ｅ Ｓ T Ｈ Ｅ T Ｉ Ｃ
@client.event
async def on_member_update(before, after):
	global changed
	
	#Prevent loops in changing nicknames
	if changed == 0:
		await client.change_nickname(after, tl.fullwidth(after.nick))
		changed = 1
	else:
		changed = 0

@client.event
async def on_message(message):
	
	command = message.content.lower()

	aestheticMessage = message.content.split("&")

	if command.startswith("&help"):
		script = open("Scripts/Help.txt", "r")
		await client.send_message(message.channel,script.read())
		script.close()
	
	elif command.startswith("&functions"):
		script = open("Scripts/Functions.txt", "r")
		await client.send_message(message.channel,script.read())
		script.close()
	
	elif command.startswith("&wavy"):
		await client.send_message(message.channel, message.author.nick + ":   " + tl.fullwidth(message.content[5:]))
		await client.delete_message(message)
	
	elif len(aestheticMessage) > 2 and message.author != client.user:		
		
		finalMessage = tl.brokenTranslate(aestheticMessage)

		await client.send_message(message.channel, message.author.nick + ":   " + finalMessage)
		await client.delete_message(message)

client.run(process.env.BOT_TOKEN)