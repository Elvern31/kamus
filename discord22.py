import discord
import random
import os
from discord.ext import commands
import asyncio

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variabel token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command("tebak")
async def tebak_sampah(ctx):
    # Memilih jenis-jenis sampah
    kategori = ["organik", "anorganik"]
    jenis_sampah = random.choice(kategori)

    # Memilih gambar secara acak dari folder 'images'
    nama_images = random.choice(os.listdir(f'sampah/{jenis_sampah}'))
    
    # Mengirim gambar kepada pengguna
    with open(f'sampah/{jenis_sampah}/{nama_images}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send("Apa jenis sampah ini?", file=picture)
    
    # Menerima jawaban dari pengguna
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Waktu habis! Jawabannya adalah: " + nama_images)
        return

    # Memeriksa jawaban
    if msg.content.lower() == jenis_sampah.lower():
        await ctx.send("Benar!")
    else:
        await ctx.send(f"Salah! Jawabannya adalah: {jenis_sampah.upper()}")

bot.run(MTM1NzY5ODgzOTYwNzUxMzIxOA.GWA6VK.Gi6i5GiT-tWaJqmkr-OSbC10qXLgBZ-B1aHpLY)
