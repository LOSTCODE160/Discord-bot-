

---


# 🤖 Discord Bot — Moderation + LLM + Weather Assistant

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenRouter](https://img.shields.io/badge/LLM-OpenRouter-orange)

A multifunctional Discord bot built with `discord.py`.  
Includes moderation, AI assistant (OpenRouter), weather info, and more.

---

## 📸 Screenshots

> Place screenshots inside an `assets/` folder in your repo.

| Slash Commands | LLM Chat | Weather |
|----------------|----------|---------|
| ![Slash Commands](assets/slash-commands.png) | ![LLM Example](![image](https://github.com/user-attachments/assets/d77301a5-cda7-4fe4-8dc4-076edbddc30f)
) | ![Weather Example](![image](https://github.com/user-attachments/assets/b3930c11-58a4-48d4-9cd7-89a2a1724950)
) |

---

## 💡 Features

- 🛡️ **Profanity Filter** — Deletes messages with bad words
- 🤖 **AI Chat** — Uses OpenRouter's free LLMs
- 🌦️ **Weather Info** — Get real-time weather using `/weather [city]`
- 👋 **Greeting** — Sends random welcome messages
- 🎭 **Auto Role Assignment** — With `/assign`
- 📩 **Welcome DMs** — Greets new members privately

---

## 🚀 Setup Guide

### 1. Clone This Repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
````

### 2. Create `.env` File

Add your tokens:

```env
DISCORD_TOKEN=your_discord_bot_token
OPEN_ROUTER_KEY=your_openrouter_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

> You can get free weather API key from [OpenWeather](https://openweathermap.org/api)

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

Tested on ✅ **Python 3.10+**

### 4. Run the Bot

```bash
python bot.py
```

---

## 🧪 Usage Examples

* `/hello` → Sends a friendly greeting
* `/ask Why is the sky blue?` → Ask the LLM anything!
* `/weather Delhi` → Returns current weather for Delhi
* `/assign` → Assigns user a default role

---

## 📁 Project Structure

```
discord-bot/
 ┣ 📂 assets/
 ┃ ┣ slash-commands.png
 ┃ ┣ llm-chat-example.png
 ┃ ┗ weather-example.png
 ┣ bot.py
 ┣ .env
 ┣ requirements.txt
 ┗ README.md
```

---

## 🧾 Sample Requirements.txt

```
discord.py==2.3.2
httpx
python-dotenv
```

---

## 🌐 Add Bot to Server

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. OAuth2 > URL Generator

   * **Scopes**: `bot`, `applications.commands`
   * **Permissions**: `Send Messages`, `Read Message History`, `Manage Roles`
3. Copy the URL → Invite to server

---

## 📜 License

MIT © [LOSTCODE160](https://github.com/LOSTCODE160)

---

## 🙌 Credits

* [discord.py](https://discordpy.readthedocs.io)
* [OpenRouter](https://openrouter.ai)
* [OpenWeather API](https://openweathermap.org)

```

---

If you're **still writing the weather function**, I can provide one that uses OpenWeatherMap API and fits perfectly into your current bot structure.

Would you like me to include the weather command code as well?
```
