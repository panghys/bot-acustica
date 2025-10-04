import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import subir_audios
from discord import Member
from gtts import gTTS


#$

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content = True # info de los mensajes
intents.members = True # info de los usuarios

bot = commands.Bot(command_prefix='!', intents = intents)

voces = ["en", "es", "ja", "fr", "de", "zh-CN", "pt", "ru", "it", "ko"]




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
async def generartts(ctx,*,texto):
    await ctx.send("preparando tts..")
    if ctx.author == bot.user:
        return
    if len(texto) > 300:
        await ctx.send(f"{ctx.author}, tu texto supera los 300, inténtalo denuevo.")
        return
    idioma = texto.split("#")
    if len(idioma) == 2:
        if idioma[1] in voces:
            lang = idioma[1]
        else:
            lang = "es"
    else:
        lang = "es"
    archivo = os.path.join("temp_tts", f"tts_{ctx.author}_{idioma[0]}_{idioma[1]}.mp3")
    if(archivo):
        tts = gTTS(text = idioma[0], lang=lang)
        tts.save(archivo)
        await ctx.send(file=discord.File(archivo))
        os.remove(archivo)
    else:
        await ctx.send("error")
        return
    

@bot.command()
async def entrar(ctx):
    canal = ctx.author.voice.channel
    if canal:
        await canal.connect()
    else:
        await ctx.send(f"no voice xd")
        return

@bot.command()
async def salir(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        return
    
@bot.command()
async def h(ctx,*,texto):
    if ctx.voice_client:
            if ctx.voice_client.is_playing() == False:
                if ctx.author == bot.user:
                    return
                if len(texto) > 300:
                    await ctx.send(f"{ctx.author}, tu texto supera los 300, inténtalo denuevo.")
                    return
                def borrar(a):
                    os.remove(archivo)
                archivo = os.path.join("temp_tts", f"tts.mp3")
                if(archivo):
                    tts = gTTS(text = texto, lang="es")
                    tts.save(archivo)
                    ctx.voice_client.play(
                        discord.FFmpegPCMAudio(source=archivo),
                        after=borrar)
            else: return
    else:
        await ctx.invoke(bot.get_command("entrar"))


@bot.command()
async def status(ctx):
    if ctx.author==bot.user:
        return
    await ctx.send(f"sigue andando el bot -> {ctx.author}")



bot.run(token, log_handler=handler,log_level=logging.DEBUG)