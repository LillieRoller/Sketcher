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

# set of bytes that represent different robot commands
# a set of bytes that represents navigating to a specific point on the robot's map
drive_forward = [0x01, 0x04, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
drive_forward_left = [0x01, 0x06, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
rotate_angle = [0x01, 0x0c, 0x00, 0x00, 0x00, 0x07, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
navigate_to = [0x01, 0x11, 0x00, 0x00, 0x00, 0x00, 0x00, 0xa0, 0x00, 0x00, 0x00, 0xa0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# function that connects to a BLE device with a given address
async def connect(address,points:list[Point]):
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
        # data = bytearray(drive_distance_packet(160))
        # data = bytearray(rotate_angle_packet(360))

        # segment1 = LineSegment(Point(0,0), Point(0, 16))
        # segment2 = LineSegment(Point(0,16), Point(0, 0))
        # segment1_rotate_angle = bytearray(rotate_angle_packet(segment1.angle))
        # segment1_drive_distance = bytearray(rotate_angle_packet(segment1.angle))
        # await.client.write_gatt_char(RX,segment1_rotate_angle, True)
        # time.sleep(5)
        # await.client.write_gatt_char(RX,segment1_drive_distance, True)
        # time.sleep(5)

        previous_point = Point(0,0)
        for point in points:

            sec_between_instructions = 5
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







        # segment2 = LineSegment(Point(0,0), Point(16,16))
        # segment2_rotate_angle = bytearray(rotate_angle_packet(segment2.angle))
        # segment2_drive_distance = bytearray(drive_distance_packet(segment2.distance))
        # segment2_finish_circle = bytearray(rotate_angle_packet(135))
        # await client.write_gatt_char(RX,segment2_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment2_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment2_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment2_finish_circle,True)
        # time.sleep(5)

        # segment3 = LineSegment(Point(0,0), Point(16,0))
        # segment3_rotate_angle = bytearray(rotate_angle_packet(segment3.angle))
        # segment3_drive_distance = bytearray(drive_distance_packet(segment3.distance))
        # segment3_finish_circle = bytearray(rotate_angle_packet(90))
        # await client.write_gatt_char(RX,segment3_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment3_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment3_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment3_finish_circle,True)
        # time.sleep(5)

        # segment4 = LineSegment(Point(0,0), Point(16,-16))
        # segment4_rotate_angle = bytearray(rotate_angle_packet(segment4.angle))
        # segment4_drive_distance = bytearray(drive_distance_packet(segment4.distance))
        # segment4_finish_circle = bytearray(rotate_angle_packet(45))
        # await client.write_gatt_char(RX,segment4_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment4_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment4_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment4_finish_circle,True)
        # time.sleep(5)

        # segment5 = LineSegment(Point(0,0), Point(0,-16))
        # segment5_rotate_angle = bytearray(rotate_angle_packet(segment5.angle))
        # segment5_drive_distance = bytearray(drive_distance_packet(segment5.distance))
        # segment5_finish_circle = bytearray(rotate_angle_packet(0))
        # await client.write_gatt_char(RX,segment5_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment5_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment5_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment5_finish_circle,True)
        # time.sleep(5)

        # segment6 = LineSegment(Point(0,0), Point(-16,-16))
        # segment6_rotate_angle = bytearray(rotate_angle_packet(segment6.angle))
        # segment6_drive_distance = bytearray(drive_distance_packet(segment6.distance))
        # segment6_finish_circle = bytearray(rotate_angle_packet(315))
        # await client.write_gatt_char(RX,segment6_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment6_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment6_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment6_finish_circle,True)
        # time.sleep(5)

        # segment7 = LineSegment(Point(0,0), Point(-16,0))
        # segment7_rotate_angle = bytearray(rotate_angle_packet(segment7.angle))
        # segment7_drive_distance = bytearray(drive_distance_packet(segment7.distance))
        # segment7_finish_circle = bytearray(rotate_angle_packet(270))
        # await client.write_gatt_char(RX,segment7_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment7_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment7_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment7_finish_circle,True)
        # time.sleep(5)

        # segment8 = LineSegment(Point(0,0), Point(-16,16))
        # segment8_rotate_angle = bytearray(rotate_angle_packet(segment8.angle))
        # segment8_drive_distance = bytearray(drive_distance_packet(segment8.distance))
        # segment8_finish_circle = bytearray(rotate_angle_packet(225))
        # await client.write_gatt_char(RX,segment8_rotate_angle,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment8_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,turn_around,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment8_drive_distance,True)
        # time.sleep(5)
        # await client.write_gatt_char(RX,segment8_finish_circle,True)
        # time.sleep(5)

        # i = 0
        # loop_count = 1
        # while i < loop_count:
        #     print(i)
        #     write_result = await client.write_gatt_char(RX,move1, move2,True)
        #     i += 1
        # time.sleep(5)

def run(instructions:list[Point]):
    """Connect to the robot run hard coded trials"""
    asyncio.run(connect(ROOT_ADDRESS,instructions))