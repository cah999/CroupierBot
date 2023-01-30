import asyncio
import os

import discord
import psycopg2
from discord.ext import commands
from gtts import gTTS


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.new_msg = False
        self.vc = None

    @staticmethod
    async def create_voice(text, lang='ru'):
        tts = gTTS(text, lang=lang)
        tts.save('voice.mp3')

    @commands.command()
    async def voice(self, ctx, *, text: str):
        global new_msg
        self.new_msg = True
        await ctx.send(embed=discord.Embed(description=f':white_check_mark: Воспроизвожу текст'))
        ch = self.client.get_guild(570546459083145216)
        voice_channel = None
        for v in ch.voice_channels:
            for member in v.members:
                if member == ctx.author:
                    voice_channel = v
                    break
        else:
            # 815911512858034226
            ch = self.client.get_guild(1044668113729355856)
            for v in ch.voice_channels:
                for member in v.members:
                    if member == ctx.author:
                        voice_channel = v
                        break
        if voice_channel:
            await self.create_voice(text)
            if not self.vc:
                self.vc = await voice_channel.connect()
            print(f'[+] Joined {voice_channel.name}')
            # vc.play(
            #     discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source='voice.mp3',
            #                            options='-loglevel panic'))
            self.vc.play(
                discord.FFmpegPCMAudio(source='voice.mp3',
                                       options='-loglevel panic'))
            print('[+] Сообщение озвучено!')
            self.new_msg = False
            while len(voice_channel.members) > 1:
                await asyncio.sleep(1)
                # if self.new_msg:
                #     return
            await self.vc.disconnect()
            self.vc = None
            print(f'[+] Leaved {voice_channel.name}')
        else:
            print('[+] Юзер не находится в каком-либо канале')


def setup(client):
    client.add_cog(Voice(client))
