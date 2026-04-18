
import discord

ALLOWED_GUILD_ID = 1291464820021002380
TOKEN = ""
TARGET_USER_ID = 0

message = "Hi"

intents = discord.Intents.default()
intents.guilds = True
intents.members = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    user = await client.fetch_user(TARGET_USER_ID)
    if message != "":
        try:
            await user.send(message)
            print(f"✅ Sent member list to user {user} {TARGET_USER_ID}")
        except discord.Forbidden:
            print(f" Could not DM the user {user}. Check their privacy settings.")

    @client.event
    async def on_message(message):
        if message.author.id == TARGET_USER_ID:
            print(f"[{message.author}] {message.content}")

client.run(TOKEN)