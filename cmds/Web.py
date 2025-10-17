from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from core import Cog_Extension
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
url1 = "https://www2.ck.tp.edu.tw/"
url2 = "https://sschool.tp.edu.tw/Login.action?schNo=353301"
url3 = "https://sprout.tw/spt/"
class Web(Cog_Extension):
    @commands.command()
    async def ck_announcement(self,ctx):
        content1 = requests.get(url1)
        doc = BeautifulSoup(content1.text, "html.parser")
        node=doc.find("div")
        for child in node.children:
            if child.find("section"):
                child=doc.find("section")
                for C in child.children:
                    if C.find("h4"):
                        C=doc.find_all("h4")
                    for CC in C:
                        ans=CC.get_text()
                        await ctx.send(ans+"-")
        await ctx.send("https://www2.ck.tp.edu.tw/")
                    
    @commands.command()
    async def sp_va(self,ctx):
        browser = webdriver.Chrome("C:/Users/chens/Downloads/DCBot/chromedriver.exe")
        browser.get("https://sprout.tw/py2022/#!index.md")
        
        time.sleep(1)
        link = browser.find_element(By.LINK_TEXT, "請假表單")
        link.click()
        source = browser.page_source
        doc = BeautifulSoup(source, "html.parser")
        print(doc.prettify())
    @commands.command()
    async def sp_main(self,ctx):
        await ctx.send("資牙官網:https://sprout.tw/spt/")
def setup(bot):
    bot.add_cog(Web(bot))
