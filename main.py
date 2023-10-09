import discord
from discord_bot import get_response

if __name__ == '__main__':
    with open('tokens/discord_token.txt', 'r') as f:
        discord_token = f.read()


    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        try:
            if message.author == client.user:
                pass
            
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print(f'{username} said: "{user_message}" ({channel})') 

            if user_message[0] == '/':
                user_message = user_message[1:]
                bot_response = get_response(user_message)
                print(bot_response)
                # await send_messages(message, bot_response, embed_list)
            
        except TypeError as e:
            print(e)

    client.run(discord_token)
