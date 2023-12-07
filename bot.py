import asyncio
import discord
import os
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot = Bot(command_prefix='/', intents=intents)

async def load():
	for cog_file in os.listdir('./cogs'):
		if cog_file.endswith(".py"):
			try:
				await bot.load_extension(f'cogs.{cog_file[:-3]}')
				print(f'Loaded {cog_file}')
			except Exception:
				print(f'Failed to load {cog_file}')
				
async def main():
	await load()
	await bot.start(os.getenv('DISCORD_TOKEN'))

asyncio.run(main())