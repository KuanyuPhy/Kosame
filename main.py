import discord
import dotenv
import os


dotenv.load_dotenv()

token = str(os.getenv("DISCORD_TOKEN"))
bot = discord.Bot(intents=discord.Intents.all(),)


@bot.event
async def on_ready():
    # print(f'We have logged in as {bot.user}')
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  
    print(message.author,": ", message.content)


if __name__ == '__main__': 
    # import cogs from cogs folder
    for filename in os.listdir("function"):
        if filename.endswith(".py"):
            extension = f"function.{filename[:-3]}"
            bot.load_extension(extension)

bot.run(token)