# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if str(message.author) == "Usmanifarooqi#7892":
    quotes = [
                  "Hey usman, your mom is gay",
                  "Shut up usman",
                  "God damn it, it's a rat -_-",
                  "you are literally a waste of space",
                  "your dad is gay for your mom",
                  "ya know, sometimes i wonder how someone so brown can be so dumb",
                  "you know you will never be as good as zain",
                  "sorry, why are you speaking?",
                  "can you please like not do that?",
                  "I wish i had a body so i could end you and your family"
                    ]
    # if str(message.author) == "Yoh#9096":
    #     usmanResponses = [
    #               "Hey usman, your mom is gay",
    #               "Shut up usman",
    #               "God damn it, it's a rat -_-",
    #               "you are literally a waste of space",
    #               "your dad is gay for your mom",
    #               "ya know, sometimes i wonder how someone so brown can be so dumb",
    #               "you know you will never be as good as zain",
    #               "sorry, why are you speaking?",
    #               "can you please like not do that?",
    #               "I wish i had a body so i could end you and your family"
    #                 ]
    #     response = random.choice(usmanResponses)
    #     await message.channel.send(response)

    # quotes = ["Hey usman, your mom is gay", "hey zain, you lookin cute ;)"]

    if message.content == '!speak':
        response = random.choice(quotes)
        await message.channel.send('<:rolf:662675730324520982>')

# @client.command(pass_context = True)
# async def clear(ctx, amount = 100):



client.run(token)