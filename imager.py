# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import math
import os
from PIL import Image, ImageDraw, ImageFilter
from PIL import ImageFont
from time import time
import urllib.request
import json
import base64
import discord

status = {}

def kisekae_k(mcid,number):
    try:
        with urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/"+mcid) as res:
            html = res.read().decode("utf-8")
    except:
        return "Error"
    try:
        json3 = json.loads(html)
    except:
        return "Error"

    if(html==""):
        return "Error"

    uuid = json3["id"]
    with urllib.request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/"+uuid) as res:
        html2 = res.read().decode("utf-8")


    json2 = json.loads(html2)

    value = json2["properties"][0]["value"]

    json4 = base64.b64decode(value).decode()

    json5 = json.loads(json4)

    url = json5["textures"]["SKIN"]["url"]


    urllib.request.urlretrieve(url,"./images/"+str(mcid)+".png")

    im = Image.open("images/"+str(mcid)+".png")

    im_crop = im.crop((0, 0, 32, 16))
    im_crop.save("images/head_"+str(mcid)+".png", quality=95)
    
    
    
    if(number=="1"):
        img = Image.open("kakkoii1.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((40, 48, 41, 50))
        img.paste(im9, (21, 18),im9)
        img.paste(im9, (22, 18),im9)
        img.paste(im9, (23, 18),im9)
        img.paste(im9, (24, 18),im9)
        img.paste(im9, (25, 18),im9)
        img.paste(im9, (26, 18),im9)
        img.paste(im9, (23, 20),im9)
        img.paste(im9, (24, 20),im9)
    if(number=="2"):
        img = Image.open("kakkoii2.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((40, 48, 41, 50))
        img.paste(im9, (21, 18),im9)
        img.paste(im9, (22, 18),im9)
        img.paste(im9, (23, 18),im9)
        img.paste(im9, (24, 18),im9)
        img.paste(im9, (25, 18),im9)
        img.paste(im9, (26, 18),im9)
        img.paste(im9, (23, 20),im9)
        img.paste(im9, (24, 20),im9)
    if(number=="3"):
        img = Image.open("kakkoii3.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((40, 48, 41, 50))
        img.paste(im9, (21, 18),im9)
        img.paste(im9, (22, 18),im9)
        img.paste(im9, (23, 18),im9)
        img.paste(im9, (24, 18),im9)
        img.paste(im9, (25, 18),im9)
        img.paste(im9, (26, 18),im9)
        img.paste(im9, (23, 20),im9)
        img.paste(im9, (24, 20),im9)
    if(number=="4"):
        img = Image.open("kakkoii4.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((40, 48, 41, 50))
        img.paste(im9, (21, 18),im9)
        img.paste(im9, (22, 18),im9)
        img.paste(im9, (23, 18),im9)
        img.paste(im9, (24, 18),im9)
        img.paste(im9, (25, 18),im9)
        img.paste(im9, (26, 18),im9)
        img.paste(im9, (23, 20),im9)
        img.paste(im9, (24, 20),im9)

    img.save('outputs/'+str(mcid)+".png")
    return './outputs/'+str(mcid)+".png"


def kisekae(mcid,number):
    try:
        with urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/"+mcid) as res:
            html = res.read().decode("utf-8")
    except:
        return "Error"
    try:
        json3 = json.loads(html)
    except:
        return "Error"

    if(html==""):
        return "Error"

    uuid = json3["id"]
    with urllib.request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/"+uuid) as res:
        html2 = res.read().decode("utf-8")


    json2 = json.loads(html2)

    value = json2["properties"][0]["value"]

    json4 = base64.b64decode(value).decode()

    json5 = json.loads(json4)

    url = json5["textures"]["SKIN"]["url"]


    urllib.request.urlretrieve(url,"./images/"+str(mcid)+".png")

    im = Image.open("images/"+str(mcid)+".png")

    im_crop = im.crop((0, 0, 32, 16))
    im_crop.save("images/head_"+str(mcid)+".png", quality=95)
    
    
    
    if(number=="1"):
        img = Image.open("kawaii1.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((48, 16, 50, 19))
        img.paste(im9, (23, 19),im9)
        im10 = im.crop((48, 16, 49, 19))
        img.paste(im10, (23, 18),im10)

        im11 = im.crop((48, 16, 50, 17))
        img.paste(im11, (35, 20),im11)
    if(number=="2"):
        img = Image.open("kawaii2.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
    if(number=="3"):
        img = Image.open("kawaii3.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((48, 16, 50, 19))
        img.paste(im9, (23, 19),im9)
        im10 = im.crop((48, 16, 49, 19))
        img.paste(im10, (23, 18),im10)

        im11 = im.crop((48, 16, 50, 17))
        img.paste(im11, (35, 20),im11)
    if(number=="4"):
        img = Image.open("kawaii4.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((48, 16, 50, 19))
        img.paste(im9, (23, 19),im9)

    img.save('outputs/'+str(mcid)+".png")
    return './outputs/'+str(mcid)+".png"

def kisekae_n(mcid,number):
    try:
        with urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/"+mcid) as res:
            html = res.read().decode("utf-8")
    except:
        return "Error"
    try:
        json3 = json.loads(html)
    except:
        return "Error"

    if(html==""):
        return "Error"

    uuid = json3["id"]
    with urllib.request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/"+uuid) as res:
        html2 = res.read().decode("utf-8")


    json2 = json.loads(html2)

    value = json2["properties"][0]["value"]

    json4 = base64.b64decode(value).decode()

    json5 = json.loads(json4)

    url = json5["textures"]["SKIN"]["url"]


    urllib.request.urlretrieve(url,"./images/"+str(mcid)+".png")

    im = Image.open("images/"+str(mcid)+".png")

    im_crop = im.crop((0, 0, 64, 16))
    im_crop.save("images/head_"+str(mcid)+".png", quality=95)
    
    
    
    if(number=="1"):
        img = Image.open("kawaii1_n.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((48, 16, 50, 19))
        img.paste(im9, (23, 19),im9)
        im10 = im.crop((48, 16, 49, 19))
        img.paste(im10, (23, 18),im10)

        im11 = im.crop((48, 16, 50, 17))
        img.paste(im11, (35, 20),im11)
    if(number=="2"):
        img = Image.open("kawaii2_n.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 30, 56, 32))
        im6 = im.crop((32, 62, 48, 64))
        img.paste(im5, (40, 30),im5)
        img.paste(im6, (32, 62),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
    if(number=="3"):
        img = Image.open("kawaii3_n.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((48, 16, 50, 19))
        img.paste(im9, (23, 19),im9)
        im10 = im.crop((48, 16, 49, 19))
        img.paste(im10, (23, 18),im10)

        im11 = im.crop((48, 16, 50, 17))
        img.paste(im11, (35, 20),im11)
    if(number=="4"):
        img = Image.open("kawaii4_n.png")
        im4 = Image.open("images/head_"+str(mcid)+".png")
        img.paste(im4, (0, 0),im4)
        im5 = im.crop((40, 31, 56, 32))
        im6 = im.crop((32, 63, 48, 64))
        img.paste(im5, (40, 31),im5)
        img.paste(im6, (32, 63),im6)
        im7 = im.crop((40, 48, 44, 52))
        im8 = im.crop((48, 16, 52, 20))
        img.paste(im7, (40, 48),im7)
        img.paste(im8, (48, 16),im8)
        im9 = im.crop((48, 16, 50, 19))
        img.paste(im9, (23, 19),im9)

    img.save('outputs/'+str(mcid)+".png")
    return './outputs/'+str(mcid)+".png"

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(activity=discord.Game("DMに[着付けスタート]と送信!"))

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if isinstance(message.channel, discord.channel.DMChannel):
        myid = message.author.id
        if message.content == 'キャンセル':
            embed = discord.Embed(title="着付ちゃん",description="キャンセルしました!\nもう一度始めるには[着付けスタート]とチャットしてください",color=0xEF71C7)
            status[myid] = "ready"
            await message.channel.send(embed=embed)
            return
        if myid in status:
            print(status[myid]+"__1")
            if status[myid] == "kakkoii_1":
                get = kisekae_k(message.content,"1")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "kakkoii_2":
                get = kisekae_k(message.content,"2")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "kakkoii_3":
                get = kisekae_k(message.content,"3")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "kakkoii_4":
                get = kisekae_k(message.content,"4")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return


                
        if myid in status:
            print(status[myid]+"__1")
            if status[myid] == "yukata_1_y":
                get = kisekae(message.content,"1")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "yukata_2_y":
                get = kisekae(message.content,"2")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "yukata_3_y":
                get = kisekae(message.content,"3")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "yukata_4_y":
                get = kisekae(message.content,"4")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return

        if myid in status:
            print(status[myid]+"__1")
            if status[myid] == "yukata_1_n":
                get = kisekae_n(message.content,"1")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "yukata_2_n":
                get = kisekae_n(message.content,"2")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "yukata_3_n":
                get = kisekae_n(message.content,"3")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
            elif status[myid] == "yukata_4_n":
                get = kisekae_n(message.content,"4")
                if get == "Error":
                    embed = discord.Embed(title="着付ちゃん",description="エラーが発生しました\nMCIDにお間違えはありませんか? もう一度MCIDを入力し直してみてください\n[キャンセル]でキャンセルできます",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="できました! ご利用頂きありがとうございました!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    abc = discord.File(get)
                    await message.channel.send(file=abc)
                    status[myid] = "ready"
                    return
                
        if myid in status:
            if status[myid] == "mcid_1":
                if message.content == "はい":
                    status[myid] = "yukata_1_y"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                elif message.content == "いいえ":
                    status[myid] = "yukata_1_n"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="[はい] または [いいえ] でお答えください",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
            elif status[myid] == "mcid_2":
                if message.content == "はい":
                    status[myid] = "yukata_2_y"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                elif message.content == "いいえ":
                    status[myid] = "yukata_2_n"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="[はい] または [いいえ] でお答えください",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
            elif status[myid] == "mcid_3":
                if message.content == "はい":
                    status[myid] = "yukata_3_y"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                elif message.content == "いいえ":
                    status[myid] = "yukata_3_n"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="[はい] または [いいえ] でお答えください",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
            elif status[myid] == "mcid_4":
                if message.content == "はい":
                    status[myid] = "yukata_4_y"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                elif message.content == "いいえ":
                    status[myid] = "yukata_4_n"
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    print(status[myid])
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="[はい] または [いいえ] でお答えください",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    return
        if myid in status:
            print(status[myid]+"__2")
            if status[myid] == "yukata":
                if message.content == "1":
                    embed = discord.Embed(title="着付ちゃん",description="髪飾りをつけますか?\n\n頭の3Dレイヤーが上書きされてしまうため、髪型などがおかしくなってしまう場合がございます。\nその場合は髪飾り無しをお選びください。",color=0xEF71C7)
                    embed.add_field(name="髪飾りを付ける",value="[はい]とチャットしてください",inline=False)
                    embed.add_field(name="髪飾りを付けない",value="[いいえ]とチャットしてください",inline=False)
                    await message.channel.send(embed=embed)
                    status[myid] = "mcid_1"
                    return
                elif message.content == "2":
                    embed = discord.Embed(title="着付ちゃん",description="髪飾りをつけますか?\n\n頭の3Dレイヤーが上書きされてしまうため、髪型などがおかしくなってしまう場合がございます。\nその場合は髪飾り無しをお選びください。",color=0xEF71C7)
                    embed.add_field(name="髪飾りを付ける",value="[はい]とチャットしてください",inline=False)
                    embed.add_field(name="髪飾りを付けない",value="[いいえ]とチャットしてください",inline=False)
                    await message.channel.send(embed=embed)
                    status[myid] = "mcid_2"
                    return
                elif message.content == "3":
                    embed = discord.Embed(title="着付ちゃん",description="髪飾りをつけますか?\n\n頭の3Dレイヤーが上書きされてしまうため、髪型などがおかしくなってしまう場合がございます。\nその場合は髪飾り無しをお選びください。",color=0xEF71C7)
                    embed.add_field(name="髪飾りを付ける",value="[はい]とチャットしてください",inline=False)
                    embed.add_field(name="髪飾りを付けない",value="[いいえ]とチャットしてください",inline=False)
                    await message.channel.send(embed=embed)
                    status[myid] = "mcid_3"
                    return
                elif message.content == "4":
                    embed = discord.Embed(title="着付ちゃん",description="髪飾りをつけますか?\n\n頭の3Dレイヤーが上書きされてしまうため、髪型などがおかしくなってしまう場合がございます。\nその場合は髪飾り無しをお選びください。",color=0xEF71C7)
                    embed.add_field(name="髪飾りを付ける",value="[はい]とチャットしてください",inline=False)
                    embed.add_field(name="髪飾りを付けない",value="[いいえ]とチャットしてください",inline=False)
                    await message.channel.send(embed=embed)
                    status[myid] = "mcid_4"
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="1-4の中で選んでください",color=0xEF71C7)
                    embed.add_field(name="1番目がいい!!",value="[1]とチャットしてください",inline=False)
                    embed.add_field(name="2番目がいい!!",value="[2]とチャットしてください",inline=False)
                    embed.add_field(name="3番目がいい!!",value="[3]とチャットしてください",inline=False)
                    embed.add_field(name="4番目がいい!!",value="[4]とチャットしてください",inline=False)
                    embed.set_image(url="http://cdn.mckarbon.com/images/list_kawaii.png")
                    await message.channel.send(embed=embed)
                    return
        if myid in status:
            print(status[myid]+"__2")
            if status[myid] == "kakkoii":
                if message.content == "1":
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    status[myid] = "kakkoii_1"
                    print(status[myid])
                    return
                elif message.content == "2":
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    status[myid] = "kakkoii_2"
                    print(status[myid])
                    return
                elif message.content == "3":
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    status[myid] = "kakkoii_3"
                    print(status[myid])
                    return
                elif message.content == "4":
                    embed = discord.Embed(title="着付ちゃん",description="MCIDを入力してください!!",color=0xEF71C7)
                    await message.channel.send(embed=embed)
                    status[myid] = "kakkoii_4"
                    print(status[myid])
                    return
                else:
                    embed = discord.Embed(title="着付ちゃん",description="1-4の中で選んでください",color=0xEF71C7)
                    embed.add_field(name="1番目がいい!!",value="[1]とチャットしてください",inline=False)
                    embed.add_field(name="2番目がいい!!",value="[2]とチャットしてください",inline=False)
                    embed.add_field(name="3番目がいい!!",value="[3]とチャットしてください",inline=False)
                    embed.add_field(name="4番目がいい!!",value="[4]とチャットしてください",inline=False)
                    embed.set_image(url="http://cdn.mckarbon.com/images/list_kakkoii.png")
                    await message.channel.send(embed=embed)
                    return


        if message.content == '着付けスタート':
            embed = discord.Embed(title="着付ちゃん",description="着付ちゃんをご利用頂きありがとうございます!\nまずは かわいい浴衣 か かっこいい浴衣 かを選んでください!\n途中でやめる場合は[キャンセル]とチャットしてください\n\nまたこのサービスはMinecraft Java Editionをお持ちの方のみがご利用になれます。",color=0xEF71C7)
            embed.add_field(name="かわいい浴衣を着たい!!",value="[かわいい]とチャットしてください",inline=False)
            embed.add_field(name="かっこいい浴衣を着たい!!",value="[かっこいい]とチャットしてください",inline=False)
            await message.channel.send(embed=embed)
            status[myid] = "started"
        elif message.content == "かっこいい":
            if myid in status:
                if status[myid] == "started":
                    embed = discord.Embed(title="着付ちゃん",description="お好きな浴衣の種類を選んでください!!",color=0xEF71C7)
                    embed.add_field(name="1番目がいい!!",value="[1]とチャットしてください",inline=False)
                    embed.add_field(name="2番目がいい!!",value="[2]とチャットしてください",inline=False)
                    embed.add_field(name="3番目がいい!!",value="[3]とチャットしてください",inline=False)
                    embed.add_field(name="4番目がいい!!",value="[4]とチャットしてください",inline=False)
                    embed.set_image(url="http://cdn.mckarbon.com/images/list_kakkoii.png")
                    status[myid] = "kakkoii"
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("まずは [着付けスタート] とチャットしてください")
            else:
                await message.channel.send("まずは [着付けスタート] とチャットしてください")
        elif message.content == "かわいい":
            if myid in status:
                if status[myid] == "started":
                    embed = discord.Embed(title="着付ちゃん",description="お好きな浴衣の種類を選んでください!!",color=0xEF71C7)
                    embed.add_field(name="1番目がいい!!",value="[1]とチャットしてください",inline=False)
                    embed.add_field(name="2番目がいい!!",value="[2]とチャットしてください",inline=False)
                    embed.add_field(name="3番目がいい!!",value="[3]とチャットしてください",inline=False)
                    embed.add_field(name="4番目がいい!!",value="[4]とチャットしてください",inline=False)
                    embed.set_image(url="http://cdn.mckarbon.com/images/list_kawaii.png")
                    status[myid] = "yukata"
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("まずは [着付けスタート] とチャットしてください")
            else:
                await message.channel.send("まずは [着付けスタート] とチャットしてください")
        else:
            if myid in status:
                if status[myid] == "started":
                    embed = discord.Embed(title="着付ちゃん",description="着付ちゃんをご利用頂きありがとうございます!\nまずは かわいい浴衣 か かっこいい浴衣 かを選んでください!\n途中でやめる場合は[キャンセル]とチャットしてください\n\nまたこのサービスはMinecraft Java Editionをお持ちの方のみがご利用になれます。",color=0xEF71C7)
                    embed.add_field(name="かわいい浴衣を着たい!!",value="[かわいい]とチャットしてください",inline=False)
                    embed.add_field(name="かっこいい浴衣を着たい!!",value="[かっこいい]とチャットしてください",inline=False)
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("まずは [着付けスタート] とチャットしてください")
            else:
                await message.channel.send("まずは [着付けスタート] とチャットしてください")


client.run("TOKEN HERE")



