
import discord

TOKEN = "" 
USER_IDS = []

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged In As {client.user} (ID: {client.user.id})')


@client.event
async def on_message(message):
    receiver = client.user if client.user != message.author else None
    print(f"[{message.author}] -> [{receiver}]: {message.content}")

client.run(TOKEN)