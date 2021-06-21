import discord
from discord.ext import commands
import datetime
import psycopg2
import os

answer5 = ['Вы не можете замутить пользователя с такой же ролью!', 'Ваши роли одинаковы, я не могу так сделать!', 'Вы не можете замутить такого же модератора как и вы!']
answer4 = ['Это невозможно сделать, так как выгнать меня может только основатель сервера!', 'Это может сделать только основатель сервера', 'Так сделать невозможно!', 'Увы, меня нельзя так остранить...']
answer3 = ['У вас не хватает прав!', 'Его роль стоит выше вашей!', 'Это нельзя сделать!', 'Ваша роль менее значима, чем этого пользователя!']
answer2 = ['Ты быканул на основателя сервера, или мне показалось?', 'Что он такого плохого тебе сделал?', 'При всём уважении к тебе я так не могу сделать!', 'Ах если бы я так мог...', 'Я не буду этого делать!', 'Сорян, но не в моих это силах!']
answer = ['Самоубийство не приведёт ни к чему хорошему!', 'Напомню: суицид - не выход!', 'Увы, я не могу этого сделать!', 'Самоубийство - не выход!', 'Не надо к себе так относиться!', 'Я не сделаю этого!', 'Я не буду это делать!', 'Я не выполню это действие', 'Не заставляй меня это сделать!']


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client
        DATABASE_URL = os.environ['DATABASE_URL']
        self.conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
        self.cursor = self.conn.cursor()




    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(773201336761974814)
        if message.channel == channel:
            if message.content.startswith('!'):
                pass
            else:
                if message.author == self.client.user:
                    pass
                else:
                    await message.delete()
                    await message.author.send(embed = discord.Embed(description = f'В канале ``{channel.name}`` можно писать **только** команды для **бота**!'), delete_after = 30)



    # clear msg
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, amount = 100 ):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
        if (amount == 0) or (amount < 0) :
            await ctx.send(embed = discord.Embed(description = f':x: Введите количество сообщений для удаления!'), delete_after = 3)
        else:
            await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений'), delete_after = 3)


    # Kick
    @commands.command()
    @commands.has_permissions(administrator = True)

    async def kick(self, ctx, member: discord.Member, *, reason = None ):
        await ctx.message.delete()
        if member.id == 312795489743405058 or member.id == 475975938577006595 or member.id == 340368453976457216 or member.id == 483866841148686337 or member.id == 715914571839176786 or member.id == 601309336454823936:
            await ctx.send(f'Ты тут давай не быкуй на **{member.name}**')
        else:
            await member.kick (reason = reason)
            embed=discord.Embed(description=f"{member.mention} был кикнут с сервера!", color=0x5abaa7)
            await member.send(embed=discord.Embed(description=f"Вы были кикнуты с сервера!\nПричина {reason}", color=0x5abaa7))
            await ctx.send(embed=embed, delete_after = 30)

    #Ban
    @commands.command()
    @commands.has_permissions(administrator = True)

    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.message.delete()
        if member.id == 312795489743405058 or member.id == 475975938577006595 or member.id == 340368453976457216 or member.id == 483866841148686337 or member.id == 715914571839176786 or member.id == 601309336454823936:
            await ctx.send(f'Ты тут давай не быкуй на **{member.name}**')
        else:
            emb = discord.Embed(title = '{} banned'.format(member.name), colour = discord.Color.red())

            await member.ban(reason = reason)
            await member.send(embed=discord.Embed(description=f"Вы были заблокированы на сервере!\nПричина **{reason}**\nДля разблокировки обращайтесь к {ctx.author.mention}", color=0x5abaa7))
            emb.add_field( name = 'Причина бана: ', value = str(reason))
            emb.set_footer(text = '{}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = emb, delete_after = 30)


    # Unban
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, member):
        await ctx.message.delete()

        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)

            embed=discord.Embed(description=f"**{user.mention}** был разблокирован на сервере!", color=0x5abaa7)
            await ctx.send(embed=embed, delete_after = 30)
            return

    # Warn
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def warn(self, ctx, member: discord.Member, *, reason = None):
        await ctx.message.delete()
        if member.id == 312795489743405058 or member.id == 475975938577006595 or member.id == 340368453976457216 or member.id == 483866841148686337 or member.id == 715914571839176786 or member.id == 601309336454823936:
            await ctx.send(f'Ты тут давай не быкуй на {member.name}')
        else:
            emb = discord.Embed(title = '{} warned!'.format(member.name), colour = discord.Color.red())
            self.cursor.execute("UPDATE users SET warns = warns + {} WHERE id = {}".format(1, member.id))   
            self.conn.commit()
            self.cursor.execute("SELECT warns FROM users WHERE id = {}".format(member.id))
            warns = self.cursor.fetchone()[0]
            emb.add_field( name = 'Причина варна: ', value = str(reason) )
            emb.add_field( name = 'Количество варнов: ', value = warns)
            emb.set_footer(text = '{}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed = emb, delete_after = 30)

            if warns >= 3:
                await member.ban(reason = '{member.name} получил 3 варна!')
                emb = discord.Embed(title = '{} banned'.format(member.name), colour = discord.Color.red())
                emb.add_field( name = 'Причина бана: ', value = '3 варна')
                emb.set_footer(text = '{}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
                await ctx.send(embed = emb, delete_after = 30)

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clearwarns(self, ctx, member: discord.Member):
        self.cursor.execute("UPDATE users SET warns = {} WHERE id = {}".format(0, member.id))   
        self.conn.commit()
        await ctx.send(embed=discord.Embed(description = f'С пользователя **{member.name}** сняты все варны!'), delete_after = 6)

    # Auto Role
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="Участник")
        await member.add_roles(role)

#    @commands.Cog.listener()
#    async def on_member_update(self, before, after):
#        if after.id == 483866841148686337:
#            if before.roles != after.roles:
#                for role in after.roles:
#                    if role.id in [774285935240151050, 774285953350369291]:
#                        await after.remove_roles(role, reason='Заработай ты нормально на эту ебаную роль')

    # # Invite Create
    # @commands.Cog.listener()
    # async def on_invite_create(self, invite: discord.Invite):
    #     member = invite.inviter
    #     channel = self.client.get_channel(779274823511310376) #Айди канала для логов
    #     embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Создано приглашение**')
    #     embed.add_field(name='Код инвайта: ', value=invite.code, inline=False)
    #     embed.add_field(name='Максимально использаваний: ', value=invite.max_uses, inline=False)
    #     embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    #     await channel.send(embed=embed)


    @commands.command(aliases=['report', 'жалоба'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def __report(self, ctx, member: discord.Member=None, *, reason=None):
        await ctx.message.delete()
        if member is None:
            embed = discord.Embed(title="Ошибка", description="Укажите пользователя `!report <member> <reason>`", color=discord.Color.red())
            await ctx.send(embed=embed, delete_after = 10)
            ctx.command.reset_cooldown(ctx)
        elif reason is None:
            embed = discord.Embed(title="Ошибка", description="Укажите причину жалобы `!report <member> <reason>`", color=discord.Color.red())
            await ctx.send(embed=embed, delete_after = 10)
            ctx.command.reset_cooldown(ctx)
        elif member == ctx.author:
            embed = discord.Embed(title="Ошибка", description="Вы не можете отправить жалобу на себя", color=discord.Color.red())
            await ctx.send(embed=embed, delete_after = 10)
            ctx.command.reset_cooldown(ctx)
        else:
            if ctx.message.attachments:
                for i in ctx.message.attachments:
                    channel = ctx.guild.get_channel(779274823511310376)
                    embed = discord.Embed(title="Жалоба", description=f'Жалоба была успешно отправлена в канал для жалоб!', color=discord.Color.green())
                    await ctx.send(embed=embed, delete_after = 10)
                    embed2 = discord.Embed(title='Новая Жалоба!", description=f"**Отправитель:** {ctx.author.mention}\n\n**Нарушитель:** {member.mention}\n\n**Причина:** {reason}', color=discord.Color.green())
                    embed2.set_image(url=i.url)
                    msg = await channel.send(embed=embed2)
                    await msg.add_reaction("✅")
                    await msg.add_reaction("❌")
                    def check(reaction, user):
                        return (str(reaction.emoji) == '✅' or '❌') and reaction.count == 4
                    reaction, user = await self.client.wait_for('reaction_add', check = check)
                    if str(reaction.emoji) == '✅':
                        await message.delete()
                        await channel.send(embed = discord.Embed(description = 'Жалоба от пользователя {ctx.author.mention успешно принята!'))
                    else:
                        await message.delete()
                        await channel.send(embed = discord.Embed(description = f'Жалоба от пользователя {ctx.author.mention} отклонена!'), delete_after = 15)
                
                    break
            else:
                channel = ctx.guild.get_channel(779274823511310376)
                embed = discord.Embed(title=f"Жалоба", timestamp=datetime.datetime.now(datetime.timezone.utc), description=f':white_check_mark: Жалоба была успешно отправлена в канал для жалоб!', color=discord.Color.green())
                await ctx.send(embed=embed, delete_after = 10)
                embed2=discord.Embed(title="Новая жалоба", timestamp=datetime.datetime.now(datetime.timezone.utc), color=0xff0000)
                embed2.add_field(name="Отправитель", value=f"{ctx.author.mention}", inline=False)
                embed2.add_field(name="Нарушитель", value=f"{member.mention}", inline=False)
                embed2.add_field(name="Причина", value=f"{reason}", inline=False)
                embed2.set_footer(text="Модераторам ку, остальным соболезную")
                message = await channel.send(embed=embed2)
                await message.add_reaction("✅")
                await message.add_reaction("❌")
                def check(reaction, user):
                    return (str(reaction.emoji) == '✅' or '❌') and reaction.count == 4
                reaction, user = await self.client.wait_for('reaction_add', check = check)
                if str(reaction.emoji) == '✅':
                    await message.delete()
                    await channel.send(embed = discord.Embed(description = f'Жалоба от {ctx.author.mention} успешно принята!'), delete_after = 15)
                else:
                    await message.delete()
                    await channel.send(embed = discord.Embed(description = f'Жалоба от {ctx.author.mention} отклонена!'), delete_after = 15)

    @commands.command(aliases=['баг', 'bug'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def __bug(self, ctx, *, reason=None):
        await ctx.message.delete()
        if reason is None:
            embed = discord.Embed(title="Ошибка", description="Укажите баг `!bug <text>`", color=discord.Color.red())
            await ctx.send(embed=embed, delete_after = 10)
            ctx.command.reset_cooldown(ctx)
        else:
            if ctx.message.attachments:
                for i in ctx.message.attachments:
                    channel = ctx.guild.get_channel(779274823511310376)
                    embed = discord.Embed(title="Баг!", description=f":white_check_mark: Баг был успешно отправлен в канал для багов!", color=discord.Color.green())
                    await ctx.send(embed=embed, delete_after = 10)
                    embed2=discord.Embed(title="Новый баг!", timestamp=datetime.datetime.now(datetime.timezone.utc), color=0xff0000)
                    embed2.add_field(name="Отправитель", value=f"{ctx.author.mention}", inline=False)
                    embed2.add_field(name="Описание", value=f"{reason}", inline=False)
                    embed2.set_footer(text="Кодеру ку, остальным соболезную")
                    embed2.set_image(url=i.url)
                    msg = await channel.send(embed=embed2)
                    await msg.add_reaction("✅")
                    coder = 312795489743405058
                    def check(reaction, user):
                        return user.id == coder and (str(reaction.emoji) == '✅')
                    reaction, user = await self.client.wait_for('reaction_add', check = check)
                    await msg.delete()
                    await channel.send(embed = discord.Embed(description = f'Баг от {ctx.author.mention} обработан!', color = discord.Color.green()), delte_after = 15)
                    break
            else:
                channel = ctx.guild.get_channel(779274823511310376)
                embed = discord.Embed(title="Баг", timestamp=datetime.datetime.now(datetime.timezone.utc), description=f":white_check_mark: Баг был успешно отправлен в канал для багов!", color=0xfbff00)
                await ctx.send(embed=embed, delete_after = 10)
                embed2=discord.Embed(title="Новый баг!", timestamp=datetime.datetime.now(datetime.timezone.utc), color=0xfbff00)
                embed2.add_field(name="Отправитель", value=f"{ctx.author.mention}", inline=False)
                embed2.add_field(name="Описание", value=f"{reason}", inline=False)
                embed2.set_footer(text="Кодеру ку, остальным соболезную")
                msg = await channel.send(embed=embed2)
                await msg.add_reaction("✅")
                coder = 312795489743405058
                def check(reaction, user):
                    return user.id == coder and (str(reaction.emoji) == '✅')
                reaction, user = await self.client.wait_for('reaction_add', check = check)
                await msg.delete()
                await channel.send(embed = discord.Embed(description = f'Баг от {ctx.author.mention} обработан!', color = discord.Color.green()), delete_after = 15)


    @__report.error
    async def report_error(self, ctx,error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(embed = discord.Embed(description = f':no_entry: {ctx.author.mention}, не так быстро!. \nОтправлять жалобы можно раз в 10 секунд!', color = 0xFFA500), delete_after = 15)





def setup(client):
    client.add_cog(mod(client))