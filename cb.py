import asyncio
import os
import logging
from bleak import BleakScanner

TARGET_NAME = "None"   
CHECK_INTERVAL = 3
MISS_LIMIT = 3

logging.basicConfig(
    filename="bt_lock.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def lock_pc():
    logging.warning("Locking PC")
    os.system("rundll32.exe user32.dll,LockWorkStation")

async def monitor():
    misses = 0
    logging.info("Bluetooth proximity monitor started")

    while True:
        found = False

        devices = await BleakScanner.discover(timeout=5)
        for d in devices:
            if d.name == TARGET_NAME:
                found = True
                logging.info(f"Device found: RSSI={d.rssi}")
                break

        if found:
            misses = 0
        else:
            misses += 1
            logging.warning("Device not found")

            if misses >= MISS_LIMIT:
                lock_pc()
                break

        await asyncio.sleep(CHECK_INTERVAL)

asyncio.run(monitor())
