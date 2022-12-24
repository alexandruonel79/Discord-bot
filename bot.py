import discord
import responses


# Send messages
async def send_message(message, user_message):
    try:
        response = await responses.handle_response(message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA1NTg4NzQ5OTcyNzIyNDg3Mg.GUUs3C.v5sEwTC4GMWoim7aiC2tu0-UbMeUneOwkt8haY'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
     
        await send_message(message, user_message)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)