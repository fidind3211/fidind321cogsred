import discord
import asyncio
import subprocess
from redbot.core import commands

class Amplify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def amplify(self, ctx):
        # Set amplification factor (2x in this case)
        amplify_factor = 2

        # Record the last 10 seconds of audio
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        audio_source = voice_client.listen(timeout=10)
        await asyncio.sleep(0.1)
        await voice_client.disconnect()

        # Amplify audio data
        audio_data = await audio_source.read()
        cmd = ['ffmpeg', '-f', 's16le', '-ar', '48000', '-ac', '2', '-i', '-', '-af', f'volume={amplify_factor}', '-f', 's16le', '-ar', '48000', '-ac', '2', '-']
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = process.communicate(input=audio_data)
        amplified_audio_data = stdout_data

        # Play amplified audio in voice channel
        voice_client = await voice_channel.connect()
        audio_source = discord.FFmpegPCMAudio(source=amplified_audio_data)
        voice_client.play(audio_source, after=lambda e: print('Finished playing audio'))
        while voice_client.is_playing():
            await asyncio.sleep(0.1)
        await voice_client.disconnect()

def setup(bot):
    bot.add_cog(Amplify(bot))
