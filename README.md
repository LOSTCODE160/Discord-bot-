Here's a clean and professional `README.md` for your Discord bot project that includes the LLM (OpenRouter) integration, role assignment, profanity filter, and greeting features:

---

````markdown
# 🤖 Discord Bot — Moderation + LLM Assistant

A powerful, multifunctional Discord bot built using `discord.py`. This bot features:

- ✅ Automatic role assignment  
- 💬 LLM integration (via [OpenRouter](https://openrouter.ai))  
- 🧼 Profanity filtering  
- 👋 Greeting commands  
- 📩 Welcome DMs for new members  

---

## 📦 Features

### 🛡️ Profanity Filter
Deletes messages that contain offensive or banned words and warns the user.

### 🤖 LLM Chat with OpenRouter
Ask intelligent questions using:
```bash
/ask Your question here...
````

Powered by OpenRouter's API — you can choose any supported free model (e.g., Mistral, DeepSeek, Gemma).

### 👋 Greetings

Randomized greetings for users:

```bash
/hello
```

### 🎭 Role Assignment

Assigns a pre-defined role to the user:

```bash
/assign
```

### 👋 Welcome DM

Sends a friendly DM to any user who joins the server.

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create `.env` File

Create a `.env` file with the following keys:

```env
DISCORD_TOKEN=your_discord_bot_token
OPEN_ROUTER_KEY=your_openrouter_api_key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python bot.py
```

---

## 🌐 Add Bot to Your Server

To invite your bot to other servers, use the OAuth2 URL Generator on [Discord Developer Portal](https://discord.com/developers/applications), and select:

* `bot` scope
* `applications.commands`
* Permissions: `Send Messages`, `Manage Roles`, etc.

---

## 📁 Folder Structure

```
📦discord-bot/
 ┣ 📄 bot.py
 ┣ 📄 .env
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 📜 License

MIT © [YourName or LOSTCODE160](https://github.com/LOSTCODE160)

---

## 💡 Credits

* Built with [discord.py](https://discordpy.readthedocs.io)
* LLM powered by [OpenRouter](https://openrouter.ai)

```

---

Let me know if you want to add badges (like Python version, OpenRouter model used, etc.) or screenshots.
```
