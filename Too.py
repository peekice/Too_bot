#client 850388710766936114
#token ODUwMzg4NzEwNzY2OTM2MTE0.YLpANA.26GUmkcjFHmELiEaQukrDglOQJA
#permission 2148005952
#https://discord.com/api/oauth2/authorize?client_id=850388710766936114&permissions=2148005952&scope=bot

import discord
import datetime
import random
client = discord.Client()
x= datetime.datetime.now()
long=x.year-2014
work=['คลองโอ่งอ่าง','แต่งเพลง']
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    global long,work
    if message.content in ['ผลงาน','ทำไรบ้าง']:
        await message.channel.send(str(random.choice(work)))
    elif message.content == 'กู้ทำไม':
        await message.channel.send('ใช้หนี้จำนำข้าว')
    elif message.content == 'เมื่อไรจะออก':
        await message.channel.send('ไม่ออก')
    elif message.content in ['Tony','โทนี่','ทักษิณ']:
        await message.channel.send('แน่จริงกลับมา')
    elif message.content == 'อยู่มากี่ปีแล้ว':
        await message.channel.send(str(long) + ' ปี')
    elif message.content == 'นายกที่ดีที่สุด':
        await message.channel.send('ก็ผมไงเหล่า')
  

client.run('ODUwMzg4NzEwNzY2OTM2MTE0.YLpANA.26GUmkcjFHmELiEaQukrDglOQJA')