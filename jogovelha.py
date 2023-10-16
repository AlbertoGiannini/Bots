import discord
from discord.ext.commands import bot
from discord.ext import commands
from random import randint
from discord import FFmpegPCMAudio
import time

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
intents.voice_states = True
 
bot = commands.Bot(command_prefix='?', intents=intents)

client = discord.Client(intents=intents)

@bot.command()
async def jogovelha(ctx):
  #try:
  channel = await ctx.guild.create_text_channel('jogo-velha')
  #except:
    #await ctx.send('{} Oops! Estou sem as permissões do servidor!'.format(ctx.author.mention))
    
  await channel.send('{} Digite ?join para entrar. É preciso de 2 jogadores para iniciar'.format(ctx.author.mention))
  players = []
  @bot.command()
  async def join(ctx):
    if ctx.channel.name != channel.name:
      await ctx.send('Oops! Chat errado')
    elif len(players) == 2:
      await ctx.send('Já existem 2 jogadores')
    else:
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

        print(players)
  @bot.command()
  async def play(ctx):
    if ctx.channel.name != channel.name:
      await ctx.send('Oops! Chat errado')
    elif len(players) < 2:
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

            if msg.author.id == players[0] or msg.author.id == players[1]:
              nonlocal win
              while msg != 'sair' or win == 9:
                try:
                  num = int(msg.content) -1
                except:
                  await ctx.send('Digite um número entre 1 e 9!')
                  await jogo(ctx)

                if num > 9 or num < 0:
                  await ctx.send('Digite um número entre 1 e 9!')
                
                elif msg.author.id == players[0] or msg.author.id == players[1]:
                  jogada = '' 
                  if msg.author.id == players[0]:
                    jogada = 'X'
                  else:
                    jogada = 'O'

                  if matriz[num] != '-':

                    await ctx.send('{} Posição ocupada!'.format(ctx.author.mention)) 
                  
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
                      elif matriz[2] == t and  matriz[4] == t and matriz[6]  == t:
                        await ctx.send('{} Venceu!'.format(player.mention))
                        exit()    
                      elif win == 8:
                        await ctx.send('Deu velha!')
                        exit() 
                    
                    if win >= 4:
                      await testvencedor(ctx, matriz[num])      
                    win = win + 1  
                else:
                  await ctx.send('{} Você não está jogando'.format(msg.author.mention))
                  await tabela(ctx)       

                msg = await bot.wait_for('message', check=lambda message: message.channel == ctx.channel)
                print('WIN:', win)
          await jogo(ctx)
          await channel.delete()


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)

bot.run('TOKEN')
