import main
import os
from discord.ext import commands
client = commands.Bot(command_prefix='g!')


@client.event
async def on_ready():
	print("Bot is ready")


@client.command()
async def male(ctx):
	await ctx.send(main.generate(main.reset(), "m"))


@client.command()
async def female(ctx):
	await ctx.send(main.generate(main.reset(), "f"))


@client.command()
async def list(ctx):
	await ctx.send(main.generate(main.reset(), "l"))


client.run(os.environ['OAUTH_TOKEN'])
