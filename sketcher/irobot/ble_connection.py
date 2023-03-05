import asyncio
from bleak import BleakClient
from sketcher.common.checksum import add_checksum_to_list
from sketcher.irobot.ble_protocol import drive_forward_distance, drive_distance_packet
import time

RX = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
TX = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
ROOT_ADDRESS = "271ECDA9-2770-F9B8-6FC9-878F9E2625E4"
FIRMWARE_VERSION = "00002a26-0000-1000-8000-00805f9b34fb"
SERIAL_NUMBER = "00002a25-0000-1000-8000-00805f9b34fb"

# both wheels forward 64/100 speed
drive_forward = [0x01, 0x04, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
drive_forward_left = [0x01, 0x06, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
rotate_angle = [0x01, 0x0c, 0x00, 0x00, 0x00, 0x07, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
# not yet compatible with the 2.1 firmware version only the 2.3 which is not yet available
navigate_to = [0x01, #dev
               0x11, #cmd
               0x00, #ID inc
               0x00, 0x00, 0x00, 0xa0, #X
               0x00, 0x00, 0x00, 0xa0, #Y
               0x00, 0x00, #heading
               0x00, 0x00, 0x00, 0x00, 0x00, 0x00 #ignored
               #checksum must be calculated and appended
               ]


async def connect(address):
    async with BleakClient(address) as client:
        firmware_version = await client.read_gatt_char(FIRMWARE_VERSION)
        print("Firmware version: {0}".format("".join(map(chr, firmware_version))))
        serial_number = await client.read_gatt_char(SERIAL_NUMBER)
        print("Serial Number: {0}".format("".join(map(chr, serial_number))))
        # data = bytearray(add_checksum_to_list(navigate_to))
        # data = bytearray(add_checksum_to_list(drive_forward))
        # data = bytearray(add_checksum_to_list(drive_forward_left))
        # data = bytearray(add_checksum_to_list(drive_forward_distance(160)))
        # data = bytearray(add_checksum_to_list(rotate_angle))
        data = bytearray(drive_distance_packet(160))
        i = 0
        loop_count = 1
        while i < loop_count:
            print(i)
            write_result = await client.write_gatt_char(RX,data,True)
            i += 1
        print(data)
        time.sleep(5)

def run():
    """Connect to the robot run hard coded trials"""
    asyncio.run(connect(ROOT_ADDRESS))