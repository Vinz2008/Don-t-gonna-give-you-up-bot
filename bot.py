import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_bot1 = "We're no strangers to love"
    message_bot2 = "You know the rules and so do I"
    message_bot3 = "A full commitment's what I'm thinking of"
    message_bot4 = "You wouldn't get this from any other guy"
    message_bot5 = "I just wanna tell you how I'm feeling"
    message_bot6 = "Gotta make you understand"
    message_bot7 = "Never gonna give you up"
    message_bot8 = "Never gonna let you down"
    message_bot9 = "Never gonna run around and desert you"
    message_bot10 = "Never gonna make you cry"
    message_bot11 = "Never gonna say goodbye"
    message_bot12 = "Never gonna tell a lie and hurt you"
    message_bot13 = "We've known each other for so long"
    message_bot14 = "Your heart's been aching, but"
    message_bot15 = "You're too shy to say it"
    message_bot16 = "Inside, we both know what's been going on"
    message_bot17 = "We know the game and we're gonna play it"
    message_bot18 = "And if you ask me how I'm feeling"
    message_bot19 = "Don't tell me you're too blind to see"
    message_bot20 = "Never gonna give you up"
    message_bot21 = "Never gonna let you down"
    message_bot22 = "Never gonna run around and desert you"
    message_bot23 = "Never gonna make you cry"
    message_bot24 = "Never gonna say goodbye"
    message_bot25 = "Never gonna tell a lie and hurt you"
    message_bot26 = "Never gonna give you up"
    message_bot27 = "Never gonna let you down"
    message_bot28 = "Never gonna run around and desert you"
    message_bot29 = "Never gonna make you cry"
    message_bot30 = "Never gonna say goodbye"
    message_bot31 = "Never gonna tell a lie and hurt you"
    message_bot32 = "(Ooh, give you up)"
    message_bot33 = "(Ooh, give you up)"
    message_bot34 = "Never gonna give, never gonna give"
    message_bot35 = "(Give you up)"
    message_bot36 = "Never gonna give, never gonna give"
    message_bot37 = "(Give you up)"
    message_bot38 = "We've known each other for so long"
    message_bot39 = "Your heart's been aching, but"
    message_bot40 = "You're too shy to say it"
    message_bot41 = "Inside, we both know what's been going on"
    message_bot42 = "We know the game and we're gonna play it"
    message_bot43 = "I just wanna tell you how I'm feeling"
    message_bot44 = "Gotta make you understand"
    message_bot45 = "Never gonna give you up"
    message_bot46 = "Never gonna let you down"
    message_bot47 = "Never gonna run around and desert you"
    message_bot48 = "Never gonna make you cry"
    message_bot49 = "Never gonna say goodbye"
    message_bot50 = "Never gonna tell a lie and hurt you"
    message_bot51 = "Never gonna give you up"
    message_bot52 = "Never gonna let you down"
    message_bot53 = "Never gonna run around and desert you"
    message_bot54 = "Never gonna make you cry"
    message_bot55 = "Never gonna say goodbye"
    message_bot56 = "Never gonna tell a lie and hurt you"
    message_bot57 = "Never gonna give you up"
    message_bot58 = "Never gonna let you down"
    message_bot59 = "Never gonna run around and desert you"
    message_bot60 = "Never gonna make you cry"
    message_bot61 = "Never gonna say goodbye"
    message_bot62 = "Never gonna tell a lie and hurt you"
    if message.content == '!dggyu':
        await message.channel.send(message_bot1)
        await message.channel.send(message_bot2)
        await message.channel.send(message_bot3)
        await message.channel.send(message_bot4)
        await message.channel.send(message_bot5)
        await message.channel.send(message_bot6)
        await message.channel.send(message_bot7)
        await message.channel.send(message_bot8)
        await message.channel.send(message_bot9)
        await message.channel.send(message_bot10)
        await message.channel.send(message_bot11)
        await message.channel.send(message_bot12)
        await message.channel.send(message_bot13)
        await message.channel.send(message_bot14)
        await message.channel.send(message_bot15)
        await message.channel.send(message_bot16)
        await message.channel.send(message_bot17)
        await message.channel.send(message_bot18)
        await message.channel.send(message_bot19)
        await message.channel.send(message_bot20)
        await message.channel.send(message_bot21)
        await message.channel.send(message_bot22)
        await message.channel.send(message_bot23)
        await message.channel.send(message_bot24)
        await message.channel.send(message_bot25)
        await message.channel.send(message_bot26)
        await message.channel.send(message_bot27)
        await message.channel.send(message_bot28)
        await message.channel.send(message_bot29)
        await message.channel.send(message_bot30)
        await message.channel.send(message_bot31)
        await message.channel.send(message_bot32)
        await message.channel.send(message_bot33)
        await message.channel.send(message_bot34)
        await message.channel.send(message_bot35)
        await message.channel.send(message_bot36)
        await message.channel.send(message_bot37)
        await message.channel.send(message_bot38)
        await message.channel.send(message_bot39)
        await message.channel.send(message_bot40)
        await message.channel.send(message_bot41)
        await message.channel.send(message_bot42)
        await message.channel.send(message_bot43)
        await message.channel.send(message_bot44)
        await message.channel.send(message_bot45)
        await message.channel.send(message_bot46)
        await message.channel.send(message_bot47)
        await message.channel.send(message_bot48)
        await message.channel.send(message_bot49)
        await message.channel.send(message_bot50)
        await message.channel.send(message_bot51)
        await message.channel.send(message_bot52)
        await message.channel.send(message_bot53)
        await message.channel.send(message_bot54)
        await message.channel.send(message_bot55)
        await message.channel.send(message_bot56)
        await message.channel.send(message_bot57)
        await message.channel.send(message_bot58)
        await message.channel.send(message_bot59)
        await message.channel.send(message_bot60)
        await message.channel.send(message_bot61)
        await message.channel.send(message_bot62)
client.run(TOKEN)
