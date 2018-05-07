import Translate as tl

import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from boto.s3.connection import S3Connection

client = commands.Bot(command_prefix = "!")
changed = False

@client.event
async def on_ready():
	print("Bot is ready")
	
	vc = discord.utils.find(client.server.channels, id="434172171644960778")

#Update new members' nicknames and roles
@client.event
async def on_member_join(member):
	await client.change_nickname(member, tl.fullwidth(member.display_name))
	defaultRole = discord.utils.get(member.server.roles, id="442109941034123294")
	await client.add_roles(member, defaultRole)
	
#Make all nicknames Ａ Ｅ Ｓ T Ｈ Ｅ T Ｉ Ｃ
@client.event
async def on_member_update(before, after):
	global changed
	
	#Prevent loops in changing nicknames
	if not(changed):
		await client.change_nickname(after, tl.fullwidth(after.nick))
		changed = True
	else:
		changed = False

@client.event
async def on_message(message):
	
	command = message.content.lower()

	aestheticMessage = message.content.split("&")
	
	if message.channel.id == "434172182193504268":
		await client.delete_message(message)
	
	elif command.startswith("&brianfact"):
		script = open("Scripts/BrianFacts.txt", "r")
		facts = str(script.read()).splitlines()
		script.close()
		factIndex = int(random.randrange(len(facts)))
		await client.send_message(message.channel,message.author.nick + ":   " + tl.fullwidth(facts[factIndex]))
	
	elif command.startswith("&help"):
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

client.run(os.environ["BOT_KEY"])
