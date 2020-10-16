import os
import random
from dotenv import load_dotenv

from discord.ext import commands
import emoji

from bs4 import BeautifulSoup

import requests

import discord

from fake_useragent import UserAgent

import datetime
from datetime import datetime
import pandas as pd
import time
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='+')
ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
   

@bot.command(name='hello')
async def stts(ctx):
    await ctx.send(f"Namaste {ctx.author.mention}")

def get_right(team):
    flag=0
    tm1 =""
    for i in team:
        if i =='(':
            tm1+=" ->  "
            flag=1
        
        if i ==')':
            tm1+=i
            tm1+=' , '
            continue
            
        if not i.isalpha() and flag==0:
            tm1+=" -> "
            flag=1
        tm1+=i
    return tm1 

@bot.command(name='ls')
async def stts(ctx):

    y = requests.get("https://iplt20api.herokuapp.com/livescore").json()
    head = y['Headline']
    status = y['Status']
    Team1 = y['Team1']
    Team2 = y['Team2']
    flag=0
    tm1 = get_right(Team1)
    tm2 = get_right(Team2)
    embed = discord.Embed(color=0x7e76dc, title='IPL 2020 Live Score')
    desc='```arm\n'
    desc+=head+"\n"
    desc+=tm1+"\n"
    desc+=tm2+"\n"
    desc+=status+"\n"
    desc += '```'
    embed.description = desc
    await ctx.send(embed=embed)

    # await ctx.send(head + "\n" + tm1 + "\n"+tm2 + "\n" + status)    

@bot.command(name='nm')
async def stts(ctx):
    y = requests.get("https://iplt20api.herokuapp.com/nextmatch").json()
    embed = discord.Embed(color=0x7e76dc, title='IPL 2020 Next Match')
    desc='```arm\n'
    desc+= y['Team']+"\n"
    desc+=y['Date']+"\n"
    desc+=y['Time']+"\n"
    desc += '```'
    embed.description = desc
    await ctx.send(embed=embed)

Team_name=['DC', 'CSK','RCB','KKR','KXIP','RR','MI','SRH']

@bot.command(name='sc')

async def stts(ctx , cnt:int):
    
    if cnt >=18:
        return await ctx.send(f"Sorry {ctx.author.mention} I Can Only Respond Upto 17 Count  "+emoji.emojize(":pensive:"))
    url = "https://www.firstpost.com/firstcricket/cricket-schedule/series/ipl-2020.html"
    res = requests.get(url , headers=ua)
    soup = BeautifulSoup(res.content , features='lxml')
    data  =soup.findAll(class_='schedule-head')
    team_name = soup.findAll(class_='sc-match-name')
    time = soup.findAll(class_='sc-label-val')
    tm=0
    embed = discord.Embed(color=0xff0000, title='Ipl 2020 Schedule ')
    desc='```\n'
    for i in range(0 , cnt):
        if i < len(data) and i <len(team_name) and tm < len(time):
            y = data[i].get_text().strip()
            
            y = y.replace('\n' , ' ')
            y = y.replace('\t' , '')
            y = y[:6]
            p = time[tm].get_text().strip()
            p = p.replace('\n' , ' ')
            p = p.replace('\t' , '')
            r = time[tm+1].get_text().strip()
            r = r.replace('\n' , ' ')
            r = r.replace('\t' , '')
            tm=tm+2
            desc+=team_name[i].get_text().strip()+'\n'+p+"  "+r+" "+y+"\n\n"
            desc+='```'+'```'+'\n\n'


    desc += '```'
    embed.description = desc
    await ctx.send(embed=embed)

@bot.command(name="pt")

async def pointt(ctx):
    url = "https://www.espncricinfo.com/series/_/id/8048/season/2020/indian-premier-league"
    
    res = requests.get(url , headers = ua)
    soup = BeautifulSoup(res.content , features='lxml')
    points = soup.findAll(class_='pr-3')
    team = soup.findAll(class_='text-left')
    teams=[]
    for i in range(1 , 9):
        teams.append(team[i].get_text())
    match =[]
    win=[]
    loss=[]
    point=[]
    nr=[]
    flag = 0
    for i in range(5 , 45):
        y = points[i].get_text()
        # print(y , end=" ")
        if flag == 0:
            match.append(y)
            flag=1
            continue
        if flag ==1:
            win.append(y)
            flag=2
            continue
        if flag == 2:
            loss.append(y)
            flag=3
            continue
        if flag ==3:
            point.append(y)
            flag=4
            continue
        if flag == 4 :
            nr.append(y)
            flag=0

    embed = discord.Embed(color=0x7e76dc, title='IPL 2020 Point Table')
    desc='```arm\n'
    desc+='Team  Match  Win  Loss  Point   NRR\n'
    desc+='----  -----  ---  ----  -----  -----\n'
    for i in range(0, 8):
        desc += teams[i] + ' ' * (9 - len(teams[i]) - len(match[i]))
        desc += match[i] + ' ' * (6 - len(win[i]))
        desc += win[i] + ' ' * (6 - len(loss[i]))
        desc += loss[i] + ' ' * (6 - len(point[i]))
        desc += point[i] + ' ' * (9 - len(nr[i])) + nr[i] + '\n'
    desc += '```'
    embed.description = desc
    await ctx.send(embed=embed)

@bot.command(name="six")

async def stts(ctx):
    for i in range(0,11):
        await ctx.send(emoji.emojize(":six:")+emoji.emojize(":fire:") , delete_after=15)

@bot.command(name="four")

async def stts(ctx):
    for i in range(0,11):
        await ctx.send(emoji.emojize(":four:"),   delete_after=15)

@bot.command(name="out")

async def stts(ctx):
    for i in range(0,11):
        await ctx.send("Out"+" "+emoji.emojize(u'\U0001F625') ,   delete_after=15)

@bot.command(name="freehit")

async def stts(ctx):
    for i in range(0,11):
        await ctx.send("Hurray FreeHit"+emoji.emojize(u'\U0001F57A') ,   delete_after=15)

@bot.command()

async def ipl(ctx , *args):
    for i in range(0,11):
        await ctx.send('{}'.format(' '.join(args)) , delete_after=15)

@bot.command(name="comentatry")

async def stream(ctx):
    url="https://www.espncricinfo.com/series/8048/game/1216543/delhi-capitals-vs-rajasthan-royals-30th-match-indian-premier-league-2020-21"
    
    store=""
    dict1={}
    while(True):
        store=""
        res = requests.get(url , headers=ua)
        soup = BeautifulSoup(res.content , features='lxml')
        data = soup.findAll(class_='match-comment-long-text')
        ball_up = soup.findAll(class_='match-comment-short-text')
        store+=ball_up[0].get_text()+"\n"
        store+=data[0].get_text()+"\n"
        if store in dict1:
            time.sleep(10)
            continue
        dict1[store]=1
        now = datetime.now().time() # time object
        now = str(now)
        embed = discord.Embed(color=0x7e76dc, title="Time ->"+now[:5])
        desc='```arm\n'
        desc+= ball_up[0].get_text()
        desc+="\n"
        desc+=data[0].get_text()
        desc += '```'
        embed.description = desc
        print(store)
        await ctx.send(embed=embed)



bot.run(TOKEN)
