import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import openai

# 1. Load các biến môi trường từ file .env (hoặc từ Render)
load_dotenv()

# 2. Cấu hình kết nối
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

# 3. Cấu hình bot Discord
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập thành công dưới tên {bot.user}')

@bot.command()
async def chat(ctx, *, prompt):
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=[{"role": "user", "content": prompt}]
        )
        await ctx.send(response.choices[0].message.content)
    except Exception as e:
        await ctx.send(f"Có lỗi xảy ra: {e}")

# 4. Chạy bot bằng token từ file .env hoặc từ Render
bot.run(os.environ.get("DISCORD_TOKEN"))