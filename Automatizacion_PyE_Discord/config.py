import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de credenciales
EMAIL = os.getenv("DISCORD_EMAIL")
PASSWORD = os.getenv("DISCORD_PASSWORD")

# Configuración del navegador
BROWSER_OPTIONS = {
    "slow_mo": 0,
    "headless": True,
    "args": ["--start-maximized"]
}