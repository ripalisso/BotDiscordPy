import discord
from discord.ext import commands
import random
import datetime
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)



client = commands.Bot(command_prefix='>', case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print('BOT ONLINE - EAEEE')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')

@client.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author}')
@client.command()
async def bomdia(ctx):
    await ctx.send(f'Olá {ctx.author}, saia um pouco de casa, está um belo dia lá fora')
@client.command()
async def boanoite(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        description= '',
        color=0xff55ff,
        timestamp=datetime.datetime.now()
    )
    embed.set_image(url="https://media.tenor.com/L9nXR7CZrc4AAAAd/hollow-knight-grimm.gif")
    await channel.send(embed=embed)
@client.command()
async def atumalaca(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        description= '',
        color=0xff55ff,
        timestamp=datetime.datetime.now()
    )
    embed.set_image(url="https://media.tenor.com/0xiAEu8Tj5EAAAAd/don-comedia-te-declaro-don-comedia.gif")
    await channel.send(embed=embed)


regras_id = 725109110466412544

regras_id = 725109110466412544

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Pega o canal de texto padrão do servidor
    if channel is not None:
        embed = discord.Embed(
            description=f'Bem-vindo {member.mention} ao clube ☕ \n'
                        f'Leia as regras em <#{regras_id}> ',
            color=0xff55ff,
        )
        await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    canal_saida = member.guild.get_channel(860695418214940672)
    if canal_saida is not None:
        embed = discord.Embed(
            title="😢 **Até logo!** 😢",
            description=f'{member.name} deixou o clube. Que a força esteja com ele',
            color=0xff55ff,
        )
        await canal_saida.send(embed=embed)

client.run("token")
