import discord
import os
from dotenv import load_dotenv

# Вчитување на околинските променливи од `.env` датотека
load_dotenv()

# Извлекување на токенот на ботот од околинската променлива "TOKEN"
token = os.environ["TOKEN"]

# Иницијализација на намерите (intents) за ботот
intents = discord.Intents.default()
intents.message_content = True  # Дозволува ботот да ја чита содржината на пораките

# Креирање нов клиент (бот) со зададените намери
client = discord.Client(intents=intents)

# Оваа функција се повикува кога ботот успешно ќе се логиран
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")  # Испишува порака дека ботот е логиран

# Оваа функција се извршува секогаш кога ботот ќе добие порака
@client.event
async def on_message(message):
    # Проверува дали пораката е испратена од самиот бот и ако е, се враќа
    if message.author == client.user:
        return

    # Проверува дали пораката започнува со "!poll" за да креира анкета
    if message.content.startswith("!poll"):
        # Го зема прашањето од пораката
        question = message.content[len("!poll "):].strip()
        if question:
            # Испраќа порака со прашањето и додава реакции за гласови
            poll_message = await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction('👍')
            await poll_message.add_reaction('👎')
        else:
            # Испраќа порака ако нема прашање
            await message.channel.send("Nemas napisano prasanje")

    # Проверува дали пораката содржи "LOL" за да го кикне корисникот
    if "LOL" in message.content:
        await message.channel.send("Ne smees da kazes LOL")
        await message.author.kick(reason="Kaza LOL")

    # Ако пораката е "ping", ботот одговара со "pong"
    if message.content == "ping":
        await message.channel.send("pong")

# Го стартува ботот со токенот кој е вчитан претходно
client.run(token)
