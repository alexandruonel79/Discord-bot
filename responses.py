import random
import youtube_dl
import os
import asyncio
import time
import discord
import weather
import chatBot

voice_client_global = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}
talkToBotGlobal={}
talkToBotGlobal[0]=0

async def handle_response(message) -> str:
    text_message = message.content.lower()

    if talkToBotGlobal[0]==0:
        if text_message == 'hello':
            return 'Hey there!'

        if text_message == 'roll':
            return str(random.randint(1, 6))

        if text_message == '!help':
            return "`This is a help message that you can modify.`"
    
        if text_message.startswith("?play"):
            try:
                voice_client = await message.author.voice.channel.connect()
                voice_client_global[0]=voice_client
            except:
                print("error")

            try:
                url = message.content.split()[1]

                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

                song = data['url']
                player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

                voice_client_global[0].play(player)

            except Exception as err:
                print(err)


        if text_message.startswith("?pause"):
            try:
                voice_client_global[0].pause()
            except Exception as err:
                print(err)

        # This resumes the current song playing if it's been paused
        if text_message.startswith("?resume"):
            try:
                voice_client_global[0].resume()
            except Exception as err:
                print(err)

        # This stops the current playing song
        if text_message.startswith("?stop"):
            try:
                voice_client_global[0].stop()
                await voice_client_global[0].disconnect()
            except Exception as err:
                print(err)
    
        if text_message.startswith("vreme"):
            oras=text_message.split(" ")[1]
            return weather.getWeather(oras)

        if text_message=="chatbot":
            talkToBotGlobal[0]=1

        if text_message == "[]": # Checks if there is an attachment on the message
            return
        else: # If there is it gets the filename from message.attachments
            imageName = str("input") + '.jpg'
            await message.attachments[0].save(imageName)
            return "Imagine salvata!"
    else:
        if text_message=="quit":
            talkToBotGlobal[0]=0
        else:
            return chatBot.generateAnswer(text_message)