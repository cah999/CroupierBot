import asyncio
import random
import datetime
import discord
from discord.ext import commands, tasks
from discord import utils
import sqlite3
import psycopg2
import os

class achive(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        self.cursor = self.conn.cursor()
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('.play'):
            self.cursor.execute("UPDATE users SET music_tracks = music_tracks + {} WHERE id = {}".format(1, message.author.id))
            self.conn.commit()
            self.cursor.execute("SELECT music_tracks FROM users WHERE id = {}".format(message.author.id))
            a = self.cursor.fetchone()[0]
            if a == 200:
                role = discord.utils.get(message.author.guild.roles, name="📀Ебан💿")
                await message.author.add_roles(role)
                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🎧Диджей🎧**", color=0x66fcff)
                embed.add_field(name="Твоя награда", value="**1000 :tickets:**\nА так же эксклюзивная роль ``📀Ебан💿``", inline=False)
                await message.author.send(embed=embed)
                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, message.author.id))   
                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, message.author.id))
                self.conn.commit()
                await message.author.send(embed=embed)
                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(message.author.id)) 
                ach = self.acursor.fetchone()[0]
                if ach == 27:
                    role = discord.utils.get(message.author.guild.roles, name="👑Склоните колено👑")
                    await message.author.add_roles(role)
                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, message.author.id))   
                    self.conn.commit()

                    await message.author.send(embed=embed)

                # РОЛЬ НУЖНА

    @commands.command(aliases = ['siwin'])
    async def __siwin(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        if member is not None:
            role = discord.utils.get(member.guild.roles, name="У меня большой мозг🤯")
            await member.add_roles(role)
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💫Мегамозг💫**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**5000 :tickets:**\nА так же эксклюзивная роль ``У меня большой мозг🤯``", inline=False)
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, member.id))
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(5000, member.id))   
            self.conn.commit()
            self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(member.id)) 
            await member.send(embed=embed)
            ach = self.cursor.fetchone()[0]
            if ach == 27:
                role = discord.utils.get(member.guild.roles, name="👑Склоните колено👑")
                await member.add_roles(role)
                embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, member.id))   
                self.conn.commit()

                await member.send(embed=embed)
        else:
            await ctx.send(embed = discord.Embed(description = 'Укажите пользователя!\n``!siwin @member``'))

def setup(client):
    client.add_cog(achive(client))