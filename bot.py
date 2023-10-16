import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
from discord import FFmpegPCMAudio
from random import randint
from discord.ui import Button

from commandsClasses.coinClass import Flip

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
intents.voice_states = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print('BOT ON!!')
    print(bot.user.name)
    print(bot.user.id)
    print("{} is Ready".format(bot.user))

class JoinPlay(discord.ui.View): 
  global players
  players = []
  @discord.ui.button(label='Join',style=discord.ButtonStyle.green)
  async def join(self, interaction: discord.Interaction, button: discord.ui.Button, custom_id='btnJoin'):
    players.append(self.message.author.id)
    if len(players) != 1:
      self.remove_item(button)
      global play
      play = discord.ui.Button(label='Play',style=discord.ButtonStyle.green, custom_id='btnPlay') 
      self.add_item(play)
      await interaction.response.edit_message(view=self)
      print(self.children)
    try:  
      await interaction.response.edit_message(view=self)
      await self.message.send('{} Entrou!'.format(interaction.user.mention))
    except:
      await self.message.send('{} Entrou!'.format(interaction.user.mention))

   

@bot.command()
async def jogovelha(ctx):
  view = JoinPlay()
  
  message = ctx
  await ctx.send('Aguardando jogadores...',view = view)
  j = len(players)
  for x in players:
    if ctx.author.id == x:
      await ctx.send('{} já deu join!'.format(ctx.author.mention))
      print('J ', j)
      break
    else:
      players.insert(j, ctx.author.id)
      await ctx.send('{} entrou!'.format(ctx.author.mention))
      print(players)
      j += 1
      print('J ', j)
  view.message = message  
  await view.wait()


@bot.command()
async def coinflip(ctx):
  view = Flip()
  embedcaracoroa = discord.Embed(title='Cara ou Coroa')
  embedcaracoroa.set_image(url='http://lh3.ggpht.com/-6KfOSzwRvkw/T2TD1zZnjnI/AAAAAAAAOVY/7ZJg4qCW0-k/s0/1real.gif')
  message = await ctx.send(embed = embedcaracoroa, view = view)
  view.message = message
  await view.wait()


@bot.command(pass_context = True)
async def bong(ctx):
  if ctx.author.voice:
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('0918.mp3')
    voice.play(source)
    await ctx.message.delete()
    while voice.is_playing():
      await asyncio.sleep(1)
    await voice.disconnect()
    
  else:
    await ctx.send('{} você não está em um canal de voz!'.format(ctx.author.mention))


@bot.command(pass_context = True)
async def rojao(ctx):
  if ctx.author.voice:
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('SOM-DO-ROJÃO-APITO-ESTOURADO_-_TubeRipper.com_.wav')
    voice.play(source)
    await ctx.message.delete()
    while voice.is_playing():
      await asyncio.sleep(1)
    await voice.disconnect() 
    
  else:
    await ctx.send('{} você não está em um canal de voz!'.format(ctx.author.mention))

@bot.command()
async def uga(ctx):
  await ctx.send('buga')


@bot.command()
async def comandos(ctx):
  embed = discord.Embed(title='COMANDOS DO MELHOR BOT DO SERVER', description='?uga \n ------ \n ?rojao \n ------ \n ?bong \n ------ \n ?coinflip \n ------ \n ?jogovelha')
  await ctx.send(embed = embed)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)

bot.run('TOKEN')
