import  discord
from discord.ext import commands

config = {
    'token': 'MTA3MTMyODk1ODY0NzM4NjEyNA.GGATvM.J9O028MYOElhKRlM7wF0XYH6sGv8BzILCvDwp8',
    'prefix': '!',

}
intents = discord.Intents.all()
intents.message_content = True
bot = discord.Client(intents=intents)

bot =  commands.Bot(command_prefix=config['prefix'] ,intents=intents)

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'hello {author.mention}!')
import random
@bot.command()
async def rand(ctx, *arg):
    author = ctx.message.author
    await ctx.reply(random.randint(0,1000000000000000000000000000000000))
@bot.command()
async def kilka(ctx, *arg):
    await ctx.reply('https://minecraft.fandom.com/ru/wiki/%D0%97%D0%B0%D0%B1%D0%BE%D1%80')
    await ctx.reply('https://minecraft.fandom.com/ru/wiki/%D0%97%D0%B5%D0%BB%D1%8C%D0%B5%D0%B2%D0%B0%D1%80%D0%B5%D0%BD%D0%B8%D0%B5')
    await ctx.reply('https://minecraft.fandom.com/ru/wiki/%D0%A2%D0%BE%D1%80%D0%B3%D0%BE%D0%B2%D0%BB%D1%8F?file=%25D0%25A2%25D0%25BE%25D1%2580%25D0%25B3%25D0%25BE%25D0%25B2%25D0%25BB%25D1%258F_%25D0%25B2_1.14-.png#%D0%9A%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84')
    await ctx.reply('https://minecraft.fandom.com/ru/wiki/%D0%A2%D0%BE%D1%80%D0%B3%D0%BE%D0%B2%D0%BB%D1%8F?file=%25D0%2593%25D0%25B0%25D0%25B9%25D0%25B4_%25D0%25BF%25D0%25BE_%25D1%2582%25D0%25BE%25D1%2580%25D0%25B3%25D0%25BE%25D0%25B2%25D0%25BB%25D0%25B5_%25D0%25B8_%25D1%2582%25D0%25BE%25D0%25B2%25D0%25B0%25D1%2580%25D0%25BE%25D0%25BE%25D0%25B1%25D0%25BC%25D0%25B5%25D0%25BD%25D1%2583_%25D0%25B2_Minecraft_Java_Edition_1.17%252B.png#%D0%9A%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84')
    await ctx.reply('https://minecraft-max.ru/kak-sdelat/oborudovanie/1802-stol-kartografa/#CRAFT')
    await ctx.reply('https://minecraftium.ru/karta/')



bot.run(config['token'])