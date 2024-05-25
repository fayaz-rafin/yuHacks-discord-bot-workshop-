import discord
from discord.ext import commands
import requests
import json
import os
from discord import embeds

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
  print("Hello World!! I'm alive!")

@client.command()
async def hello(message):
  await message.channel.send("Hello!")

@client.command()
async def info(ctx,message):
  pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{message}" 
  data = requests.get(pokemon_url).json()
  name = data['species']['name'].capitalize()
  poketype = data['types'][0]['type']['name'].capitalize()
  image = data['sprites']['front_default']

  #description of pokemon
  description = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{message}").json()
  entry = description['flavor_text_entries'][0]['flavor_text']

  #embed message
  result = discord.Embed(title = name, description=entry)
  result.add_field(name="Type: ", value = poketype, inline=False)
  result.set_image(url=image)
  await ctx.send(embed=result)
  



client.run(os.getenv('TOKEN'))
