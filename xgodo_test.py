from adb_shell.adb_device import AdbDeviceTcp
from datetime import datetime
import os
import time

# --- Connexion à Bluestacks / XGODO ---
device = AdbDeviceTcp(host="127.0.0.1", port=5555)

# --- Préparer le dossier pour les logs et screenshots ---
screenshots_dir = "screenshots"
logs_dir = "logs"
os.makedirs(screenshots_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)

# Nom du fichier log
log_file_path = os.path.join(logs_dir, f"xgodo_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

def log(message):
    """Écrire le message à la fois sur la console et dans le fichier log"""
    print(message)
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

try:
    device.connect()
    if device.available:
        log("✅ Connexion réussie à XGODO dans Bluestacks !")

        # --- Lancer l’application ---
        log("📱 Lancement de l'application XGODO...")
        device.shell("am start -n com.xgodo.app/.MainActivity")
        time.sleep(5)

        # --- Tap sur la zone principale ---
        log("👉 Tap sur la zone principale...")
        device.shell("input tap 300 600")
        time.sleep(3)

        # --- Scroll haut ---
        log("⬆️ Défilement vers le haut...")
        device.shell("input swipe 500 1200 500 400 300")
        time.sleep(2)

        # --- Scroll bas ---
        log("⬇️ Défilement vers le bas...")
        device.shell("input swipe 500 400 500 1200 300")
        time.sleep(2)

        # --- Capture d’écran ---
        screenshot_path = os.path.join(
            screenshots_dir, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        image_data = device.shell("screencap -p", decode=False)
        with open(screenshot_path, "wb") as f:
            f.write(image_data)
        log(f"📸 Capture d’écran enregistrée : {screenshot_path}")

        # --- Retour à l’accueil ---
        log("🏠 Retour à l’écran d’accueil...")
        device.shell("input keyevent 3")
        time.sleep(1)

        # --- Fermeture de l’application ---
        log("❎ Fermeture de l'application XGODO...")
        device.shell("am force-stop com.xgodo.app")

        log("✅ Séquence d’automatisation terminée avec succès !")

    else:
        log("❌ Impossible de se connecter à l’appareil.")

except Exception as e:
    log(f"🚨 Erreur lors de la connexion ou de l’automatisation : {e}")
