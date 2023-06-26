import asyncio  # import the asyncio module
from bleak import BleakClient  # import BleakClient from bleak library
from common.checksum import add_checksum_to_list  # import add_checksum_to_list function from the common.checksum module
from irobot.ble_protocol import drive_forward_distance, drive_distance_packet, rotate_angle_packet  # import these functions from irobot.ble_protocol
from irobot.robot_navigation import Point, LineSegment, Tracking  # import Point and LineSegment classes from irobot.robot_navigation
import time # import time module

RX = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # assign a string to RX variable
TX = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # assign a string to TX variable
ROOT_ADDRESS = "271ECDA9-2770-F9B8-6FC9-878F9E2625E4"  # assign a string to ROOT_ADDRESS variable
FIRMWARE_VERSION = "00002a26-0000-1000-8000-00805f9b34fb"  # assign a string to FIRMWARE_VERSION variable
SERIAL_NUMBER = "00002a25-0000-1000-8000-00805f9b34fb"  # assign a string to SERIAL_NUMBER variable

# function that connects to a BLE device with a given address
async def connect(address,points:list[Point]):
    async with BleakClient(address) as client:
        firmware_version = await client.read_gatt_char(FIRMWARE_VERSION)
        print("Firmware version: {0}".format("".join(map(chr, firmware_version))))
        serial_number = await client.read_gatt_char(SERIAL_NUMBER)
        print("Serial Number: {0}".format("".join(map(chr, serial_number))))

        previous_point = Point(0,0)
        for point in points:

            sec_between_instructions = 7
            segment = LineSegment(start = previous_point, destination = point )
            # Rotates the robot to calculated angle
            angle_packet = bytearray(rotate_angle_packet(segment.angle))
            await client.write_gatt_char(RX,angle_packet,True)
            time.sleep(sec_between_instructions)


            # droves the robot to calculated distance
            distance_packet = bytearray(drive_distance_packet(segment.distance))
            await client.write_gatt_char(RX,distance_packet,True)
            time.sleep(sec_between_instructions)

            reset_north = bytearray(rotate_angle_packet(-segment.angle))
            await client.write_gatt_char(RX,reset_north,True)
            time.sleep(sec_between_instructions)

            previous_point = point

def run(instructions:list[Point]):
    """Connect to the robot run hard coded trials"""
    asyncio.run(connect(ROOT_ADDRESS,instructions))