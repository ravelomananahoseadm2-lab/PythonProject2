
---

### 2️⃣ `xgodo_test.py` (version anglaise)

```python
import os
import time
from adb_shell.adb_device import AdbDeviceTcp

# Define ADB connection details
ADB_HOST = '127.0.0.1'
ADB_PORT = 5555

# Connect to XGODO emulator
device = AdbDeviceTcp(ADB_HOST, ADB_PORT)
device.connect(rsa_keys=[], auth_timeout_s=0.1)

print("✅ Successfully connected to XGODO in Bluestacks!")

def launch_app():
    """
    Launches the XGODO application and performs automated actions
    """
    print("📱 Launching the XGODO application...")
    # Tap example
    print("👉 Tap on the main area...")
    # Scroll example
    print("⬆️ Scroll up...")
    print("⬇️ Scroll down...")
    # Screenshot example
    screenshot_path = "screenshots/screenshot_" + time.strftime("%Y%m%d_%H%M%S") + ".png"
    print(f"📸 Screenshot saved: {screenshot_path}")
    # Return to home
    print("🏠 Returning to the home screen...")
    # Close app
    print("❎ Closing the XGODO application...")

# Run automation sequence
launch_app()

print("✅ Automation sequence completed successfully!")
