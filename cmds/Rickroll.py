import discord
from discord.ext import commands
import os
from core import Cog_Extension
u="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
U="https://www.youtube.com/watch?v=ETOGjHMMM3E"
class RickRoll(Cog_Extension):
        
    @commands.command()
    async def rickroll(self, ctx):
        song_exist = os.path.isfile("song.mp3")
        try:
            if song_exist:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice is None:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='好滑好嫩')
            await voiceChannel.connect(timeout = 600.0)
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        
        os.system(f"yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 {u}")

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
    
        voice.play(discord.FFmpegPCMAudio(executable = 'ffmpeg.exe', source = "song.mp3"))

    @commands.command()
    async def not_rickroll(self, ctx):
        song_exist = os.path.isfile("song.mp3")
        try:
            if song_exist:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        
        os.system(f"yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 {U}")

        if voice is None:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='好滑好嫩')
            await voiceChannel.connect(timeout = 600.0)
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
    
        voice.play(discord.FFmpegPCMAudio(executable = 'ffmpeg.exe', source = "song.mp3"))
    @commands.command()
    async def stop_rickroll(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
                await voice.disconnect()
        except:
            await ctx.send("The bot is not connected to a voice channel.")
    
def setup(bot):
    bot.add_cog(RickRoll(bot))