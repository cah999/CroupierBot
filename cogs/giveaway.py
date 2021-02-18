import discord
from discord.ext import commands
import random
import asyncio
class giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

    def convert(self, time):
        pos = ["с","м","ч","д"]

        time_dict = {"с" : 1, "м" : 60, "ч" : 3600 , "д" : 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command(aliases = ['giveaway'])
    async def gstart(self, ctx):
        await ctx.message.delete()
        await ctx.send("Давай начнём **розыгрыш**! Ответь на пару вопросов, это займёт **15 секунд**!", delete_after = 15)

        questions = ["Укажи **канал**, в котором будет проходить **розыгрыш**", 
                    "Какова **длительность** розыгрыша? (с|м|ч|д)",
                    "Каков **приз** розыгрыша?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel 

        for i in questions:
            msg1 = await ctx.send(i, delete_after = 15)

            try:
                msg = await self.client.wait_for('message', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                await msg1.delete()
                await ctx.send('Ты не ответил **вовремя**! Будь быстрее в следующий раз!', delete_after = 15)
                return
            else:
                await msg.delete()
                answers.append(msg.content)
        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"Ты **неправильно** выбрал **канал**. Сделай в следующий раз это так {ctx.channel.mention}.", delete_after = 15)
            return

        channel = self.client.get_channel(c_id)

        time = self.convert(answers[1])
        if time == -1:
            await ctx.send(f"Ты **неправильно** указал **время**. Используй (с|м|ч|д) в следующий раз!", delete_after = 15)
            return
        elif time == -2:
            await ctx.send(f"**Время** должно быть **целочисленным**. Введи целочисленное значение в следующий раз", delete_after = 15)
            return            

        prize = answers[2]

        await ctx.send(f"**Розыгрыш** будет в {channel.mention} и будет продолжаться **{answers[1]}**!", delete_after = 15)

        embed = discord.Embed(title = "🎉 GIVEAWAY 🎉", description = f"``Нажми на реакцию, чтобы принять участие ``🎉", color = ctx.author.color)
        embed.add_field(name = "Приз розыгрыша:", value = f"**{prize}**")
        embed.set_footer(text = f"Конец через {answers[1]}")
        my_msg = await channel.send(embed = embed)

        await my_msg.add_reaction("🎉")
        await asyncio.sleep(time)
        new_msg = await channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        msg = await channel.send(f"Поздравляю! {winner.mention} выиграл {prize}!")
        await msg.add_reaction('✅')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        await self.client.wait_for('reaction_add', check=check)
        await msg.delete()
        await my_msg.delete()

    @gstart.error
    async def gstart_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            embed = discord.Embed(title = "<:fail:761292267360485378> Giveaway failed!", color = ctx.author.color)
            embed.add_field(name = "Причина:", value = "`Недостаточно прав!`")
            embed.add_field(name = "Как устранить:", value = "Получи права администратора, лол!")
            await ctx.send(embed = embed)
    
    @commands.command()
    async def reroll(self,ctx, channel : discord.TextChannel, id_ : int):
        await ctx.message.delete()
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("id сообщения был введён неверно.\nВ следующий раз тегни канал и затем напиши id сообщения", delete_after = 15)
            return
        
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        msg = await channel.send(f"**Реролл**\nПоздравляем! Новый победитель: {winner.mention}!")    
        await msg.add_reaction('✅')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        await self.client.wait_for('reaction_add', check=check)
        await msg.delete()


    @reroll.error
    async def reroll_error(self,ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Рерол не удался!", color = ctx.author.color)
            embed.add_field(name = "Причина:", value = "`Недостаточно прав!`")
            embed.add_field(name = "Что нужно:", value = "Получить права, лол!")
            await ctx.send(embed = embed)
def setup(client):
    client.add_cog(giveaway(client))