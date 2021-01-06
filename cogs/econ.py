import discord
from discord.ext import commands
import sqlite3
import random
import asyncio
from datetime import datetime
import datetime
import threading
import os
import psycopg2
"""            
Переделать крайм  ✔
Если получится соединить с бункером
Или просто добавить генератор в дс
А ещё голосование кста
Обнуление ✔
Сделать систему монет по войс чату ✔
Статистика сообщений ✔
Добавить магазин ✔
Ачивки
Добавить перевод ✔
Пофиксить баги
help // Сделать отдельно в канале команды бота
АВТО РОЛЬ!!! ✔
МУТ X
ВАРН ✔

ОЧИЩАТЬ  ЧАТ В ГАМБЛИНГЕ ОТ ЛИШНИХ СООБЩЕНИЙ
МОД 
ШОП
СООБЩЕНИЕ ПОСЛЕ КИКА или БАНА В ЛС
КНПОКУ ДЛЯ ОТВЕТА

ГИВЫ ✔
АНТИ СПАМ X
Jackpot
3 кнопки побега в ограблении
Описание для ачивок
Ref system
Сборы в fun py ?
Coinflip s botom ✔
Galochku na duel ✔
Bolshe menshe 50/50 ✔
СДЕЛАТЬ СООБЩЕНИЯ В ЛС(БОЛЬШИНСТВО) ✔
rainbow role (mb)  ✔

            # $crime - ограбить (шанс на ограбление 40%, на проигрыш 60%) ✔

Репорты ✔
КРАЙМ НЕ РАБОТАЕТ
Баги ✔
Краш <3 
Manager - yt notifications
Как можно ещё сделать:


- Отдельный бот для статистики ✔
- Отдельный бот для радуги ✔

"""


class Economic(commands.Cog):

    def __init__(self, client):
        self.client = client 
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        self.cursor = self.conn.cursor()



    #Level-system
    @commands.Cog.listener()
    async def on_message(self, message):
        self.cursor.execute("UPDATE users SET messages = messages + {} WHERE id = {}".format(1, message.author.id))
        self.conn.commit()
        if message.author == self.client.user:
            return
        user = message.author
        self.cursor.execute("SELECT xp FROM users WHERE id = {}".format(user.id))
        xp = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(user.id))
        lvl = self.cursor.fetchone()[0]
        if xp >= 400+100*lvl:
            self.cursor.execute("UPDATE users SET lvl = lvl + {} WHERE id = {}".format(1, user.id))
            self.cursor.execute("UPDATE users SET xp = {} WHERE id = {}".format(0, user.id))
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(lvl*100+100, user.id))
            self.conn.commit()
            self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(user.id))
            lvl = self.cursor.fetchone()[0]
            await user.send(embed = discord.Embed (description = f'Поздравляю! Ты получил **{lvl}** уровень!\nТвоя награда: **{lvl*100} :tickets: **', color=0xfbff00), delete_after=60*10)
            if lvl == 10:
                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**⭐️Мама, кажется, я расту!⭐️**", color=0x66fcff)
                await user.send(embed=embed)
                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, user.id))
                self.conn.commit()
            elif lvl == 20:
                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🌟Биг Бой🌟**", color=0x66fcff)
                await user.send(embed=embed)
                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, user.id))
                self.conn.commit()
            elif lvl == 30:
                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**✨Дедуля✨**", color=0x66fcff)
                await user.send(embed=embed)
                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, user.id))
                self.conn.commit()
                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(user.id))
                ach = self.cursor.fetchone()[0]
                if ach == 27:
                    role = discord.utils.get(user.guild.roles, name="👑Склоните колено👑")
                    await user.add_roles(role)
                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, user.id))
                    self.conn.commit()
                    await user.send(embed=embed)
        else:
            self.cursor.execute("UPDATE users SET xp = xp + {} WHERE id = {}".format(5, user.id))
            self.conn.commit()
            
        self.cursor.execute("SELECT messages FROM users WHERE id = {}".format(user.id))
        msg = self.cursor.fetchone()[0]
        if msg == 100:
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**✏️На скорую руку✏️**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**500 :tickets:**", inline=False)
            await user.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(500, user.id))   
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, user.id))
            self.conn.commit()


        elif msg == 500:
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🖋Ну, я тут настрочил🖋**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**2500 :tickets:**", inline=False)
            await user.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(2500, user.id))   
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, user.id))
            self.conn.commit()

        elif msg == 5000:
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**📚Наследник Толстого📚**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**5000 :tickets:**", inline=False)
            await user.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(5000, user.id))   
            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, user.id))
            self.conn.commit()
            self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(user.id))
            ach = self.cursor.fetchone()[0]
            if ach == 27:
                role = discord.utils.get(user.guild.roles, name="👑Склоните колено👑")
                await user.add_roles(role)
                embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, user.id))
                self.conn.commit()
                await user.send(embed=embed)



    #Voice-ticket-xp system
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel:
            if after.mute or after.self_mute:
                return
            elif (len(after.channel.members) > 1):
                while after.channel and not after.self_mute:
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1, member.id))   
                    self.cursor.execute("UPDATE users SET voice_minutes = voice_minutes + 1 WHERE id = {}".format(member.id))   
                    self.conn.commit()

                    self.cursor.execute("SELECT voice_minutes FROM users WHERE id = {}".format(member.id))
                    voice = self.cursor.fetchone()[0]
                    if voice == 60*100:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🥉Орунькаю🥉**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                        await member.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, member.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, member.id))
                        self.conn.commit()

                    elif voice == 60*500:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🥈Орирую🥈**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**2000 :tickets:**", inline=False)
                        await member.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(2000, member.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, member.id))
                        self.conn.commit()

                    elif voice == 60*1000:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🥇У меня нет рта, но я должен кричать🥇**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**3000 :tickets:**", inline=False)
                        await member.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(3000, member.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, member.id))
                        self.conn.commit()
                        self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(member.id))
                        ach = self.cursor.fetchone()[0]
                        if ach == 27:
                            role = discord.utils.get(member.guild.roles, name="👑Склоните колено👑")
                            await member.add_roles(role)
                            embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                            embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, member.id))   
                            self.conn.commit()

                    await asyncio.sleep(60)
                else:
                    return
        elif not after.channel:
            # на случай если человек вышел из канала
            return



    # Info
    @commands.command(aliases = ['info', 'INFO', 'Info', 'balance'], usage = '!info / !info <@user> (при достижении 15 уровня) ')
    async def __info(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        if member is None:
            embed=discord.Embed(title="Статистика вашего аккаунта на сервере БиШ", color=0xff8800)
            embed.add_field(name="Имя", value = f'**{ctx.author}** 👦🏽', inline=False)
            embed.add_field(name="Дата захода на сервер", value = f'**{ctx.author.joined_at.strftime("%m/%d/%Y")}** 📅', inline=False)
            self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
            embed.add_field(name="Баланс", value = f'**{self.cursor.fetchone()[0]} :tickets:**', inline=False)
            self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id))
            embed.add_field(name="Уровень", value = f'**{self.cursor.fetchone()[0]} :confetti_ball:**', inline=False)
            self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id))
            all = 500 + 100*self.cursor.fetchone()[0]
            self.cursor.execute("SELECT xp FROM users WHERE id = {}".format(ctx.author.id))
            embed.add_field(name="Опыт", value = f'**{self.cursor.fetchone()[0]}/{all} ⭐️**', inline=False)
            self.cursor.execute("SELECT messages FROM users WHERE id = {}".format(ctx.author.id))
            embed.add_field(name="Количество сообщений", value = f'**{self.cursor.fetchone()[0]} :e_mail:**', inline=False)
            self.cursor.execute("SELECT voice_minutes FROM users WHERE id = {}".format(ctx.author.id))
            a = self.cursor.fetchone()[0]
            if a//60 < 10:
                if a%60 < 10:
                    embed.add_field(name="Время проведённое в войсе", value = f'**0{a//60}:0{a%60} 🎤 **', inline=False)
                else:
                    embed.add_field(name="Время проведённое в войсе", value = f'**0{a//60}:{a%60} 🎤 **', inline=False)
            else:
                if a%60 < 10:
                    embed.add_field(name="Время проведённое в войсе", value = f'**{a//60}:0{a%60} 🎤 **', inline=False)
                else:
                    embed.add_field(name="Время проведённое в войсе", value = f'**{a//60}:{a%60} 🎤 **', inline=False)
            self.cursor.execute("SELECT warns FROM users WHERE id = {}".format(ctx.author.id))
            embed.add_field(name="Количество варнов", value = f'**{self.cursor.fetchone()[0]} :no_entry:**', inline=False)
            await ctx.author.send(embed=embed, delete_after = 60*5)
        else:
            self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id))
            if self.cursor.fetchone()[0] < 15:
                await ctx.author.send(embed = discord.Embed(description = 'Для просмотра профелей других людей вам нужно иметь **15 уровень**'), delete_after = 60)
            else:
                embed=discord.Embed(title=f"Статистика пользователя {member.name} на сервере БиШ", color=0xff8800)
                embed.add_field(name="Имя", value = f'**{member}** 👦🏽', inline=False)
                embed.add_field(name="Дата захода на сервер", value = f'**{member.joined_at.strftime("%m/%d/%Y")} 📅**', inline=False)
                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                embed.add_field(name="Баланс", value = f'**{self.cursor.fetchone()[0]} :tickets:**', inline=False)
                self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(member.id))
                embed.add_field(name="Уровень", value = f'**{self.cursor.fetchone()[0]} :confetti_ball:**', inline=False)
                self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(member.id))
                all = 500 + 100*self.cursor.fetchone()[0]
                self.cursor.execute("SELECT xp FROM users WHERE id = {}".format(member.id))
                embed.add_field(name="Опыт", value = f'**{self.cursor.fetchone()[0]}/{all} ⭐️**', inline=False)
                self.cursor.execute("SELECT messages FROM users WHERE id = {}".format(member.id))
                embed.add_field(name="Количество сообщений", value = f'**{self.cursor.fetchone()[0]} :e_mail:**', inline=False)
                self.cursor.execute("SELECT voice_minutes FROM users WHERE id = {}".format(member.id))
                a = self.cursor.fetchone()[0]
                if a//60 < 10:
                    if a%60 < 10:
                        embed.add_field(name="Время проведённое в войсе", value = f'**0{a//60}:0{a%60} 🎤 **', inline=False)
                    else:
                        embed.add_field(name="Время проведённое в войсе", value = f'**0{a//60}:{a%60} 🎤 **', inline=False)
                else:
                    if a%60 < 10:
                        embed.add_field(name="Время проведённое в войсе", value = f'**{a//60}:0{a%60} 🎤 **', inline=False)
                    else:
                        embed.add_field(name="Время проведённое в войсе", value = f'**{a//60}:{a%60} 🎤 **', inline=False)
                self.cursor.execute("SELECT warns FROM users WHERE id = {}".format(member.id))
                embed.add_field(name="Количество варнов", value = f'**{self.cursor.fetchone()[0]} :no_entry:**', inline=False)
                await ctx.author.send(embed=embed, delete_after = 60*5)

    # DAILY
    @commands.command(aliases = ['daily', 'award'], usage = '!daily')
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def __daily(self, ctx):
        await ctx.message.delete()
        amount = random.randrange(100, 251)
        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount, ctx.author.id))
        self.conn.commit()     
        embed=discord.Embed(description=f':white_check_mark: **{ctx.author.name}** ты получил **{amount}** :tickets:!', color=0xe59eff)
        await ctx.author.send(embed=embed, delete_after = 60)

    @__daily.error
    async def daily_error(self, ctx, error):
        await ctx.message.delete()
        n = round(error.retry_after)
        def convert(n):
            return str(datetime.timedelta(seconds = n))
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.author.send(embed = discord.Embed(description = f':no_entry: {ctx.author.name}, ты сегодня уже брал дневной бонус\nПопробуй снова через: **{convert(n)}**!', color = 0xFFA500), delete_after = 60)



    # GIVE
    @commands.command(aliases = ['give'], usage = 'give <@user> <amount>')
    async def __give(self, ctx, member: discord.Member, amount: int):
        await ctx.message.delete()
        if ctx.author.id != 312795489743405058:
            await ctx.send(f'{ctx.author.mention} у вас недостаточно прав для использования данной команды!')
        else:
            if amount <= 0:
                await ctx.send(embed = discord.Embed(
                    description = f"__{ctx.author}__, ты чо, самый умный? Минус убери!"
                ))
            else:
                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount, member.id))
                self.conn.commit()
                await member.send(embed=discord.Embed(description = f'Твой баланс пополнен на **{amount}** :tickets: !\n\n*С любовью,* **{ctx.author.name}** *<3*'), delete_after = 60)

    @commands.command(aliases = ['take'], usage = 'take <@user> <amount>')
    async def __take(self, ctx, member: discord.Member = None, amount = None):
        await ctx.message.delete()
        if ctx.author.id != 312795489743405058:
            await ctx.send(f'{ctx.author.mention} у вас недостаточно прав для использования данной команды!')
        else:
            if int(amount) < 1:
                await ctx.send(embed = discord.Embed(
                    description = f"__{ctx.author}__, не надо так!"
                ))
            else:
                self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, member.id))
                self.conn.commit() 
                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id)) 
                a = self.cursor.fetchone()[0]
                if a < 0:
                    self.cursor.execute("UPDATE users SET balance = 0 WHERE id = {}".format(member.id))
                    self.conn.commit() 
                    await member.send(embed=discord.Embed(description = f'С **вашего** баланса сняты **все** средства!\n\n*С любовью,* **{ctx.author.name}** *<3*'), delete_after = 60)
                else:
                    await member.send(embed=discord.Embed(description = f'С **вашего** баланса снято **{amount}** :tickets: !\n\n*С любовью,* **{ctx.author.name}** *<3*'), delete_after = 60)


    @commands.command(
        name = "перевод",
        aliases = ['send'],
        breif = 'Перевод денег другому пользователю',
        usage = 'send <@user> <amount>'
    )
    async def __send(self, ctx, member: discord.Member, amount: int):
        await ctx.message.delete()

        if amount <= 0:
            await ctx.send(embed = discord.Embed(
                description = f"**{ctx.author}**, ты чо, самый умный? Минус убери!"
            ), delete_after = 5)
        elif member == ctx.author:
            await ctx.send(embed = discord.Embed(
                description = f"**{ctx.author}**, ты чо, самый умный?"
            ), delete_after = 5)
        elif type(amount) != int:
            await ctx.send(embed = discord.Embed(
                description = f"**{ctx.author}**, ты чего наделал?????"
            ), delete_after = 5)
        else:
            self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id)) 
            a = self.cursor.fetchone()[0]
            if a < amount:
                await ctx.send(embed = discord.Embed(
                    description = f"**{ctx.author}**, у тебя недостаточно средств для перевода"
                ), delete_after = 5)
            else:
                self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, ctx.author.id))
                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount, member.id))
                self.conn.commit()
                await member.send(embed=discord.Embed(description = f'**{ctx.author.name}** перевёл вам **{amount}** :tickets: !'), delete_after = 60)
                print(f'[log] {ctx.author} перевёл {member} {amount}')


#-----------------------------------------------------------------------------------GAMES---------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------GAMES---------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------GAMES---------------------------------------------------------------------------------------------------
    @commands.command(
        name = 'слоты',
        aliases=['slots', 'bet'],
        breif = 'Попыйтайте свою удачу в казино №1 в России!',
        usage = 'slots <сумма игры>')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def __slot(self, ctx, amount: int = None):
        await ctx.message.delete()
        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
        ubalance = self.cursor.fetchone()[0]
        if amount is None:
            await ctx.send(embed=discord.Embed(description = f'**{ctx.author.name}** введите сумму!'), delete_after = 5)
            ctx.command.reset_cooldown(ctx)
        elif amount < 1:
            await ctx.send(embed=discord.Embed(description = f'**{ctx.author.name}**, укажите сумму больше 0 :tickets:'), delete_after = 5)
            ctx.command.reset_cooldown(ctx)
        else:
            if ubalance < amount:
                await ctx.send(embed=discord.Embed(description = f"**{ctx.author}**, у вас недостаточно средств для игры!"), delete_after = 5)
                ctx.command.reset_cooldown(ctx)
            else:
                self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, ctx.author.id))
                self.conn.commit()
                emojis = "🍎🍊🍐🍋🍉🍇🍓🍒🥥🥝🍆🥒"
                a = random.choice(emojis)
                b = random.choice(emojis)
                c = random.choice(emojis)

                message = await ctx.send(embed=discord.Embed(description ='Начинаю крутить слоты....'), delete_after = 60)
                i = 1
                n = random.randint(1, 10)
                for i in range(n):
                    new_embed = discord.Embed(description = f'| {random.choice(emojis)} | {random.choice(emojis)} | {random.choice(emojis)} |')
                    await message.edit(embed=new_embed)
                    await asyncio.sleep(i/10)
                end_embed = discord.Embed(description = f'| {a} | {b} | {c} |')
                await message.edit(embed=end_embed)
                slotmachine = f"**| {a} | {b} | {c} |\n{ctx.author.name}**,"

                if (a == b == c):
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount*3, ctx.author.id))
                    self.conn.commit()
                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                    bal = self.cursor.fetchone()[0]
                    embed1=discord.Embed(description = f'{slotmachine} 3 в ряд, ты победил! 🎉\n Ваш баланс: **{bal}** :tickets:')
                    await message.edit(embed = embed1)
                    self.cursor.execute("UPDATE users SET slots_wins = slots_wins + {} WHERE id = {}".format(1, ctx.author.id))   
                    self.conn.commit()
                    self.cursor.execute("SELECT slots_wins FROM users WHERE id = {}".format(ctx.author.id))
                    a = self.cursor.fetchone()[0]
                    if a == 100:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**♟Опа стрик♟**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                    elif a == 250:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💰Мама, накрывай стол💰 **", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**2500 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(2500, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                    elif a == 500:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💎ЛЕГЧАЙШАЯ ДЛЯ ВЕЛИЧАЙШЕГО💎**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**5000 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(5000, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                        self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                        b = self.cursor.fetchone()[0]
                        if b == 27:
                            role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                            await ctx.author.add_roles(role)
                            embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                            embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                            await ctx.author.send(embed=embed)
    
                elif (a == b) or (a == c) or (b == c):
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount*2, ctx.author.id))
                    self.conn.commit()
                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                    bal = self.cursor.fetchone()[0]
                    embed2=discord.Embed(description = f'{slotmachine} 2 в ряд, ты победил! 🎉 \n Ваш баланс: **{bal}** :tickets:')
                    await message.edit(embed = embed2)
                    self.cursor.execute("UPDATE users SET slots_wins = slots_wins + {} WHERE id = {}".format(1, ctx.author.id))   
                    self.conn.commit()
                    self.cursor.execute("SELECT slots_wins FROM users WHERE id = {}".format(ctx.author.id))
                    a = self.cursor.fetchone()[0]
                    if a == 100:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**♟Опа стрик♟**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                    elif a == 250:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💰Мама, накрывай стол💰 **", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**2500 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(2500, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                    elif a == 500:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💎ЛЕГЧАЙШАЯ ДЛЯ ВЕЛИЧАЙШЕГО💎**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**5000 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(5000, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                        b = self.cursor.fetchone()[0]
                        if b == 27:
                            role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                            await ctx.author.add_roles(role)
                            embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                            embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                            self.conn.commit()
                            await ctx.author.send(embed=embed)
                else:
                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                    bal = self.cursor.fetchone()[0]
                    embed3=discord.Embed(description = f'{slotmachine} Нет совпадений, ты проиграл 😢\n Ваш баланс: **{bal}** :tickets:')
                    await message.edit(embed = embed3)

    @__slot.error
    async def slot_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(embed = discord.Embed(description = f':no_entry: {ctx.author.mention}, не так быстро. \nКрутить слоты можно раз в 10 секунд! \nПопробуй снова через: {round(error.retry_after)} секунд!', color = 0xFFA500), delete_after = 5)

    @commands.command(aliases = ['duel'], usage = '!duel <@user> <сумма игры>')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def __duel(self, ctx, member: discord.Member = None, amount: int = None):
        await ctx.message.delete()
        if member is None:
            await ctx.send(f"**{ctx.author.name}**, укажите пользователя, с которым желаете сразиться!", delete_after = 5)
            ctx.command.reset_cooldown(ctx)
        else:
            if amount is None:
                await ctx.send(f"**{ctx.author.name}**, укажите сумму, на которую желаете сразиться!", delete_after = 5)
                ctx.command.reset_cooldown(ctx)
            elif amount < 1:
                await ctx.send(f"**{ctx.author.name}**, укажите сумму больше 1 :tickets: ", delete_after = 5)
                ctx.command.reset_cooldown(ctx)
            else:
                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                ubal = self.cursor.fetchone()[0]
                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                mbal = self.cursor.fetchone()[0]
                if ubal < amount:
                    await ctx.send(f"**{ctx.author.name}**, у вас недостаточно средств для дуэли!", delete_after = 5)
                    ctx.command.reset_cooldown(ctx)
                elif mbal < amount:
                    await ctx.send(f"**{ctx.author.name}**, у {member.name} недостаточно средств для дуэли!", delete_after = 5)
                    ctx.command.reset_cooldown(ctx)
                else:
                    message = await ctx.send(f'**{ctx.author.name}** бросил дуэль **{member.name}**\nЖдём подтверждения от {member.mention} \n**{member.name}**, нажми на реакцию, чтобы принять участие в дуэли', delete_after = 30)
                    await message.add_reaction('✅')
                    def check(reaction, user):
                        return user == member and str(reaction.emoji) == '✅'
                    try:
                        await self.client.wait_for('reaction_add', timeout=60.0, check = check)
                    except asyncio.TimeoutError:
                        emb = discord.Embed(colour=discord.Color.green())
                        emb.add_field(name=':x: Дуэль', value = 'Действие отменнено!')
                        await ctx.send(embed = emb, delete_after=10 )
                    else:
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                        ubal = self.cursor.fetchone()[0]
                        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                        mbal = self.cursor.fetchone()[0]
                        if ubal < amount:
                            await ctx.send(f"**{ctx.author}**, у вас недостаточно средств для дуэли!\n Не надо пытаться меня переиграть!", delete_after = 5)
                            ctx.command.reset_cooldown(ctx)
                        elif mbal < amount:
                            await ctx.send(f"**{ctx.author}**, у {member.name} недостаточно средств для дуэли!\nНе нужно пытаться мне переиграть!", delete_after = 5)
                            ctx.command.reset_cooldown(ctx)
                        await message.delete()
                        n = random.randint(0, 1)
                        if n == 1:
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount, ctx.author.id))   
                            self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, member.id))   
                            self.conn.commit()
                            self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                            ubal = self.cursor.fetchone()[0]
                            self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                            mbal = self.cursor.fetchone()[0]
                            await ctx.send(f'**{ctx.author}** победил! Ему начислено **{amount} :tickets:** \nБаланс {ctx.author.name} составляет __{ubal}__:tickets:\nБаланс **{member.name}** составляет __{mbal}__:tickets:', delete_after = 15)
                            self.cursor.execute("UPDATE users SET duel_wins = duel_wins + {} WHERE id = {}".format(1, ctx.author.id))   
                            self.cursor.execute("UPDATE users SET duel_loses = duel_loses + {} WHERE id = {}".format(1, member.id)) 
                            self.conn.commit()
                            self.cursor.execute("SELECT duel_wins FROM users WHERE id = {}".format(ctx.author.id))
                            a = self.cursor.fetchone()[0]
                            self.cursor.execute("SELECT duel_loses FROM users WHERE id = {}".format(member.id))
                            c = self.cursor.fetchone()[0]
                            if a == 100:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🔫Дантес🔫**", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await ctx.author.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                b = self.cursor.fetchone()[0]
                                if b == 27:
                                    role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                    await ctx.author.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))
                                    self.conn.commit()
                                    await ctx.author.send(embed=embed)
                            elif c == 100:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🩸Пушкин🩸 **", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await member.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, member.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, member.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(member.id))
                                d = self.cursor.fetchone()[0]
                                if d == 27:
                                    role = discord.utils.get(member.guild.roles, name="👑Склоните колено👑")
                                    await member.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, member.id))   
                                    self.conn.commit()
                                    await member.send(embed=embed)
                        else:
                            self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, ctx.author.id))   
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount, member.id))   
                            self.conn.commit()
                            self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                            ubal = self.cursor.fetchone()[0]
                            self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(member.id))
                            mbal = self.cursor.fetchone()[0]
                            await ctx.send(f'**{member}** победил! Ему начислено **{amount} :tickets:**\nБаланс {member.name} составляет __{mbal}__:tickets:\nБаланс **{ctx.author.name}** составляет __{ubal}__:tickets:', delete_after = 15)
                            self.cursor.execute("UPDATE users SET duel_wins = duel_wins + {} WHERE id = {}".format(1, member.id))   
                            self.cursor.execute("UPDATE users SET duel_loses = duel_loses + {} WHERE id = {}".format(1, ctx.author.id))   
                            self.conn.commit()
                            self.cursor.execute("SELECT duel_wins FROM users WHERE id = {}".format(member.id))
                            e = self.cursor.fetchone()[0]
                            self.cursor.execute("SELECT duel_loses FROM users WHERE id = {}".format(ctx.author.id))
                            f = self.cursor.fetchone()[0]
                            if e == 100:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🔫Дантес🔫**", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await member.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, member.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, member.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(member.id))
                                ach = self.cursor.fetchone()[0]
                                if ach == 27:
                                    role = discord.utils.get(member.guild.roles, name="👑Склоните колено👑")
                                    await member.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))
                                    self.conn.commit()
                                    await member.send(embed=embed)
                            elif f == 100:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🩸Пушкин🩸 **", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await ctx.author.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                achi = self.cursor.fetchone()[0]
                                if achi == 27:
                                    role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                    await ctx.author.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, member.id))   
                                    self.conn.commit()
                                    await ctx.author.send(embed=embed)

    @__duel.error
    async def duel_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(embed = discord.Embed(description = f':no_entry: {ctx.author.mention}, тихо-тихо, не так быстро. \nНужно перезарядить револьвер \nПопробуй снова через: {round(error.retry_after)} секунд!', color = 0xFFA500))



    #Походу криминал
    @commands.command(aliases = ['crime'], usage = '!crime')
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def __crime(self, ctx):
        await ctx.message.delete()
        self.cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id))
        lvl = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
        bal = self.cursor.fetchone()[0]
        if lvl < 10:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, для доступа к ограблениям вам нужен **10 уровень**', color = discord.Color.red(), delete_after = 10))
        elif bal < 0:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, у вас отрицательный баланс!**', color = discord.Color.red(), delete_after = 10))

        else:
            amount = random.randint(0, 5001)
            message = await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, нам удалось обнаружить, что в сейфе находится **{amount} :tickets:**\nВы уверены, что хотите продолжить?', color = discord.Color.purple()))
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            def check(reaction, user):
                return user == ctx.author and (str(reaction.emoji) == '✅' or '❌')
            reaction, user = await self.client.wait_for('reaction_add', check = check)
            if str(reaction.emoji) == '✅':
                await message.clear_reactions()
                embed = discord.Embed(description = f'**{ctx.author.name}**, хорошо, давай продолжим.')
                await message.edit(embed = embed)
                await asyncio.sleep(5)
                end_embed = discord.Embed(description = 'Начинаю **взламывать** сейф...')
                await message.edit(embed=end_embed)
                n = random.randint(0,1)
                await asyncio.sleep(2)
                i = 1
                k = 1
                s='█'
                while i < 99:
                    rand = random.randint(1, 25)
                    k = k+1
                    i = i + rand
                    if i > 100:
                        break
                    embed2 = discord.Embed(description = f'Взлом сейфа...\n**{k*s} {str(i)}%**')
                    await message.edit(embed = embed2)

                if n == 0:
                    yes_embed = discord.Embed(description = 'Успех! ✅\nТебе **удалось** взломать сейф!')
                    await message.edit(embed = yes_embed)
                    await asyncio.sleep(3)
                    e = discord.Embed(description = f'**{ctx.author.name}**, поздравляю!\nТебе уже перечислили **{amount}** :tickets: на твой счёт')
                    await message.edit(embed = e)
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount, ctx.author.id))
                    self.conn.commit()
                    self.cursor.execute("UPDATE users SET crime_win = crime_win + {} WHERE id = {}".format(1, ctx.author.id))   
                    self.conn.commit()
                    await asyncio.sleep(10)
                    await message.delete()
                    self.cursor.execute("SELECT crime_win FROM users WHERE id = {}".format(ctx.author.id))
                    a = self.cursor.fetchone()[0]
                    if a == 100:
                            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💎День зарплаты💎**", color=0x66fcff)
                            embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                            await ctx.author.send(embed=embed)
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                            self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                            self.conn.commit()
                            self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                            ach = self.cursor.fetchone()[0]
                            if ach == 27:
                                    role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                    await ctx.author.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                                    self.conn.commit()
                                    await ctx.author.send(embed=embed)

                else:
                    no_embed = discord.Embed(description = 'Неудача! ❌\nК сожалению, тебе **не удалось** взломать сейф, за тобой уже выехала полиция🚔\nПопробуй скрыться одним из нижеперечисленных способов')
                    await message.edit(embed = no_embed)
                    await message.add_reaction("🎭")
                    await message.add_reaction("🔫")
                    await message.add_reaction("🎎")
                    escape = random.randint(0,2)
                    def check1(reaction, user):
                        return user == ctx.author and (str(reaction.emoji) == '🎭' or '🔫' or '🎎')
                    reaction, user = await self.client.wait_for('reaction_add', check = check1)
                    if str(reaction.emoji) == '🎭':
                        await message.clear_reactions()
                        if escape == 0:
                            emb = discord.Embed(description = 'Чтож, ты выбрал **верный способ** укрыться. Поздравляю')
                            await message.edit(embed = emb)
                            self.cursor.execute("UPDATE users SET crime_lose = crime_lose + {} WHERE id = {}".format(1, ctx.author.id))   
                            self.conn.commit()
                            self.cursor.execute("SELECT crime_lose FROM users WHERE id = {}".format(ctx.author.id))
                            b = self.cursor.fetchone()[0]
                            if b == 50:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🙏Матвей🙏**", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await ctx.author.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                ach = self.cursor.fetchone()[0]
                                if ach == 27:
                                    role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                    await ctx.author.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                                    self.conn.commit()
                                    await ctx.author.send(embed=embed)
                            await asyncio.sleep(10)
                            await message.delete()

                        else:
                            emb1 = discord.Embed(description = f'К сожалению, ты выбрал неверный способ побега. Теперь тебе нужно заплатить штраф в размере **{amount*1.5}:tickets:** ')
                            await message.edit(embed = emb1)
                            self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount*1.5, ctx.author.id))
                            self.conn.commit()
                            await asyncio.sleep(10)
                            await message.delete()

                    elif str(reaction.emoji) == '🔫':
                        await message.clear_reactions()
                        if escape == 1:
                            emb = discord.Embed(description = 'Чтож, ты выбрал **верный способ** укрыться. Поздравляю')
                            await message.edit(embed = emb)
                            self.cursor.execute("UPDATE users SET crime_lose = crime_lose + {} WHERE id = {}".format(1, ctx.author.id))   
                            self.conn.commit()
                            self.cursor.execute("SELECT crime_lose FROM users WHERE id = {}".format(ctx.author.id))
                            b = self.cursor.fetchone()[0]
                            if b == 50:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🙏Матвей🙏**", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await ctx.author.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                ach = self.cursor.fetchone()[0]
                                if ach == 27:
                                    role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                    await ctx.author.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                                    self.conn.commit()
                                    await ctx.author.send(embed=embed)
                            await asyncio.sleep(10)
                            await message.delete()
                        else:
                            emb1 = discord.Embed(description = f'К сожалению, ты выбрал неверный способ побега. Теперь тебе нужно заплатить штраф в размере **{amount*1.5}:tickets:** ')
                            await message.edit(embed = emb1)
                            self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount*1.5, ctx.author.id))
                            self.conn.commit()
                            await asyncio.sleep(10)
                            await message.delete()
                    elif str(reaction.emoji) == '🎎':
                        await message.clear_reactions()
                        if escape == 2:
                            emb = discord.Embed(description = 'Чтож, ты выбрал **верный способ** укрыться. Поздравляю')
                            await message.edit(embed = emb)
                            self.cursor.execute("UPDATE users SET crime_lose = crime_lose + {} WHERE id = {}".format(1, ctx.author.id))   
                            self.conn.commit()
                            self.cursor.execute("SELECT crime_lose FROM users WHERE id = {}".format(ctx.author.id))
                            b = self.cursor.fetchone()[0]
                            if b == 50:
                                embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🙏Матвей🙏**", color=0x66fcff)
                                embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                await ctx.author.send(embed=embed)
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                ach = self.cursor.fetchone()[0]
                                if ach == 27:
                                    role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                    await ctx.author.add_roles(role)
                                    embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                                    self.conn.commit()
                                    await ctx.author.send(embed=embed)
                            await asyncio.sleep(10)
                            await message.delete()
                        else:
                            emb1 = discord.Embed(description = f'К сожалению, ты выбрал неверный способ побега. Теперь тебе нужно заплатить штраф в размере **{amount*1.5}:tickets:** ')
                            await message.edit(embed = emb1)
                            self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount*1.5, ctx.author.id))
                            self.conn.commit()
                            await asyncio.sleep(10)
                            await message.delete()
            elif str(reaction.emoji) == '❌':
                await message.clear_reactions()
                embe = discord.Embed(description = 'Хорошо, можешь попробовать снова через 60 минут!')
                await message.edit(embed=embe)
                await asyncio.sleep(10)
                await message.delete()


                        
    @__crime.error
    async def crime_error(self, ctx,error):
        await ctx.message.delete()
        n = round(error.retry_after)
        def convert(n):
            return str(datetime.timedelta(seconds = n))
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.author.send(embed = discord.Embed(description = f':no_entry: {ctx.author.name}, тихо-тихо, подожди пока всё утихнет\nПопробуй снова через: **{convert(n)}**!', color = 0xFFA500), delete_after = 60)


# NVUTI

    @commands.command(aliases = ['nvuti'], usage = 'nvuti <сумма игры> + \n!nvuti <сумма игры> -')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def __nvuti(self, ctx, amount:int = None, result = None):
        await ctx.message.delete()
        if amount is None:
            await ctx.send(f'**{ctx.author.name}** укажите сумму игры.', delete_after = 5)
            ctx.command.reset_cooldown(ctx)
        else:
            if result is None: 
                await ctx.send(f'**{ctx.author.name}** укажите исход игры ``(!nvuti <amount> <+/->)``', delete_after = 5)
                ctx.command.reset_cooldown(ctx)
            else:
                if amount < 1:
                    await ctx.send(f'**{ctx.author.name}**, укажите сумму игры больше 0 :tickets:', delete_after = 5)
                    ctx.command.reset_cooldown(ctx)
                else:
                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                    ubal = self.cursor.fetchone()[0]
                    if amount > ubal:
                        ctx.command.reset_cooldown(ctx)
                        await ctx.send(f"**{ctx.author.name}**, у вас недостаточно средств для игры.", delete_after = 5)
                    else:
                        self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, ctx.author.id))
                        self.conn.commit()
                        n = random.randint(0, 100)
                        if result == '+':
                            if n > 50:
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount*2, ctx.author.id))
                                self.conn.commit()        
                                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                                ubal = self.cursor.fetchone()[0]                        
                                await ctx.send(embed=discord.Embed(description = f'{ctx.author.name} **успех** ! \nВаш баланс: __{ubal}__ :tickets:'), delete_after = 10)
                                self.cursor.execute("UPDATE users SET nvuti_wins = nvuti_wins + {} WHERE id = {}".format(1, ctx.author.id))  
                                self.conn.commit()
                                self.cursor.execute("SELECT nvuti_wins FROM users WHERE id = {}".format(ctx.author.id))
                                a = self.cursor.fetchone()[0]
                                if a == 100:
                                    embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💵Stonks!💵**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                    await ctx.author.send(embed=embed)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                    self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                    self.conn.commit()
                                    self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                    ach = self.cursor.fetchone()[0]
                                    if ach == 27:
                                        role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                        await ctx.author.add_roles(role)
                                        embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                        embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))   
                                        self.conn.commit()
                                        await ctx.author.send(embed=embed)
                            else:
                                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                                ubal = self.cursor.fetchone()[0]  
                                await ctx.send(embed = discord.Embed(description = f'{ctx.author.name} в этот раз не повезло!\nВаш баланс __{ubal}__ :tickets:'), delete_after = 10)
                        elif result == '-':
                            if n < 50:
                                self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount*2, ctx.author.id))
                                self.conn.commit()
                                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                                ubal = self.cursor.fetchone()[0]  
                                await ctx.send(embed=discord.Embed(description = f'{ctx.author.name} **успех** ! \nВаш баланс: __{ubal}__ :tickets:'), delete_after = 5)
                                self.cursor.execute("UPDATE users SET nvuti_wins = nvuti_wins + {} WHERE id = {}".format(1, ctx.author.id))   
                                self.conn.commit()
                                self.cursor.execute("SELECT nvuti_wins FROM users WHERE id = {}".format(ctx.author.id))
                                a = self.cursor.fetchone()[0]
                                if a == 100:
                                    embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💵Stonks!💵**", color=0x66fcff)
                                    embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                                    await ctx.author.send(embed=embed)
                                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                                    self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                                    self.conn.commit()
                                    self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                                    ach = self.cursor.fetchone()[0]
                                    if ach == 27:
                                        role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                                        await ctx.author.add_roles(role)
                                        embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                                        embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id))
                                        self.conn.commit()
                                        await ctx.author.send(embed=embed)
                            else:
                                self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                                ubal = self.cursor.fetchone()[0]  
                                await ctx.send(embed = discord.Embed(description = f'{ctx.author.name} в этот раз не повезло!\nВаш баланс __{ubal}__ :tickets:'), delete_after = 10)
                        else:
                            await ctx.send(f'{ctx.author.name} правильное использование команды: ``!nvuti <amount> <+/->``', delete_after = 5)
                            ctx.command.reset_cooldown(ctx)

    @__nvuti.error
    async def crime_error(self, ctx,error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(embed = discord.Embed(description = f':no_entry: {ctx.author.mention}, не так быстро!', color = 0xFFA500), delete_after = 5)
 
#coinflip w/ bot

    @commands.command(aliases = ['coinflip'], usage = '!coinflip <сумма игры>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def __coinflip(self, ctx, amount:int = None):
        await ctx.message.delete()
        self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
        ubal = self.cursor.fetchone()[0] 
        if amount is None:
            await ctx.send(f'**{ctx.author.name}**, укажите ставку', delete_after = 5)
            ctx.command.reset_cooldown(ctx)
        else:
            if amount < 1:
                await ctx.send(f'**{ctx.author.name}**, укажите сумму больше 0 :tickets:', delete_after = 5)
                ctx.command.reset_cooldown(ctx)
            elif amount > ubal:
                await ctx.send(f'**{ctx.author.name}**, у вас недостаточно средств для игры', delete_after = 5)
                ctx.command.reset_cooldown(ctx)
            else:
                self.cursor.execute("UPDATE users SET balance = balance - {} WHERE id = {}".format(amount, ctx.author.id))
                self.conn.commit()
                n = random.randint(0, 1)
                if n == 1:
                    self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(amount*2, ctx.author.id))
                    self.conn.commit()
                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                    ubal = self.cursor.fetchone()[0] 
                    await ctx.send(embed=discord.Embed(description  = f'**{ctx.author.name}**, поздравляю с победой!\nВаш баланс __{ubal}__ :tickets:'), delete_after = 10)
                    self.cursor.execute("UPDATE users SET coinflip_wins = coinflip_wins + {} WHERE id = {}".format(1, ctx.author.id))
                    self.conn.commit()
                    self.cursor.execute("SELECT coinflip_wins FROM users WHERE id = {}".format(ctx.author.id))
                    a = self.cursor.fetchone()[0] 
                    if a == 100:
                        embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**💵Stonks!💵**", color=0x66fcff)
                        embed.add_field(name="Твоя награда", value="**1000 :tickets:**", inline=False)
                        await ctx.author.send(embed=embed)
                        self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(1000, ctx.author.id))   
                        self.cursor.execute("UPDATE users SET achivements = achivements + {} WHERE id = {}".format(1, ctx.author.id))
                        self.conn.commit()
                        self.cursor.execute("SELECT achivements FROM users WHERE id = {}".format(ctx.author.id))
                        ach = self.cursor.fetchone()[0] 
                        if ach == 27:
                            role = discord.utils.get(ctx.author.guild.roles, name="👑Склоните колено👑")
                            await ctx.author.add_roles(role)
                            embed=discord.Embed(title="Ты получил ПОСЛЕДНЕЕ достижение!🥳", description="**🏆ЛЕГЕНДА🏆**", color=0x66fcff)
                            embed.add_field(name="Твоя награда", value="**10000 :tickets:**\nА также эксклюзивная роль ``👑Склоните колено👑``", inline=False)
                            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(10000, ctx.author.id)) 
                            self.conn.commit()
                            await ctx.author.send(embed=embed)
                else:
                    self.cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
                    ubal = self.cursor.fetchone()[0] 
                    await ctx.send(embed=discord.Embed(description = f'**{ctx.author.name}**, вы проиграли!\nВаш балас __{ubal}__ :tickets:'), delete_after = 10)
 

    @__coinflip.error
    async def crime_error(self, ctx,error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(embed = discord.Embed(description = f':no_entry: {ctx.author.mention}, не так быстро!', color = 0xFFA500), delete_after = 15)


    @commands.command(aliases = ['ebanut`_bota'])
    async def settozero(self, ctx):
        await ctx.message.delete()
        if ctx.author.id == 312795489743405058:
            message = await ctx.send('Бот начинает обнуляться...\nВы точно уверены что хотите это сделать?!\nНажмите на галочку, чтобы подтвердить действие ')
            await message.add_reaction('✅')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '✅'
            try:
                await self.client.wait_for('reaction_add', timeout=30.0, check = check)
            except asyncio.TimeoutError:
                emb = discord.Embed(colour=discord.Color.green())
                emb.add_field(name=':shushing_face: Обнуление:', value = 'Действие отменнено!')
                await ctx.send(embed = emb, delete_after=30 )
            else:
                await message.delete()
                for guild in self.client.guilds:
                    for member in guild.members:
                        self.cursor.execute("UPDATE users SET balance = 0, lvl = 1, xp = 0, messages = 0, warns = 0, voice_minutes = 0, invites = 0, duel_wins = 0, duel_loses = 0, music_tracks = 0, slots_wins = 0, crime_win = 0, crime_lose = 0, nvuti_wins = 0, coinflip_wins = 0, achivements = 0 WHERE id = {}".format(member.id))
                        self.conn.commit()
                        await ctx.send(f'{member.name} обнулён', delete_after = 3)
        else:
            await ctx.send('Это может сделать только мой создатель!')



def setup(client):
    client.add_cog(Economic(client))