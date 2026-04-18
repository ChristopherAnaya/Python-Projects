
import discord

TOKEN = ""
USER_IDS = []

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged In As {client.user} (ID: {client.user.id})')

    while True:
        for index, users in enumerate(USER_IDS):
            print(index+1, await client.fetch_user(users))

        TARGET_USER_ID = USER_IDS[int(input("Wich User Do You Want? "))-1]

        user = await client.fetch_user(TARGET_USER_ID)

        message = input("What Is Your Message? ")

        try:
            await user.send(message)
            print(f"Sent message '{message}' to {user}.")
        except discord.Forbidden:
            print(f"Could Not DM The User {user}. Check Their Privacy Settings.")

        if input("Would You Like To Send Another? Y/N ") == "n":
            break


client.run(TOKEN)