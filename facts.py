import random

links = ["The world’s oldest wooden wheel has been around for more than 5,000 years",
        "Sudan has more pyramids than any country in the world",
        "There are parts of Africa in all four hemispheres",
        "German chocolate cake was invented in Texas"]

async def schedule_daily_message(message):
        await message.channel.send(random.choice(links))