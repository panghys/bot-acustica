import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import subir_audios
from discord import Member


#$

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content = True # info de los mensajes
intents.members = True # info de los usuarios

bot = commands.Bot(command_prefix='!', intents = intents)



@bot.event
async def on_ready():
    print("LISTO: BOT EN EJECUCIÓN")

@bot.command()
async def audio(ctx, *, link):
        print("recibido")
        if ctx.author == bot.user:
            return
        print(f"buscando {link}")
        archivo = await subir_audios.subirAudio(link, "audio.mp3")
        if (archivo):
            await ctx.send(file=discord.File(archivo))
            os.remove(archivo)
        else:
            print("fail")
            await ctx.send("error")

@bot.command()
async def status(ctx):
    if ctx.author==bot.user:
        return
    await ctx.send(f"sigue andando el bot")
    await ctx.send(f"request de {ctx.author}")



bot.run(token, log_handler=handler,log_level=logging.DEBUG)