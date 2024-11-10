import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# 봇 설정
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class MidjourneyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user}로 로그인했습니다!")
        print("------")


bot = MidjourneyBot()

# Midjourney 채널 ID와 Midjourney 봇 ID 설정
MIDJOURNEY_CHANNEL_ID = int(os.getenv('MIDJOURNEY_CHANNEL_ID'))
MIDJOURNEY_BOT_ID = int(os.getenv('MIDJOURNEY_BOT_ID'))


@bot.tree.command(name="imagine", description="Midjourney로 이미지 생성")
async def imagine(interaction: discord.Interaction, prompt: str):
    """
    Midjourney 이미지 생성 명령어를 실행합니다.
    """
    # 먼저 응답을 지연시킵니다
    await interaction.response.defer(ephemeral=True)

    channel = bot.get_channel(MIDJOURNEY_CHANNEL_ID)
    if not channel:
        await interaction.followup.send("Midjourney 채널을 찾을 수 없습니다.", ephemeral=True)
        return

    try:
        # Midjourney 명령어 실행
        async with channel.typing():
            await channel.send(f"/imagine prompt: {prompt}")

        await interaction.followup.send(
            f"Midjourney 명령어를 실행했습니다!\n"
            f"프롬프트: {prompt}\n"
            f"채널 {channel.mention}에서 결과를 확인하세요.",
            ephemeral=True
        )

    except discord.Forbidden:
        await interaction.followup.send("봇이 해당 채널에 메시지를 보낼 권한이 없습니다.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.tree.command(name="variation", description="Midjourney 이미지 변형 생성")
async def variation(interaction: discord.Interaction, message_id: str, variation_number: int):
    """
    Midjourney 이미지의 변형을 생성합니다.
    """
    if not 1 <= variation_number <= 4:
        await interaction.response.send_message("변형 번호는 1에서 4 사이여야 합니다.", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True)

    channel = bot.get_channel(MIDJOURNEY_CHANNEL_ID)
    if not channel:
        await interaction.followup.send("Midjourney 채널을 찾을 수 없습니다.", ephemeral=True)
        return

    try:
        # V 버튼 클릭 에뮬레이션
        await channel.send(f"/variation {message_id} {variation_number}")

        await interaction.followup.send(
            f"변형 명령어를 실행했습니다!\n"
            f"메시지 ID: {message_id}, 변형 번호: {variation_number}\n"
            f"채널 {channel.mention}에서 결과를 확인하세요.",
            ephemeral=True
        )

    except Exception as e:
        await interaction.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.tree.command(name="upscale", description="Midjourney 이미지 업스케일")
async def upscale(interaction: discord.Interaction, message_id: str, upscale_number: int):
    """
    Midjourney 이미지를 업스케일합니다.
    """
    if not 1 <= upscale_number <= 4:
        await interaction.response.send_message("업스케일 번호는 1에서 4 사이여야 합니다.", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True)

    channel = bot.get_channel(MIDJOURNEY_CHANNEL_ID)
    if not channel:
        await interaction.followup.send("Midjourney 채널을 찾을 수 없습니다.", ephemeral=True)
        return

    try:
        # U 버튼 클릭 에뮬레이션
        await channel.send(f"/upscale {message_id} {upscale_number}")

        await interaction.followup.send(
            f"업스케일 명령어를 실행했습니다!\n"
            f"메시지 ID: {message_id}, 업스케일 번호: {upscale_number}\n"
            f"채널 {channel.mention}에서 결과를 확인하세요.",
            ephemeral=True
        )

    except Exception as e:
        await interaction.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


# Midjourney 봇의 응답 모니터링
@bot.event
async def on_message(message):
    if message.author.id == MIDJOURNEY_BOT_ID:
        # Midjourney 봇의 메시지를 처리하는 로직을 추가할 수 있습니다
        pass

    await bot.process_commands(message)


# 봇 실행
bot.run(os.getenv('DISCORD_TOKEN'))