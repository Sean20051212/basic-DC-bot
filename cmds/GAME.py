
from discord.ext import commands
from core import Cog_Extension
import random
import discord
from dotenv import load_dotenv
from discord import User

bot = commands.Bot(command_prefix ="$")
user = discord.Client()
load_dotenv()
game_started=False
co=0
t=0
ans=1111
class GAME(Cog_Extension):
    @commands.command()
    async def Game(self, ctx, member:discord.Member): 
        def __init__(self, client):
            self.client = client
        global f1 ,f2 ,f3 ,f4,game_started,t,N
        User=member
        N=User.name
        if game_started==True:
            await ctx.send("遊戲已經開始啦!")
        game_started=True
        self._last_member = None
        f1=random.randint(1,9)
        f2=random.randint(1,9)
        while f2==f1:
            f2=random.randint(1,9)
        f3=random.randint(1,9)
        while f3==f1 or f3==f2:
            f3=random.randint(1,9)
        f4=random.randint(1,9)
        while f4==f1 or f4==f2 or f4==f2:
            f4=random.randint(1,9)
        await ctx.send("請猜一個不含0、數字不重複的四位數")
    @commands.command()
    async def ans(self,ctx,A):
        global game_started,t,N
        if game_started==True:
            print(f"偷偷告訴你，答案是{1000*f1+100*f2+10*f3+f4}")
            if A !=(1000*f1+100*f2+10*f3+f4):
                co=0
                if str(f1) ==str(A)[0]:
                    co+=1
                if str(f2) ==str(A)[1]:
                    co+=1
                if str(f3) ==str(A)[2]:
                    co+=1
                if str(f4) ==str(A)[3]:
                    co+=1
                await ctx.send(f"答對了{co}個字，答錯了{4-co}個字")
                t+=1
                if co==4:
                    await ctx.send("成功答對啦!遊戲結束!")
                    game_started=False
                    with open("./game save.txt", 'a') as A:
                        print(f"{t}次過關 挑戰者{N}",file=A,end="\n")
                    with open("./game save.txt", 'r') as R:
                        A_lines=R.readlines()
                    with open("./game save.txt", 'w') as W:
                        for L in sorted(A_lines):
                            print(L,file=W,end="")
                    t=0
        else:
            await ctx.send("遊戲未開始，請用$game指令開始遊戲")
    @commands.command()
    async def stop_game(self,ctx):
        global game_started,t
        game_started=False
        t=0
        await ctx.send("遊戲結束!")
    @commands.command()
    async def place(self,ctx):
        global t,N
        with open("./game save.txt", 'r') as R:
            A_lines=R.readlines()
            for i in A_lines:
                await ctx.send(i)
        
def setup(bot):
    bot.add_cog(GAME(bot))
