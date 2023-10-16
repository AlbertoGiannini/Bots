import discord
from discord.ext import commands
from discord.ext.commands import bot
import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='?', intents=intents)
players = []
@bot.command()
async def jogovelha(ctx):
  channel = await ctx.guild.create_text_channel('jogo-velha')  
  await channel.send('{} Digite ?join para entrar. É preciso de 2 jogadores para iniciar'.format(ctx.author.mention))
  




@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)

bot.run('MTAwNzI5NTM5MDM4ODg1NDk4Ng.Gy-ju4.9boMVgOTnU72Ix7hiZI52iWPYxyDgflXt36e7M')