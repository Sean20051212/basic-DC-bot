import discord
from discord.ext import commands
import os
from core import Cog_Extension
import time

core_directory = 'C:/Users/chens/Downloads/DCBot/core.py'

song_directory = 'C:/Users/chens/Downloads/DCBot/Song_save.txt'

ffmpeg_directory = 'C:/Users/chens/Downloads/DCBot/ffmpeg.exe'

class Music(Cog_Extension):
      
    @commands.command()
    async def Play(self,ctx):
        song_exist = os.path.isfile("Song.mp3")
        if song_exist:
            os.remove("Song.mp3")
        with open(song_directory, 'r') as songread:
            songlist=songread.readlines()
            if len(songlist)==0:
                await ctx.send("目前歌單內沒有歌曲喔!")
                exit
            else:
                firstsong=songlist[0]
                print(firstsong,songlist)
                listlenth=len(songlist)
                for playmusic in range(listlenth):
                    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
                    if not voice:
                        channel = ctx.author.voice.channel
                        voice=await channel.connect()
                    t=0
                    while voice.is_playing():
                        time.sleep(5)
                        t+=1
                        if t==5:
                            await ctx.send(".")
                            t=0
                    song_exist = os.path.isfile("Song.mp3")
                    if song_exist:
                        os.remove("Song.mp3")
                    if voice is None:
                        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='重考解題專區')
                        await voiceChannel.connect(timeout = 600.0)
                        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
                    
                    os.system(f"yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 {firstsong}")

                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            
                            os.rename(file, "Song.mp3")
                
                    voice.play(discord.FFmpegPCMAudio(executable =ffmpeg_directory, source = "Song.mp3"))
                    
                    songlist.remove(firstsong)
                    with open(song_directory, 'w') as songread2:
                        for sr2 in songlist:
                            print(sr2,file=songread2,end="")
                    with open(song_directory, 'r') as songread3:
                        songlist=songread3.readlines()
                        if len(songlist)==0:
                            await ctx.send("目前歌單內沒有歌曲喔!")
                            exit
                        else:
                            firstsong=songlist[0]
                        print(firstsong,songlist)
                        
    @commands.command()
    async def leave(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
                await voice.disconnect()
        except:
            await ctx.send("我不在語音頻道內喔!")


    @commands.command()
    async def pause(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try: 
            if voice.is_playing():
                voice.pause()
            else:
                await ctx.send("沒有任何正在播放的音樂!")
        except:
            await ctx.send("我不在語音頻道內喔!")


    @commands.command()
    async def resume(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            if voice.is_paused():
                voice.resume()
            else:
                await ctx.send("音樂沒被暫停呀?")
        except:
            await ctx.send("我不在語音頻道內喔!")

    @commands.command()
    async def stop(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            voice.stop()
        except:
            await ctx.send("我不在語音頻道內喔!")



def setup(bot):
    bot.add_cog(Music(bot))