import discord
from discord.ext import commands
from collections import defaultdict
from datetime import datetime
import sqlite3
import psycopg2
import os
class InviteTracker(commands.Cog, name='Invites'):
    def __init__(self, client):
        self.client = client
        self.cached_invites = defaultdict(lambda: defaultdict(int))
        client.loop.create_task(self.get_guild_invites())
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        self.cursor = self.conn.cursor()

    async def get_guild_invites(self):
        await self.client.wait_until_ready()
        for guild in self.client.guilds:
            if not guild.me.guild_permissions.manage_guild:
                continue
            try:
                invites = await guild.invites()
            except discord.HTTPException:
                continue
            if not invites:
                continue
            self.cached_invites[guild.id] = defaultdict(int, {invite.code: invite.uses for invite in invites})


    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        self.cached_invites[invite.guild.id][invite.code]
        # defaultdict handles everything

    @commands.Cog.listener()
    async def on_invite_delete(self, invite: discord.Invite):
        del self.cached_invites[invite.guild.id][invite.code]
        if not self.cached_invites[invite.guild.id]:
            del self.cached_invites[invite.guild.id]

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        invite_channel = self.client.get_channel(764722943296667649)
        if not member.guild.me.guild_permissions.manage_guild or member.guild.id not in self.cached_invites:
            return

        invites = await member.guild.invites()
        inviter = None
        for invite in invites:
            # if invite.uses > self.cached_invites[member.guild.id][invite.code]:
            inviter = invite.inviter
            self.cached_invites[member.guild.id][invite.code] = invite.uses
        if inviter is None:
            e = discord.Embed(description = 'К нам присоединился новый участник! ',
                              color=discord.Colour.dark_purple(),
                              timestamp=datetime.utcnow())
            e.set_author(icon_url=member.avatar_url, name=member)
            await invite_channel.send(embed=e)
            return 
        self.cursor.execute("UPDATE users SET invites = invites + {} WHERE id = {}".format(1, inviter.id))
        self.conn.commit()
        self.cursor.execute("SELECT invites FROM users WHERE id = {}".format(inviter.id))
        a = self.cursor.fetchone()[0]
        if a == 10:
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🎆Общительный🎆**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**2000 :tickets:**", inline=False)
            embed.set_footer(text="Следующее достижение: 25 друзей")
            await inviter.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(2000, inviter.id))
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, inviter.id))
            self.conn.commit()

        elif a == 25:
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🎇Душа компании🎇**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**4000 :tickets:**", inline=False)
            embed.set_footer(text="Следующее достижение: 50 друзей")
            await inviter.send(embed=embed)        
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(4000, inviter.id))   
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, inviter.id))
            self.conn.commit()

        elif a == 50:
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**Альфач😎**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**7500 :tickets:**", inline=False)
            await inviter.send(embed=embed)            
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(7500, inviter.id))
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, inviter.id))
            self.conn.commit()
            self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(inviter.id))
            b = self.cursor.fetchone()[0]
            if b == 27:
                role = discord.utils.get(inviter.guild.roles, name="👑Склоните колено👑")
                await inviter.add_roles(role)
                embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, inviter.id))   
                self.conn.commit()

                await inviter.send(embed=embed)
        if invite_channel is not None:
            e = discord.Embed(title='К нам присоединился новый участник! ',
                              color=discord.Colour.dark_purple(),
                              timestamp=datetime.utcnow())
            e.set_author(icon_url=member.avatar_url, name=member)
            

            e.add_field(name='Приласил:', value=f'{inviter.mention} (Количество приглашений: {a})')
            await invite_channel.send(embed=e)

    def prettify_invites(self):
        """Converts our nested defaultdicts to dicts for print"""
        return {k: dict(v) if isinstance(v, defaultdict) else v for (k, v) in self.cached_invites.items()}


def setup(client):
    client.add_cog(InviteTracker(client))