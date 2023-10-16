import discord
from random import randint

class Flip(discord.ui.View):

  def __init__(self):
    super().__init__()
      
  moedacoroa = discord.Embed(title="Caiu Coroa!").set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/R00007A.JPG')
  moedacara = discord.Embed(title="Caiu Cara!").set_image(url='http://www.moedasdobrasil.com.br/moedas/images/moedas1/A00007A.JPG')
  
  @discord.ui.button(label='Cara', style=discord.ButtonStyle.green)
  async def cara(self, interaction: discord.Interaction, button: discord.ui.Button):
    #disable buttons after click
    #for child in self.children:
    #  child.disabled = True
    if randint(1, 2) % 2 != 0:
      self.moedacara.description='Você ganhou!'
      await interaction.response.edit_message(embed=self.moedacara, view=self)
    else: 
      self.moedacoroa.description='Você perdeu!'
      await interaction.response.edit_message(embed=self.moedacoroa, view=self)
  @discord.ui.button(label='Coroa', style=discord.ButtonStyle.green)
  async def coroa(self, interaction: discord.Interaction, button: discord.ui.Button):
    #disable buttons after click
    #for child in self.children:
    # child.disabled = True
    if randint(1, 2) % 2 == 0:
      self.moedacoroa.description='Você ganhou!'
      await interaction.response.edit_message(embed=self.moedacoroa, view=self)
    else: 
      self.moedacara.description='Você perdeu!'
      await interaction.response.edit_message(embed=self.moedacara, view=self)   
