from enum import IntEnum
from common.checksum import add_checksum_to_list

class Device(IntEnum):
    """The robot is organized into a collection of logical and independent devices.
    Each device is a subsystem of the robot (such as the motors or color sensor)
    that only accepts packets that pertain to itself."""
    GENERAL = 0
    MOTORS = 1

class Command(IntEnum):
    """Each device implements a series of commands. The command number tells each device how to interpret
    the contents of the payload. Some commands will trigger the robot to send a response packet."""
    DRIVE_DISTANCE = 8
    ROTATE_ANGLE = 12


def drive_forward_distance(mm: int):
    """Instruct the robot to drive straight forward the given distance in millimeters"""
    base_bytes = [1, 8, 0]
    distance_bytes = list(mm.to_bytes(4, byteorder='big'))
    base_bytes.extend(distance_bytes)
    zero_fill_length = 19 - len(base_bytes)
    listofzeros = [0] * zero_fill_length
    base_bytes.extend(listofzeros)
    return base_bytes


def packet(dev: Device, cmd: Command, id: int = 0)->list:
    """the base of the devices packet that will stay constant without the checksum"""
    finalList = [0] * 19
    finalList[0] = int(dev)
    finalList[1] = int(cmd)
    finalList[2] = id
    return finalList

def drive_distance_packet(cm: int):
    """adding the vried payload for the specific drive forward packet"""
    mm = cm * 10
    payload = list(mm.to_bytes(4, byteorder='big'))
    # payload:          [0][1][2][3]
    # packet : [0][1][2][3][4][5][6]
    result = packet(dev = Device.MOTORS, cmd = Command.DRIVE_DISTANCE)
    result[3] = payload[0]
    result[4] = payload[1]
    result[5] = payload[2]
    result[6] = payload[3]
    result = add_checksum_to_list(result)
    return result

def rotate_angle_packet(degree):
    decidegree = degree * 10
    payload = list(decidegree.to_bytes(4, byteorder='big'))
    result = packet(dev = Device.MOTORS, cmd = Command.ROTATE_ANGLE)
    result[3] = payload[0]
    result[4] = payload[1]
    result[5] = payload[2]
    result[6] = payload[3]
    result = add_checksum_to_list(result)
    return result


def navigate_to(x, y):
    """need to create equations to calculate in order for navigate_to to exist"""