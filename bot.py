import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
from discord import FFmpegPCMAudio
from random import randint

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
intents.voice_states = True
 
bot = commands.Bot(command_prefix='?', intents=intents)

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print('BOT ON!!')
    print(bot.user.name)
    print(bot.user.id)
    print("{} is Ready".format(bot.user))


class Cara(discord.ui.View):
      
  moedacoroa = discord.Embed(title="Caiu Coroa!").set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/R00007A.JPG')
  moedacara = discord.Embed(title="Caiu Cara!").set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/A00007A.JPG')
  
  @discord.ui.button(label='Cara', style=discord.ButtonStyle.green)
  async def cara(self, interaction: discord.Interaction, button: discord.ui.Button):
    #for child in self.children:
    #  child.disabled = True
    if randint(0, 1000) % 2 != 0:
      self.moedacara.description='Você ganhou!'
      await interaction.response.edit_message(embed=self.moedacara, view=self)
    else: 
      self.moedacoroa.description='Você perdeu!'
      await interaction.response.edit_message(embed=self.moedacoroa, view=self)
  @discord.ui.button(label='Coroa', style=discord.ButtonStyle.green)
  async def coroa(self, interaction: discord.Interaction, button: discord.ui.Button):
    #for child in self.children:
    #  child.disabled = True
    if randint(0, 1000) % 2 == 0:
      self.moedacoroa.description='Você ganhou!'
      await interaction.response.edit_message(embed=self.moedacoroa, view=self)
    else: 
      self.moedacara.description='Você perdeu!'
      await interaction.response.edit_message(embed=self.moedacara, view=self)    

@bot.command()
async def coinflip(ctx):
  view = Cara()
  caracoroa = discord.Embed(title='Cara ou Coroa')
  caracoroa.set_image(url='http://lh3.ggpht.com/-6KfOSzwRvkw/T2TD1zZnjnI/AAAAAAAAOVY/7ZJg4qCW0-k/s0/1real.gif')
  message = await ctx.send(embed = caracoroa, view = view)
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
  embed = discord.Embed(title='COMANDOS DO MELHOR BOT DO SERVER', description='?foo \n ------ \n?uga \n ------ \n ?rojao \n ------ \n ?bong \n ------ \n ?coinflip')
  await ctx.send(embed = embed)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)

bot.run('TOKEN')