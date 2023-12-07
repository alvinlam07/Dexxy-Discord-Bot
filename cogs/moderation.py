import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\n{self.bot.user.name} is up and running!\n")
        
        # show server(s) bot is in
        print("Connected Servers: ")
        guilds = self.bot.guilds
        for guild in guilds:
            print(" - " + guild.name)

async def setup(bot):
    await bot.add_cog(Moderation(bot))