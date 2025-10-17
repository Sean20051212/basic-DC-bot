import discord
from discord.ext import commands
import os
from core import Cog_Extension

class TODO(Cog_Extension):
    @commands.command()
    async def ADD(self,ctx,date,something):#something必須是英文
        with open("./TODO_save.txt", 'a') as AA:
            print(f"{date} {something}",file=AA,end="\n")
        with open("./TODO_save.txt", 'r') as AR:
            A_lines=AR.readlines()
        with open("./TODO_save.txt", 'w') as AW:
            for L in sorted(A_lines):
                print(L,file=AW,end="")
        await ctx.send(f"日期:{date}，事件:{something}已上傳")
    
    @commands.command()
    async def DEL(self,ctx,date,something):
        Del=False
        with open("./TODO_save.txt", 'r') as DR:
            D_lines=DR.readlines()
            print(D_lines)
            if f"{date} {something}" in D_lines:
                lot=D_lines.index(f"{date} {something}")
                Del=True
            elif f"{date} {something}\n" in D_lines:
                lot=D_lines.index(f"{date} {something}\n")
                Del=True
            else:
                await ctx.send(f"日期:{date}，事件:{something}不存在")
        if Del==True:
            with open("./TODO_save.txt", 'w') as DW:
                D_lines.pop(lot)
                for i in D_lines:
                    print(i,file=DW)
            await ctx.send(f"日期:{date}，事件:{something}已刪除")
        Del=False
    @commands.command()
    async def SHOW(self,ctx):
        with open("./TODO_save.txt", 'r') as SR:
            show=SR.readlines()
            await ctx.send("你的TODO list")
            print(show)
            if len(show)==0 or show==["\n"]:
                await ctx.send("是空的")
                return
            for S in show:
                await ctx.send(S)
            for g in show:
                    print(g,file=SR)
    @commands.command()
    async def CLEAR(self,ctx):
        with open("./TODO_save.txt", 'w') as CR:
            print("",file=CR)
        await ctx.send("ALL TODO list cleared")
def setup(bot):
    bot.add_cog(TODO(bot))