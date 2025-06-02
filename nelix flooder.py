# AVANT DE DIRE QUE SA MARCHE PAS ALLEZ DANS LE CMD ET FAITES CES COMMANDES:
# pip install discord
# pip install pytz

import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import pytz
TOKEN = "CHANGE LE TOKEN ET LAISSE LES GUILLEMET" # TOKEN FAUT LE CHANGER BANDE DE NEGRION
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"bot en ligne sal bougnoul")
    await bot.change_presence(
        activity=discord.Game(name="status du bot"), # LE STATUS DU BOT CHANGEZ LE BANDE DE BOUGNOULE
        status=discord.Status.dnd
    )
    try:
        synced = await bot.tree.sync()
        print(f"Synchronisé {len(synced)} commandes slash.")
    except Exception as e:
        print(f"Erreur syncro des commande : {e}")

@bot.tree.command(name="flood", description="Commande de flood (DM ou Serveur)")
@app_commands.describe(texte="Texte à flooder")
async def gen(interaction: discord.Interaction, texte: str):
    await interaction.response.send_message("baizage de serveur", ephemeral=True)
    for _ in range(5):
        await interaction.followup.send(texte, ephemeral=False)
    user = interaction.user
    paris_tz = pytz.timezone("Europe/Paris")
    current_time = datetime.now(paris_tz).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time} by {user.name}] Message is <{texte}>")
bot.run(TOKEN)
