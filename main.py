import discord
import dotenv
import os


dotenv.load_dotenv()

token = str(os.getenv("DISCORD_TOKEN"))
bot = discord.Bot(intents=discord.Intents.all(),)

if __name__ == '__main__': 
    # import cogs from cogs folder
    for filename in os.listdir("function"):
        if filename.endswith(".py"):
            extension = f"function.{filename[:-3]}"
            bot.load_extension(extension)

bot.run(token)