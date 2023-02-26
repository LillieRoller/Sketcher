import crc8

def checksum(data):
    """given the list of bytes, this returns the checksum for the bytes"""
    calc = crc8.crc8()
    calc.update(bytearray(data))
    return int(calc.hexdigest(), 16)