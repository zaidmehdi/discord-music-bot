import discord
from yt_dlp import YoutubeDL
import asyncio

if __name__ == '__main__':
    with open('tokens/discord_token.txt', 'r') as f:
        discord_token = f.read()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    voice_clients = {}

    yt_dl_opts = {'format': 'bestaudio/best'}
    ytdl = YoutubeDL(yt_dl_opts)

    ffmpeg_options = {'options': '-vn'}

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(msg):
        if msg.content.startswith('/play'):
            try:
                voice_client = await msg.author.voice.channel.connect()
                voice_clients[voice_client.guild.id] = voice_client
            except Exception as e:
                print(e)

            try:
                url = msg.content.split()[1]

                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

                song = data['url']
                player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

                voice_clients[msg.guild.id].play(player)
                 
            except Exception as e:
                print(e)


        if msg.content.startswith('/pause'):
            try:
                voice_clients[msg.guild.id].pause()
            except Exception as e:
                print(e)


        if msg.content.startswith('/resume'):
            try:
                voice_clients[msg.guild.id].resume()
            except Exception as e:
                print(e)


        if msg.content.startswith('/stop'):
            try:
                voice_clients[msg.guild.id].stop()
                await voice_clients[msg.guild.id].disconnect()
            except Exception as e:
                print(e)

    client.run(discord_token)
