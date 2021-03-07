import discord
from discord.ext import commands
import random
import asyncio
import psycopg2
import os
class fun(commands.Cog):

    def __init__(self, client):
        self.client = client
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        self.cursor = self.conn.cursor()

    @commands.command(
        name="ролл",
        aliases=["roll"],
        breif="Генерация случайного числа от 1 до 100",
        usage="roll"
        )
    async def __roll(self, ctx, arg1=None, arg2=None):
        await ctx.message.delete()
        if (arg1 is None) and (arg2 is None):
            rand = random.randint(1, 100)
            await ctx.send(embed=discord.Embed(
                description=f"**{ctx.author.name}** роллит **1-100**\n"
                            f"Ваше случайное число: **{rand}** :diamonds:", color=0x00bfff), delete_after=60)
        elif arg2 is None:
            min = int(arg1.split('-')[0])
            max = int(arg1.split('-')[1])
            rand = random.randint(min, max)
            await ctx.send(embed=discord.Embed(
                description=f"**{ctx.author.name}** роллит **{min}-{max}**\n"
                            f"Ваше случайное число: **{rand}** :diamonds:", color=0x00bfff), delete_after=60)
        else:
            print(arg1, arg2)
            rand = random.randint(arg1, arg2)
            await ctx.send(embed=discord.Embed(
                description=f"**{ctx.author.name}** роллит **{str(arg1)}-{str(arg2)}**\n"
                            f"Ваше случайное число: **{rand}** :diamonds:", color=0x00bfff), delete_after=60)



    # @commands.command(
    #     name="ролл",
    #     aliases=["roll"],
    #     breif="Генерация случайного числа от 1 до 100",
    #     usage="roll"
    #     )
    # async def __roll(self, ctx, min = 1, max = 100 ):
    #     await ctx.message.delete()
    #     if min <= 0:
    #         embed=discord.Embed(description=":x: Введите число больше 0 ", color=0xff0000)
    #         await ctx.send(embed=embed, delete_after = 3)
    #     elif max > 2147483647:
    #         max = 2147483647
    #         rand = random.randrange(min, max+1)
    #         embed=discord.Embed(description=f"**{ctx.author.name}** роллит ``{min}-{max}``\nВаше случайное число: **{str(rand)}** :diamonds:", color=0x00bfff)
    #         await ctx.send(embed=embed, delete_after = 60)
    #     elif max < min:
    #         await ctx.send(embed= discord.Embed(description = f'{ctx.author} укажите максимальное число больше минимального!', color=0x00bfff))
    #     else:
    #         rand = random.randrange(min, max+1)
    #         embed=discord.Embed(description=f"**{ctx.author.name}** роллит ``{min}-{max}``\nВаше случайное число: **{str(rand)}** :diamonds:", color=0x00bfff)
    #         await ctx.send(embed=embed, delete_after = 60)

    @commands.command(aliases = ['flip'], usage = '!flip')
    async def __flip(self, ctx):
        await ctx.message.delete()
        n = random.randint(0, 1)
        result = 'Орёл' if n == 1 else 'Решка'
        if result == 'Орёл':
            embed=discord.Embed(description=f"**{ctx.author.name}** подбрасывает **монетку**\nВам выпал: **{result}** :new_moon:", color=0xd7fe90)
        else:
            embed=discord.Embed(description=f"**{ctx.author.name}** подбрасывает **монетку**\nВам выпала: **{result}** :full_moon:", color=0xd7fe90)

        await ctx.send(embed=embed, delete_after=60)


    @commands.command(aliases = ['dice'], usage = '!dice')
    async def __dice(self, ctx):
        await ctx.message.delete()
        n = random.randrange(1, 7)
        embed=discord.Embed(description=f"**{ctx.author.name}** кидает **кубик**\nНа грани: **{str(n)}** :game_die:", color=0xfb00ff)
        await ctx.send(embed=embed, delete_after=60)


    @commands.command(aliases=['рулетка'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_guild_permissions(manage_messages=True)
    async def russiablyat(self, ctx):
        try:
            channel = ctx.message.author.voice.channel
        except:
            return await ctx.send( 'Вы не находитесь в каком либо голосовом канале!' )
        print(len(channel.members))
        await ctx.message.delete()
        while len(channel.members) > 1:
            message = await ctx.send("``3``")
            await asyncio.sleep(0.5)
            await message.edit(content="``2``")
            await asyncio.sleep(0.5)
            await message.edit(content="``1``")
            await asyncio.sleep(0.5)
            dead = random.choice(channel.members)
            await message.edit(content=f"бум")
            await asyncio.sleep(0.5)
            await dead.move_to(None)
            await message.edit(content=None, embed=discord.Embed(description=f'{dead.mention} словил пулю... Помянем F'))
            await asyncio.sleep(2)

    # @commands.command(aliases = ['bunker'])
    # async def __bunker(self, ctx, payload):
    #     mess = await ctx.send('Набор в игру')
    #     payload.emoji = '✅'
    #     await mess.add_reaction('✅')
    #     await asyncio.sleep(10)
    #     mess = await ctx.channel.fetch_message(mess.id)
    #     if payload.emoji.users := discord.utils.get(mess.reactions, emoji=ctx.guild.get_emoji(471483388532742130)):
    #         async for user in '✅'.users:
    #             print(str(user)) 
    # @commands.command(aliases = ['senda'])
    # @commands.has_guild_permissions(manage_messages=True)
    # async def __senda(self, ctx, member:discord.Member = None):
    #     await ctx.channel.purge (limit = 1)
    #     embed=discord.Embed(title="Ответы ", description="**Второй** вариант\n\n**1** - ``35``\n**2** - ``yzx``\n**3** - ``2``\n**4** - ``23``\n **5** - ``7``\n**6** - ``165``\n**7** - ``340``\n**8** - ``504``\n**9** - ``1832``\n**10** - ``4``\n**11** - ``150``\n**12** - ``19``\n**13** - ``15``\n**14** - ~~???~~\n**15** - ``820``\n**19** - ``7``\n**20**- ``1619``\n**21** - ``18``", color=0x80ffce)
    #     embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    #     await member.send(embed=embed)

    @commands.command(aliases = ['chlen', 'hui', 'член'], usage = '!член')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def __chlen(self, ctx):
        await ctx.message.delete()
        n = random.randint(-3, 27)
        if n == -3 or n == -2 or n == 2 or n == 3 or n == 4:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, ну и хуек у тебя...\n**{n}** сантиметра'), delete_after = 10)
        elif n == 0:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, так ты вообще без хуя...\n**{n}** сантиметров'), delete_after = 10)
        elif n == 1 or n == -1:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, да уж, как ты с такой валыной живёшь...\n**{n}** сантиметр'), delete_after = 10)
        else:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, твой хуёк не так уж плох...\n**{n}** сантиметров'), delete_after = 10)            

    @commands.command(aliases = ['gay', 'gaymeter', 'гей'], usage = '!гей')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def __gay(self, ctx):
        await ctx.message.delete()
        n = random.randint(0, 100)
        if n == 0:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, вопросов нет. Натурал.\nТы гей на **{n}%**'), delete_after = 10)
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🤵🏻УБЕРНАТУРАЛ🤵🏻**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**500 :tickets:**", inline=False)
            await ctx.author.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(500, ctx.author.id))   
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
        if n <= 30:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, ну немного конечно есть, но можешь считать себя не геем...\nТы гей на **{n}%**'), delete_after = 10)
        elif n > 30 and n < 50:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, ладно, ещё сойдёт...\n Ты гей на **{n} %**'), delete_after = 10)
        elif n >= 50 and n < 99:
            await ctx.send(embed = discord.Embed(description = f'Ясно, **{ctx.author.name}** гей...\nТы гей на **{n} %**'), delete_after = 10)
        else:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, АХАХАХАХАХАХАХАХ. Соболезную.\nТы гей на **{n} %**'), delete_after = 10)
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🌈Welcome to the club, buddy🌈**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**500 :tickets:**", inline=False)
            await ctx.author.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(500, ctx.author.id))   
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


    @commands.command(aliases = ['roleroll'])
    async def __roles1(self, ctx, member1:discord.Member = None, member2:discord.Member = None, member3:discord.Member = None, member4:discord.Member = None, member5:discord.Member = None):
        await ctx.message.delete()
        roles = ['мидер','кери','оффлейнер','саппорт','фул саппорт']
        random.shuffle(roles)
        await ctx.send(embed = discord.Embed(description = f'**{member1.name}** - {roles[0]}\n**{member2.name}** - {roles[1]}\n**{member3.name}** - {roles[2]}\n**{member4.name}** - {roles[3]}\n**{member5.name}** - {roles[4]}'), delete_after = 15)

    @commands.command(aliases = ['rdota'], usage = '!rdota')
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def __roles(self, ctx):
        await ctx.message.delete()
        colors = ['0x28bd93','0x6b9fff','0xff0073','0x8e27aa','0x12678c','0x75f5d5','0x52ff8e','0xfcfcfc','0x0b8e0f','0xe2ff9e','0xffb029','0xc67e76','0x6b7cff','0xfbff00','0x44ff00']
        roles = ['мидер','кери','оффлейнер','саппорт','фул саппорт']
        end = []
        random.shuffle(roles)
        try:
            channel = ctx.message.author.voice.channel
        except:
            return await ctx.send( 'Вы не находитесь в каком либо голосовом канале!', delete_after = 5)
        else:
            member = channel.members
            n = len(channel.members)
            message = await ctx.send(embed=discord.Embed(description = 'Начинаю выдавать роли...'),delete_after = 60)
            for i in range(1, n+1):
                embed=discord.Embed(description = f'**{member[i-1].mention}** - {roles[i-1]}', color = 0x6b9fff)
                end.append(f"{member[i-1].name} | {roles[i-1]} ") 
                await message.edit(embed=embed)
                await asyncio.sleep(5)
            if n == 1:
                emb = discord.Embed(description = f"**{end[0]}**", color = 0x32aafd, timestamp = ctx.message.created_at)
                await message.edit(embed = emb)
            elif n == 2:
                emb = discord.Embed(description = f"**{end[0]}\n\n{end[1]}**", color = 0x32aafd, timestamp = ctx.message.created_at)
                await message.edit(embed = emb)
            elif n == 3:
                emb = discord.Embed(description = f"**{end[0]}\n\n{end[1]}\n\n{end[2]}**", color = 0x32aafd, timestamp = ctx.message.created_at)
                await message.edit(embed = emb)
            elif n == 4:
                emb = discord.Embed(description = f"**{end[0]}\n\n{end[1]}\n\n{end[2]}\n\n{end[3]}**", color = 0x32aafd, timestamp = ctx.message.created_at)
                await message.edit(embed = emb)
            elif n == 5:
                emb = discord.Embed(description = f"**{end[0]}\n\n{end[1]}\n\n{end[2]}\n\n{end[3]}\n\n{end[4]}**", color = 0x32aafd, timestamp = ctx.message.created_at)
                await message.edit(embed = emb)
            
        # embed = discord.Embed(description = '')


    @commands.command(aliases = ['iq', 'iqtest', 'айку'], usage = '!айку')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def __iq(self, ctx):
        await ctx.message.delete()
        n = random.randint(-100, 200)
        
        if n == -100:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, Рофлан поминки...**{n} iq**'), delete_after = 10)
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🧟‍♂️У МИНЯ БАЛЬШОЙ МОСГ🧟‍♂️**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**500 :tickets:**", inline=False)
            await ctx.author.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(500, ctx.author.id))   
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

        elif n < 0:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, Ессс, минус **{-1*n} iq** уху!'), delete_after = 10)
        elif n < 30 and n > 0:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, чел, ты такой глупый...\nТвой iq: **{n}**'), delete_after = 10)
        elif n > 30 and n < 70:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, ну ты и тупик...\nТвой iq: **{n}**'), delete_after = 10)
        elif n > 70 and n < 100:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, неплохо. \nТвой iq: **{n}**'), delete_after = 10)
        elif n >= 100 and n < 199:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, мои поздравления, ты реально умён, бро!\nТвой iq: **{n}**'), delete_after = 10)
        else:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, СВЕРХЧЕЛОВЕК!\nТвой iq: **{n}**'), delete_after = 10)  
            embed=discord.Embed(title="Ты получил новое достижение!🥳", description="**🧠Пишу ответы майл ру🧠**", color=0x66fcff)
            embed.add_field(name="Твоя награда", value="**500 :tickets:**", inline=False)
            await ctx.author.send(embed=embed)
            self.cursor.execute("UPDATE users SET balance = balance + {} WHERE id = {}".format(500, ctx.author.id))   
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


    @commands.command(aliases = ['eblanvtime', 'еблан_в_тиме', 'дота2', 'dota'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def __dota(self, ctx):
        await ctx.message.delete()
        with open ('./cogs/resources/obidno.txt', encoding='utf-8') as file:
            obzivaka = file.readlines()
            obzivakarand = random.choice(obzivaka)
            await ctx.author.send(embed = discord.Embed(description = f'**{obzivakarand}**'), delete_after = 60*10)

    @__dota.error
    async def dota_error(self, ctx,error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.author.send(embed = discord.Embed(description = f':no_entry: {ctx.author.mention}, не так быстро!', color = 0xFFA500), delete_after = 5)


    @commands.command()
    async def button(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send('Тут есть кнопка\nНажми на меня!')
        await msg.add_reaction('🔴')
        await msg.add_reaction('🔁')
        def check(reaction, user):
            return str(reaction.emoji) == '🔁' and user == ctx.author
        while True:
            user, reaction = await self.client.wait_for('reaction_add', check = check)
            await msg.clear_reactions() 
            await msg.add_reaction('🔴')
            await msg.add_reaction('🔁')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        channel = self.client.get_channel(796005631865782273)
        if member != self.client.user:
            if str(payload.emoji) == '🔴':
                await channel.send(embed = discord.Embed(description = f'**{member.name}** нажал на красную кнопку!'), delete_after = 5)

        # elif member.id == 312795489743405058:
        #     return
        else:
            return




def setup(client):
    client.add_cog(fun(client))