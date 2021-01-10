import asyncio
import random
import datetime
import discord
from discord.ext import commands, tasks
from discord import utils
import sqlite3
import psycopg2
import os

class lb(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        self.cursor = self.conn.cursor()


    #TOP tickets
    @commands.command(aliases = ['moneytop'])
    async def __moneytop(self,ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = '👨🏻‍🏭 Топ 10 богатых сучек 👩🏻‍🔧', color = 0x32aafd)
        counter = 0
        self.cursor.execute("SELECT name, balance FROM users ORDER BY balance DESC LIMIT 10")
        users = self.cursor.fetchall()
        print(users)
        for row in users:
            counter += 1
            if counter == 1:
                embed.add_field(
                    name = f'# {counter} | {row[0]} ← Rich Bitch 😎',
                    value = f'Баланс: **{row[1]}** :tickets:',
                    inline = False
                )
            else:
                embed.add_field(
                    name = f'# {counter} | {row[0]}',
                    value = f'Баланс: **{row[1]}** :tickets:',
                    inline = False
                )
        await ctx.send(embed = embed, delete_after = 60)

    # TOP LVL
    @commands.command(aliases = ['lvltop'])
    async def __lvltop(self,ctx):        
        await ctx.message.delete()
        embed = discord.Embed(title = '🤴 Топ влиятельных сучек 👸', color = 0x32aafd)
        counter = 0

        self.cursor.execute("SELECT name, lvl FROM users ORDER BY lvl DESC, xp DESC LIMIT 10")
        users = self.cursor.fetchall()
        for row in users:
            counter += 1
            if counter == 1:
                embed.add_field(
                    name = f'# {counter} | {row[0]} ← Big Boss🐓',
                    value = f'Уровень: **{row[1]}** ✨',
                    inline = False
                )
            else:
                embed.add_field(
                    name = f'# {counter} | {row[0]}',
                    value = f'Уровень: **{row[1]}** ✨',
                    inline = False
                )
        await ctx.send(embed = embed, delete_after = 60)

    # TOP voice
    @commands.command(aliases = ['voicetop'])
    async def __voicetop(self,ctx):        
        await ctx.message.delete()
        embed = discord.Embed(title = '👩‍🎤 Топ общительных сучек 👨‍🎤', color = 0x32aafd)
        counter = 0
        self.cursor.execute("SELECT name, voice_minutes FROM users ORDER BY voice_minutes DESC")
        users = self.cursor.fetchall()
        print(users)
        for row in users:
            print(row)
            counter += 1
            if counter == 1:
                embed.add_field(
                    name = f'# {counter} | {row[0]} ← Душа компаний 👨‍🚀',
                    value = f'Часы: **{row[1]//60}** 🎙',
                    inline = False
                )
            else:
                print(row)
                embed.add_field(
                    name = f'# {counter} | {row[0]}',
                    value = f'Часы: **{row[1]//60}** 🎙',
                    inline = False
                )
        await ctx.send(embed = embed, delete_after = 60)


    @commands.command(aliases = ['rank'])
    async def __rank(self, ctx):
        guild_id = 315748640968933376
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        await ctx.message.delete()
        self.cursor.execute(f"SELECT name FROM users WHERE id = {ctx.author.id}")
        user = self.cursor.fetchone()[0]
        self.cursor.execute(f"SELECT xp FROM users WHERE id = {ctx.author.id}")
        xp = self.cursor.fetchone()[0]
        self.cursor.execute(f"SELECT lvl FROM users WHERE id = {ctx.author.id}")
        lvl = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT name, lvl FROM users ORDER BY lvl DESC, xp DESC")
        rankings = self.cursor.fetchall()
        rank = 0
        for x in rankings:
            rank += 1
            if x[0] == user:
                break
        self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id))
        all = 500 + 100*self.cursor.fetchone()[0]
        boxes = int((xp*20)/all)
        embed = discord.Embed(title = f"Ранк {ctx.author.name}")
        embed.add_field(name = "Уровень", value = f'**{lvl}**', inline = True)
        embed.add_field(name = "XP", value = f'**{xp}/{all}**', inline = True)
        embed.add_field(name = "Ранк", value = f'**{rank}/{ctx.guild.member_count+guild.member_count}**', inline = True)
        embed.add_field(name = "Прогресс", value = boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline = False)
        embed.set_thumbnail(url = ctx.author.avatar_url)
        await ctx.channel.send(embed = embed, delete_after = 60)


def setup(client):
    client.add_cog(lb(client))