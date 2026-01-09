from bleak import BleakScanner
import asyncio

async def scan():
    devices = await BleakScanner.discover(timeout=5)
    for d in devices:
        print(d.name)

asyncio.run(scan())