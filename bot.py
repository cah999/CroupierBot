import discord
import os
from discord.ext import commands
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
cursor = conn.cursor()
client = commands.Bot(command_prefix="!", intents = discord.Intents(messages = True, guild_messages = True, members = True, guilds = True, reactions = True, voice_states = True, invites = True))
client.remove_command('help')



@client.event
async def on_ready():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users1 (
        name text,
        id bigint PRIMARY KEY,
	    balance bigint,
	    xp int,
	    lvl	int NOT NULL,
        messages int,
        warns int,
        voice_minutes int,
        invites int,
        duel_wins int,
        duel_loses int,
        music_tracks int,
        slots_wins int,
        crime_win int,
        crime_lose int,
        nvuti_wins int,
        coinflip_wins int,
        achivements int,
        server_id int
    ); """)
    for guild in client.guilds:
        for member in guild.members:
            cursor.execute(f"SELECT * FROM users WHERE id = {member.id}")
            if cursor.fetchone() is None:
                # cursor.execute("INSERT INTO users1 (name, id, balance, xp, lvl, messages, warns, voice_minutes, invites, duel_wins, duel_loses, music_tracks, slots_wins, crime_win, crime_lose, nvuti_wins, coinflip_wins, achivements, server_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (member.name, member.id, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, guild.id))
                cursor.execute("INSERT INTO users1 (name, id, balance, xp, lvl, messages, warns, voice_minutes, invites, duel_wins, duel_loses, music_tracks, slots_wins, crime_win, crime_lose, nvuti_wins, coinflip_wins, achivements) SELECT (name, id, balance, xp, lvl, messages, warns, voice_minutes, invites, duel_wins, duel_loses, music_tracks, slots_wins, crime_win, crime_lose, nvuti_wins, coinflip_wins, achivements) FROM users")
                conn.commit()
            else:
                pass

    # cursor.execute("""DELETE FROM users a USING (
    #     SELECT MIN(ctid) as ctid, id
    #         FROM users 
    #         GROUP BY id HAVING COUNT(*) > 1
    #     ) b
    #     WHERE a.id = b.id 
    #     AND a.ctid <> b.ctid
    #     """)
    conn.commit()
    print('Bot connected!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('жизнь'))


#status
@client.command()
@commands.has_permissions(administrator=True)
async def status(ctx, type=None, *, text=None):
    await ctx.message.delete()
    if type is None:
        await ctx.send(embed = discord.Embed(description=f'**{ctx.author.name}**, укажите тип изменения статуса'), delete_after = 7)
    elif (type == 'play') or (type == 'Play'):
        if text is None:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, укажите текст статуса'), delete_after = 7)
        else:
            embed=discord.Embed(title='Статус бота изменен!',color=0x37393F, description='Бот теперь играет в ' + text )
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name=text))
            await ctx.send(embed=embed, delete_after = 5)
            await ctx.message.delete()
    elif (type == 'listen') or (type == 'Listen'):
        if text is None:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, укажите текст статуса'), delete_after = 7)
        else:
            embed=discord.Embed(title='Статус бота изменен!',color=0x37393F, description='Бот теперь слушает ' + text )
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
            await ctx.send(embed=embed, delete_after = 5)
            await ctx.message.delete()
    elif (type == 'watch') or (type == 'Watch'):
        if text is None:
            await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}**, укажите текст статуса'), delete_after = 7)
        else:
            embed=discord.Embed(title='Статус бота изменен!',color=0x37393F, description='Бот теперь смотрит ' + text )
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
            await ctx.send(embed=embed, delete_after = 5)
            await ctx.message.delete()


@client.command()
async def ping(ctx):
    cursor.execute("SELECT balance FROM users WHERE id = {}".format(ctx.author.id))
    await ctx.send('Pong! Your server id is **{cursor.fetchone()[0]}**')

@client.event
async def on_member_join(member):
    cursor.execute(f"SELECT id FROM users WHERE id = {member.id}")
    a = cursor.fetchone()[0]
    if a is None:
        for guild in client.guilds:
            cursor.execute(f"INSERT INTO users (name, id, balance, xp, lvl, messages, warns, voice_minutes, invites, duel_wins, duel_loses, music_tracks, slots_wins, crime_win, crime_lose, nvuti_wins, coinflip_wins, achivements, server_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (member.name, member.id, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, guild.id))
            conn.commit()
    else:
        pass

@client.event
async def on_command_error(error):
	print(error)
    #
	# if isinstance(error, commands.UserInputError):
	# 	await ctx.send(embed = discord.Embed(
	# 		description = f"Правильное использование команды: `{ctx.prefix}{ctx.command.usage}`"
	# 	), delete_after = 10)


@client.command()
async def reload(ctx, extensions):
    await ctx.message.delete()
    if ctx.author.id == 312795489743405058:
        client.unload_extension(f'cogs.{extensions}')
        client.load_extension(f'cogs.{extensions}')
        embed=discord.Embed(title=f":white_check_mark: Reload", description=f"\n__{extensions}__ **reloaded!**", color=0x00ff1e)
        await ctx.send(embed=embed, delete_after=3)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
# conn.close()
client.run('NzU1MDIzNTcwMzU4MzcwMzA1.X19Qfg.XVFpGANs1YSKh4LCrNQhX27fHVw')