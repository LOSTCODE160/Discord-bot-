import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import random
import os
import re
import httpx
import asyncio
from discord import app_commands

# Load .env
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

# --- OpenRouter AI Chat ---
def query_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPEN_ROUTER_KEY')}",
        "HTTP-Referer": "https://github.com/LOSTCODE160",
        "X-Title": "Discord Bot LLM Chat"
    }

    payload = {
        "model": "google/gemma-3n-e4b-it:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=60)
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- Weather Fetch ---
def get_weather(city):
    api_key = os.getenv("OPEN_WEATHER_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = httpx.get(url, timeout=10)
        data = response.json()

        if data.get("cod") != 200:
            return f"❌ Could not find weather for **{city}**."

        weather_data = data.get("weather", [{}])[0]
        main_data = data.get("main", {})
        wind_data = data.get("wind", {})

        weather = weather_data.get("description", "N/A").capitalize()
        temp = main_data.get("temp", "N/A")
        feels_like = main_data.get("feels_like", "N/A")
        humidity = main_data.get("humidity", "N/A")
        wind = wind_data.get("speed", "N/A")

        return (
            f"**🌤 Weather in {city.title()}**\n"
            f"🌡 Temp: {temp}°C (feels like {feels_like}°C)\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind} m/s\n"
            f"📖 Condition: {weather}"
        )
    except Exception as e:
        return f"❌ Error fetching weather: {str(e)}"

    # IMAGE

async def generate_image(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {os.getenv('REPLICATE_API_TOKEN')}",
        "Content-Type": "application/json"
    }

    payload = {
        "version": "jpwzq056hd9rmc0cq2vh87m2jzw",  
        "input": {
            "prompt": prompt
            
        }
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            print("Status:", response.status_code)
            print("Response:", response.text)
            response.raise_for_status()
            prediction = response.json()
            return prediction['urls']['get']
        except Exception as e:
            return f"❌ Error: {str(e)}"

# --- Ready Event ---
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Sync failed: {e}")

# --- On Member Join ---
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

# --- Moderation: Delete Banned Words ---
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    banned_words = [
        "shit", "fuck", "fucku", "fuck you", "fuckyou", "bitch", "bkl", "bc", "mc", "chutiya",
        "gandu", "madarchod", "behenchod", "loda", "lund", "bsdk", "chu", "suar", "kutte", "gaand",
        "haraami", "harami", "randi", "chodu", "gand", "jhatu", "jhant", "gaandfat", "chut", "gandmasti",
        "madharchod", "tatti", "gandhi", "kutta", "ghanta", "fattu", "gaand mara", "ma chod", "behn chod",
        "terima", "teri maa", "teri behen", "bhosdi", "bhosdike", "nalayak", "bhadwe", "bhosdiwale", "mkc"
    ]

    pattern = r'\b(' + '|'.join(re.escape(word) for word in banned_words) + r')\b'

    if re.search(pattern, message.content.lower()):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, please avoid using bad language!")

    await bot.process_commands(message)

# --- Greetings Command ---
greetings_list = [
    "Hello", "Hey", "Hi there", "What's up", "Yo", "Howdy", "Hola", "Namaste", "Greetings",
    "Good to see you", "Hey there", "Hi buddy", "Welcome", "Wassup", "How’s it going",
    "Salutations", "Peace", "Bonjour", "Hola amigo", "Konnichiwa", "Oi", "Sup", "Heyy",
    "Hello there", "Hi hi", "Yo yo", "Hiiiii", "Namaskar", "Ram Ram", "Sat Sri Akal", "Adaab", "hii"
]

@bot.command(name="hello")
async def say_hello(ctx):
    greeting = random.choice(greetings_list)
    await ctx.send(f"{greeting} {ctx.author.mention} 😁!")

# --- Assign Role Command ---
BOT_ROLE_NAME = "test-bot-role"

@bot.command(name="assign")
async def assign_role(ctx):
    role = discord.utils.get(ctx.guild.roles, name=BOT_ROLE_NAME)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} has been assigned the role `{BOT_ROLE_NAME}` 😁!")
    else:
        await ctx.send("⚠️ The specified role does not exist.")

# --- Slash Command: Ask LLM ---
@bot.tree.command(name="ask", description="Ask OpenRouter AI a question")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    answer = query_openrouter(question)
    chunks = [answer[i:i+2000] for i in range(0, len(answer), 2000)]
    for chunk in chunks:
        await interaction.followup.send(chunk)

# --- Slash Command: Weather ---
@bot.tree.command(name="weather", description="Get current weather for a city")
async def weather(interaction: discord.Interaction, city: str):
    await interaction.response.defer()
    report = get_weather(city)
    await interaction.followup.send(report)

# --- Slash Command: Image Generation ---
@bot.tree.command(name="image", description="Generate an AI image with a prompt")
@app_commands.describe(prompt="What image do you want?")
async def image(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    polling_url = await generate_image(prompt)

    if polling_url.startswith("❌"):
        await interaction.followup.send(polling_url)
        return

    await interaction.followup.send(f"🖼 Image is generating! Check status here:\n{polling_url}")

    try:
        for _ in range(10):
            async with httpx.AsyncClient() as client:
                poll = await client.get(polling_url, headers={"Authorization": f"Token {os.getenv('REPLICATE_API_TOKEN')}"})
                status = poll.json()
                if status["status"] == "succeeded":
                    image_url = status["output"][0]
                    await interaction.followup.send(image_url)
                    return
                elif status["status"] == "failed":
                    await interaction.followup.send("❌ Generation failed.")
                    return
            await asyncio.sleep(5)
    except Exception as e:
        await interaction.followup.send(f"❌ Polling error: {str(e)}")

# --- Run Bot ---
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
