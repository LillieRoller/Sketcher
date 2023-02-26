from typing import List
import crc8

def checksum(data):
    """given the list of bytes, this returns the checksum for the bytes"""
    calc = crc8.crc8()
    calc.update(bytearray(data))
    return int(calc.hexdigest(), 16)

def add_checksum_to_list(data:List[int]):
    """Given the list of bytes it will return the check sum and append it to a copy of the list"""
    actual = data.copy()
    actual.append(checksum(data))
    return actual