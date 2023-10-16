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
  async def play(ctx):
    if ctx.channel.name != 'jogo-velha':
      await ctx.send('Oops! Chat errado')

    else:
      if len(players) < 2:
        await ctx.send('{} É preciso ter 2 jogadores para iniciar!'.format(ctx.author.mention))
      else: 
        if ctx.author.id !=  players[0] and ctx.author.id != players[1]:
            print('ID ', ctx.author.id)
            await ctx.send('{} não se mete corno'.format(ctx.author.mention))

        else: 
          matriz = []
          j = 0
          while j < 9:
            matriz.append('-')
            j += 1

            async def tabela(ctx):
              p = 0
              mensagem = ''
              while p < 9:
                mensagem += '\n{}   |   {}   |   {}'.format(matriz[p], matriz[p+1], matriz[p+2])
                p += 3
              await ctx.send(mensagem)


          ##message = await client.wait_for('message', check=lambda message: message.author == ctx.author)
          await tabela(ctx)
          win = 0
          async def jogo(ctx):
            msg = await bot.wait_for('message', check=lambda message: message.channel == ctx.channel)

            if msg.author.id != players[0] and msg.author.id != players[1]:
              await ctx.send('{} Você não está jogando'.format(msg.author.mention))
            else:
              nonlocal win
              while msg != 'sair' or win == 9:
              
                try:
                  num = int(msg.content) -1
                except:
                  await ctx.send('{} Digite um número entre 1 e 9!'.format(ctx.author.mention))
                  await jogo(ctx)

                if num > 9 or num < 0:
                  await ctx.send('{} Digite um número entre 1 e 9!'.format(ctx.author.mention))
      
                else:
                  jogada = '' 
                  if msg.author.id == players[0]:
                    jogada = 'X'
                  else:
                    jogada = 'O'
                  
                  if matriz[num] ==  'X' or matriz[num] ==  'O':
                    await ctx.send('{} Posição ocupada!'.format(ctx.author.mention))
                    await tabela(ctx)

                  else:
                    matriz[num] = jogada
                    await tabela(ctx)

                    print(matriz)
                    print(matriz[num])

                    async def testvencedor(ctx, t):
                      line = 0
                      col = 0
                      player = msg.author
                      while line < 9:
                        if matriz[line] == t and  matriz[line+1] == t and matriz[line+2]  == t:
                          await ctx.send('{} Venceu!'.format(player.mention))
                          exit()                    
                        line += 3
                      while col < 3:
                        if matriz[col] == t and  matriz[col+3] == t and matriz[col+6]  == t:
                          await ctx.send('{} Venceu!'.format(player.mention))
                          exit()
                        col += 1
                      if matriz[0] == t and  matriz[4] == t and matriz[8]  == t:
                        await ctx.send('{} Venceu!'.format(player.mention))
                        exit()
                      if matriz[2] == t and  matriz[4] == t and matriz[6]  == t:
                        await ctx.send('{} Venceu!'.format(player.mention))
                        exit()    

                    
                    if win >= 4:
                      await testvencedor(ctx, matriz[num])      
                    win = win + 1         

                msg = await bot.wait_for('message', check=lambda message: message.channel == ctx.channel)
                print('WIN:', win)
          await jogo(ctx)


@bot.command()
async def aa(ctx):
  rand = randint(0, 100)
  embed = discord.Embed(title='CARA OU COROA', description='?cara ou ?coroa')
  embed.set_image(url='http://lh3.ggpht.com/-6KfOSzwRvkw/T2TD1zZnjnI/AAAAAAAAOVY/7ZJg4qCW0-k/s0/1real.gif')
  await ctx.send(embed = embed)

  @bot.command()
  async def cara(ctx):
    rand = randint(0, 100)
    if rand % 2 == 0:
      cara = discord.Embed(title='VOCÊ PERDEU!')
      cara.set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/A00007A.JPG')
      print(rand)
      await ctx.send(embed = cara)
    else:
      coroa = discord.Embed(title='VOCÊ GANHOU!')
      coroa.set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/R00007A.JPG')
      await ctx.send(embed = coroa)

  @bot.command()
  async def coroa(ctx):
    rand = randint(0, 100)
    if rand % 2 != 0:
      coroa = discord.Embed(title='VOCÊ GANHOU!')
      coroa.set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/R00007A.JPG')
      print(rand)
      await ctx.send(embed = coroa)
    else:
      cara = discord.Embed(title='VOCÊ PERDEU!')
      cara.set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/A00007A.JPG')
      await ctx.send(embed = cara)
 

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

bot.run('MTAwNzI5NTM5MDM4ODg1NDk4Ng.Gy-ju4.9boMVgOTnU72Ix7hiZI52iWPYxyDgflXt36e7M')