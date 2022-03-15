import asyncio
import os

import discord
import psycopg2
from discord.ext import commands

'''
Тут осталось:
Добавить реакции по ролям + проверки на баланс/ на наличие этой роли +
Нужна проверка на наличие уже этой роли +

Проработать систему с инвентарём/кейсами (poka chto beta)

Есть шанс, что тебе выпадет кейс после того, как ты ливнул из войса

Sdelat premium

XP za voice +
'''


class shop(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.message = None
        self.guild = None
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cursor = self.conn.cursor()

    #  SHOP 1
    @commands.command(aliases=['rshop1'])
    # ROLES
    async def __rshop(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="Магазин ролей", description="Нажми на реакцию, чтобы приобрести роль",
                              color=0x52bdff)
        embed.add_field(name="\u200b", value="<@&774285889286963231> \n **```50 000 билетиков 1️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285892881219604> \n **```49 000 билетиков 2️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285895566098442> \n **```48 000 билетиков 3️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285897452617750> \n **```47 000 билетиков 4️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285900258607114> \n **```46 000 билетиков 5️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285902750154772> \n **```45 000 билетиков 6️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285904649912381> \n **```44 000 билетиков 7️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285907636256778> \n **```43 000 билетиков 8️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285910128853003> \n **```42 000 билетиков 9️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285912481071124> \n **```41 000 билетиков 🔟```**", inline=True)
        message = await ctx.send(embed=embed)

        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')
        await message.add_reaction('5️⃣')
        await message.add_reaction('6️⃣')
        await message.add_reaction('7️⃣')
        await message.add_reaction('8️⃣')
        await message.add_reaction('9️⃣')
        await message.add_reaction('🔟')

    #  SHOP 2
    @commands.command(aliases=['rshop2'])
    # ROLES
    async def __rshop2(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(color=0x52bdff)
        embed.add_field(name="\u200b", value="<@&774285914654113814> \n **```40 000 билетиков 1️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285916604596245> \n **```39 000 билетиков 2️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285919074648104> \n **```38 000 билетиков 3️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285921372602388> \n **```37 000 билетиков 4️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285923369353257> \n **```36 000 билетиков 5️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285925773475912> \n **```35 000 билетиков 6️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285927933542420> \n **```34 000 билетиков 7️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285930101604352> \n **```33 000 билетиков 8️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285932111200326> \n **```32 000 билетиков 9️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285935240151050> \n **```31 000 билетиков 🔟```**", inline=True)
        message = await ctx.send(embed=embed)

        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')
        await message.add_reaction('5️⃣')
        await message.add_reaction('6️⃣')
        await message.add_reaction('7️⃣')
        await message.add_reaction('8️⃣')
        await message.add_reaction('9️⃣')
        await message.add_reaction('🔟')

    #  SHOP 3
    @commands.command(aliases=['rshop3'])
    # ROLES
    async def __rshop3(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(color=0x52bdff)
        embed.add_field(name="\u200b", value="<@&774285937303093298> \n **```30 000 билетиков 1️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285940029128765> \n **```29 000 билетиков 2️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285941975023676> \n **```28 000 билетиков 3️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285943958929408> \n **```27 000 билетиков 4️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285946463715368> \n **```26 000 билетиков 5️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285948976496671> \n **```25 000 билетиков 6️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285951433179196> \n **```23 000 билетиков 7️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774285953350369291> \n **```21 500 билетиков 8️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774293230278934568> \n **```20 000 билетиков 9️⃣```**", inline=False)
        embed.add_field(name="\u200b", value="<@&774293227997495340> \n **```20 000 билетиков 🔟```**", inline=True)
        message = await ctx.send(embed=embed)

        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')
        await message.add_reaction('5️⃣')
        await message.add_reaction('6️⃣')
        await message.add_reaction('7️⃣')
        await message.add_reaction('8️⃣')
        await message.add_reaction('9️⃣')
        await message.add_reaction('🔟')

    # # SHOP ITEMS
    # @commands.command(aliases = ['ishop'])
    # # ITEMS
    # async def __ishop(self, ctx):
    #     await ctx.channel.purge (limit = 1)
    #     embed=discord.Embed(title="Магазин предметов", description="Нажми на реакцию, чтобы приобрести предмет", color=0x5cff61)
    #     embed.add_field(name="\u200b", value="PREMIUM-статус (3 месяца) \n **```100 000 билетиков 1️⃣```**", inline=False)
    #     embed.add_field(name="\u200b", value="Lite PREMIUM-статус (3 месяца) \n **```65 000 билетиков 2️⃣```**", inline=False)
    #     embed.add_field(name="\u200b", value="Clan Leader \n **```50 000 билетиков 3️⃣```**", inline=False) pod voprosom
    #     embed.add_field(name="\u200b", value="Midas \n **```40 000 билетиков 4️⃣```**", inline=False) #Za dengi / Pereskazat` istoriy pro Midasa moderatory / k 8 minute midas (ne turbo)
    #     embed.add_field(name="\u200b", value="VIP-статус \n **```35 000 билетиков 5️⃣```**", inline=False) 
    #     embed.add_field(name="\u200b", value="Кейс ролей #1 \n **```35 000 билетиков 6️⃣```**", inline=False)
    #     embed.add_field(name="\u200b", value="Кейс ролей #2 \n **```35 000 билетиков 7️⃣```**", inline=False)
    #     embed.add_field(name="\u200b", value="Кейс ролей #3 \n **```35 000 билетиков 8️⃣```**", inline=False)
    #     embed.add_field(name="\u200b", value="Lite VIP-статус \n **```10 000 билетиков 9️⃣```**", inline=True)
    #     message = await ctx.send(embed=embed)

    #     await message.add_reaction('1️⃣')
    #     await message.add_reaction('2️⃣')
    #     await message.add_reaction('3️⃣')
    #     await message.add_reaction('4️⃣')
    #     await message.add_reaction('5️⃣')
    #     await message.add_reaction('6️⃣')
    #     await message.add_reaction('7️⃣')
    #     await message.add_reaction('8️⃣')
    #     await message.add_reaction('9️⃣')

    # self.cursor.execute("UPDATE users SET balance = balance  {} WHERE id = {}".format(cost, member))

    # self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
    #     ============================

    # КУПИТЬ РОЛЬ
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 782192944487989269:  # Айди сообщения
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            if payload.emoji.name == '1️⃣':
                role1 = discord.utils.get(guild.roles, name="ЁБАНЫЙ РОТ ЭТОГО КАЗИНО🎰")
                cost = 50000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '1️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '2️⃣':
                role1 = discord.utils.get(guild.roles, name="shit, i got cyber bullied🌌")
                cost = 49000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '2️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '3️⃣':
                role1 = discord.utils.get(guild.roles, name="БДСМ🧸")
                cost = 48000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '3️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '4️⃣':
                role1 = discord.utils.get(guild.roles, name="Chlenix🔋")
                cost = 47000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '4️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '5️⃣':
                role1 = discord.utils.get(guild.roles, name="somebody once told me...🧻")
                cost = 46000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '5️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '6️⃣':
                role1 = discord.utils.get(guild.roles, name="Инопришеленец👽")
                cost = 45000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '6️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '7️⃣':
                role1 = discord.utils.get(guild.roles, name="Ты как из дурки вылез?💉")
                cost = 44000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '7️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '8️⃣':
                role1 = discord.utils.get(guild.roles, name="Как я вылез, говоришь?🩸")
                cost = 43000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '8️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '9️⃣':
                role1 = discord.utils.get(guild.roles, name="Хто я?🌚")
                cost = 42000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '9️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '🔟':
                role1 = discord.utils.get(guild.roles, name="А чо всмысле? 🤷🏽")
                cost = 41000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '🔟',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass


        elif message_id == 782192954651312158:  # Айди сообщения
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            if payload.emoji.name == '1️⃣':
                role1 = discord.utils.get(guild.roles, name="Лунная призма дай мне сил🌠")
                cost = 40000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '1️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '2️⃣':
                role1 = discord.utils.get(guild.roles, name="password: Oral_Cumshot03🏳️‍🌈")
                cost = 39000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '2️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '3️⃣':
                role1 = discord.utils.get(guild.roles, name="Mr. Semen`s🐓")
                cost = 38000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '3️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '4️⃣':
                role1 = discord.utils.get(guild.roles, name="Дядя Богдан👨🏼‍🌾")
                cost = 37000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '4️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '5️⃣':
                role1 = discord.utils.get(guild.roles, name="Final brain cell🦠")
                cost = 36000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '5️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '6️⃣':
                role1 = discord.utils.get(guild.roles, name="Ценю мать🧡")
                cost = 35000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '6️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '7️⃣':
                role1 = discord.utils.get(guild.roles, name="АУЕбалбес🚬")
                cost = 34000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\nНажми на **галочку**, чтобы '
                                    f'**подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '7️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '8️⃣':
                role1 = discord.utils.get(guild.roles, name="Я их БЛЯТЬ ненавижу, Дио!🤬")
                cost = 33000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\nНажми на **галочку**, чтобы '
                                    f'**подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '8️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '9️⃣':
                role1 = discord.utils.get(guild.roles, name="Джотаро, ты любишь кабачки?🍆")
                cost = 32000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '9️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '🔟':
                role1 = discord.utils.get(guild.roles, name="Уебан 1000-ого ранга🏆")
                cost = 31000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '🔟',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass


        elif message_id == 782192962742255637:  # Айди сообщения
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            if payload.emoji.name == '1️⃣':
                role1 = discord.utils.get(guild.roles, name="Ластхит по перхоти 🧊")
                cost = 30000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '1️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '2️⃣':
                role1 = discord.utils.get(guild.roles, name="Крип крипочек💫")
                cost = 29000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '2️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '3️⃣':
                role1 = discord.utils.get(guild.roles, name="Gachi Player🌈")
                cost = 28000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '3️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '4️⃣':
                role1 = discord.utils.get(guild.roles, name="Отсосу за колбасу🌭")
                cost = 27000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '4️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '5️⃣':
                role1 = discord.utils.get(guild.roles, name="Clown🤡")
                cost = 26000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '5️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '6️⃣':
                role1 = discord.utils.get(guild.roles, name="༼ つ ◕_◕ ༽つ=ε/̵͇̿/’̿’̿ ̿ ̿̿")
                cost = 25000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '6️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '7️⃣':
                role1 = discord.utils.get(guild.roles, name="༼ つ ◕_◕ ༽つ")
                cost = 23000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '7️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '8️⃣':
                role1 = discord.utils.get(guild.roles, name="Raccoon🦝")
                cost = 21500
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '8️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '9️⃣':
                role1 = discord.utils.get(guild.roles, name="BadBoy👦")
                cost = 20000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '9️⃣',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass
            elif payload.emoji.name == '🔟':
                role1 = discord.utils.get(guild.roles, name="SexyGirl👧")
                cost = 20000
                if role1 is not None:
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        bal = self.cursor.fetchone()[0]
                        if bal >= cost:
                            if role1 in payload.member.roles:
                                await member.send('Вы уже имеете эту роль!', delete_after=60)

                            if role1 in payload.member.roles:
                                await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '🔟',
                                                                       payload.user_id)
                                await member.send('Вы уже имеете эту роль!', delete_after=60)
                            else:
                                msg = await member.send(
                                    f'Вы уверены что хотите приобрести ``{role1}``?\n'
                                    f'Нажми на **галочку**, чтобы **подтверидть** действие.',
                                    delete_after=31)
                                await msg.add_reaction('✅')

                                def check(reaction, user):
                                    return user == member and str(reaction.emoji) == '✅'

                                try:
                                    await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                                except asyncio.TimeoutError:
                                    emb = discord.Embed(colour=discord.Color.green())
                                    emb.add_field(name=':x: Покупка роли:', value='Действие отменнено!')
                                    await member.send(embed=emb, delete_after=30)
                                else:
                                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                                    bal = self.cursor.fetchone()[0]
                                    if bal >= cost:
                                        self.cursor.execute(
                                            "UPDATE users SET balance = balance - {} WHERE id = {}".format(cost,
                                                                                                           member.id))
                                        self.conn.commit()
                                        await member.add_roles(role1)
                                        await member.send('Вы успешно приобрели роль!', delete_after=60)
                                    else:
                                        await member.send('Не надо меня обманывать, бро', delete_after=60)
                        else:
                            await self.client.http.remove_reaction(payload.channel_id, payload.message_id, '🔟',
                                                                   payload.user_id)
                            await member.send('У вас недостаточно средств для покупки данной роли!', delete_after=30)
                    else:
                        pass


def setup(client):
    client.add_cog(shop(client))
