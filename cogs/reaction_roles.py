import discord
from discord.ext import commands
from discord import utils

class rr(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases = ['channels'])
    # ROLES
    async def _channels(self, ctx):
        dota = utils.get(ctx.message.guild.emojis, name="RoflanDota2")
        csgo = utils.get(ctx.message.guild.emojis, name="RoflanCsGo")
        among = utils.get(ctx.message.guild.emojis, name="RoflanAmongUs")
        gta = utils.get(ctx.message.guild.emojis, name="RoflanGTAV")
        si = utils.get(ctx.message.guild.emojis, name="RoflanSI")
        rocket = utils.get(ctx.message.guild.emojis, name="RoflanLeague")
        ds = utils.get(ctx.message.guild.emojis, name="RoflanDS")
        genshin = utils.get(ctx.message.guild.emojis, name="RoflanGenshi")
        mine = utils.get(ctx.message.guild.emojis, name="RoflanMinecraft")
        terraria = utils.get(ctx.message.guild.emojis, name="RoflanTerraria")

    
        await ctx.channel.purge (limit = 1)
        embed=discord.Embed(title="Игровые каналы", description="**Нажми на реакцию, чтобы получить доступ к игровым каналам**", color=0xe770ff)
        embed.add_field(name="\u200b", value=f"**{dota} - <@&764732857926156308>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{csgo} - <@&764732928726532137>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{among} - <@&764732179607453736>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{gta} - <@&764732887005659157>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{si} - <@&764756169519661127>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{rocket} - <@&764733602986065960>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{ds} - <@&764742481194778634>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{genshin} - <@&764734209964769281>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{mine} - <@&764742579224051722>**", inline=False)
        embed.add_field(name="\u200b", value=f"**{terraria} - <@&766653096050032682>**", inline=False)
        message = await ctx.send(embed=embed)

        await message.add_reaction(dota)
        await message.add_reaction(csgo)
        await message.add_reaction(among)
        await message.add_reaction(gta)
        await message.add_reaction(si)
        await message.add_reaction(rocket)
        await message.add_reaction(ds)
        await message.add_reaction(genshin)
        await message.add_reaction(mine)
        await message.add_reaction(terraria)




    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        overwrite.use_voice_activation = True
        overwrite.connect = True
        overwrite.speak = True
        overwrite.stream = True
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        if message_id == 782599935979290655:
            if payload.emoji.name == 'RoflanDota2':
                category = discord.utils.get(guild.categories, name='😡Dota 2')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log]{member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanCsGo':
                category = discord.utils.get(guild.categories, name='💣🔫CS GO')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log] {member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanAmongUs':
                category = discord.utils.get(guild.categories, name='👨🚀Among Us')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log] {member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanGTAV':
                category = discord.utils.get(guild.categories, name='💲GTA V')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log] {member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanSI':
                category = discord.utils.get(guild.categories, name='🏆SiGame')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log] {member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanLeague':
                category = discord.utils.get(guild.categories, name='🚗Rocket League')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log]{member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanDS':
                category = discord.utils.get(guild.categories, name='💀Dark Souls')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log]{member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanGenshi':
                category = discord.utils.get(guild.categories, name='🎆Genshin Impact')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                print(f'[log]{member.name} добавлен в {category}')
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
            elif payload.emoji.name == 'RoflanMinecraft':
                category = discord.utils.get(guild.categories, name='🍎Minecraft')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log]{member.name} добавлен в {category}')
            elif payload.emoji.name == 'RoflanTerraria':
                category = discord.utils.get(guild.categories, name='🌳Terraria')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=overwrite)
                await member.send(f'Поздравляю! Теперь у тебя есть доступ в ``{category}``', delete_after = 60)
                print(f'[log]{member.name} добавлен в {category}')


    #Удалить роль
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        if message_id == 782599935979290655:
            if payload.emoji.name == 'RoflanDota2':
                category = discord.utils.get(guild.categories, name='😡Dota 2')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log]{member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanCsGo':
                category = discord.utils.get(guild.categories, name='💣🔫CS GO')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log] {member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanAmongUs':
                category = discord.utils.get(guild.categories, name='👨🚀Among Us')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log] {member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanGTAV':
                category = discord.utils.get(guild.categories, name='💲GTA V')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log] {member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanSI':
                category = discord.utils.get(guild.categories, name='🏆SiGame')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log] {member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanLeague':
                category = discord.utils.get(guild.categories, name='🚗Rocket League')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log]{member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanDS':
                category = discord.utils.get(guild.categories, name='💀Dark Souls')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log]{member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanGenshi':
                category = discord.utils.get(guild.categories, name='🎆Genshin Impact')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log]{member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanMinecraft':
                category = discord.utils.get(guild.categories, name='🍎Minecraft')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log]{member.name} убран из {category}')
            elif payload.emoji.name == 'RoflanTerraria':
                category = discord.utils.get(guild.categories, name='🌳Terraria')
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await category.set_permissions(member, overwrite=None)
                print(f'[log]{member.name} убран из {category}')


def setup(client):
    client.add_cog(rr(client))