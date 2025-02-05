import os

import discord
import psycopg2
from discord.ext import commands

DATABASE_URL = os.environ['DATABASE_URL']
TOKEN = os.environ['TOKEN']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
client = commands.Bot(command_prefix="!",
                      intents=discord.Intents(messages=True, guild_messages=True, members=True, guilds=True,
                                              reactions=True, voice_states=True, invites=True))
client.remove_command('help')


@client.event
async def on_ready():
    # cursor.execute("DROP TABLE users1")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
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
            achivements int
    ); """)
    for guild in client.guilds:
        for member in guild.members:
            cursor.execute(f"SELECT * FROM users WHERE id = {member.id}")
            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO users "
                    "(name, id, balance, xp, lvl, messages, warns, voice_minutes, invites, duel_wins, duel_loses, "
                    "music_tracks, slots_wins, crime_win, crime_lose, nvuti_wins, coinflip_wins, achivements) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    " ON CONFLICT DO NOTHING",
                    (member.name, member.id, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
                conn.commit()
            else:
                pass

    conn.commit()
    print('Bot connected!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('жизнь'))


@client.event
async def on_member_join(member):
    cursor.execute(f"SELECT id FROM users1 WHERE id = {member.id}")
    a = cursor.fetchone()[0]
    if a is None:
        for guild in client.guilds:
            cursor.execute(
                f"INSERT INTO users "
                f"(name, id, balance, xp, lvl, messages, warns, voice_minutes, invites, duel_wins, duel_loses, "
                f"music_tracks, slots_wins, crime_win, crime_lose, nvuti_wins, coinflip_wins, achivements) "
                f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (member.name, member.id, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            conn.commit()
    else:
        pass


@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.UserInputError):
        await ctx.send(embed=discord.Embed(
            description=f"Правильное использование команды: `{ctx.prefix}{ctx.command.usage}`"
        ), delete_after=10)


@client.command()
async def reload(ctx, extensions):
    await ctx.message.delete()
    if ctx.author.id == 312795489743405058:
        client.unload_extension(f'cogs.{extensions}')
        client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(title=f":white_check_mark: Reload", description=f"\n__{extensions}__ **reloaded!**",
                              color=0x00ff1e)
        await ctx.send(embed=embed, delete_after=3)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
# conn.close()
client.run(TOKEN)
