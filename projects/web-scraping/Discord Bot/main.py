import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!poll"):
        question = message.content[len("!poll "):].strip()
        if question:
            poll_message = await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction('👍')
            await poll_message.add_reaction('👎')
        else:
            await message.channel.send("Nemas napisano prasanje")

    if "LOL" in message.content:
        await message.channel.send("Ne smees da kazes LOL")
        await message.author.kick(reason="Kaza LOL")

    if message.content == "ping":
        await message.channel.send("pong")
client.run(token)
