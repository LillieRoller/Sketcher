import crc8
from sketcher.common.checksum import checksum

def test_example():
	hash = crc8.crc8()
	hash.update(b'123')
	assert hash.hexdigest() == 'c0'
	assert hash.digest() == b'\xc0'

def test_drive_forward():
	hash = crc8.crc8()
	hash.update(b'\x01\x04\x00\x00\x00\x00\x64\x00\x00\x00\x64\x00\x00\x00\x00\x00\x00\x00\x00')
	assert hash.hexdigest() == 'd1'

def test_drive_forward_array():
	data = [0x01, 0x04, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
	assert checksum(data) == 0xd1

def test_checksum_appended_to_bytearray():
	data = [0x01, 0x04, 0x00, 0x00, 0x00]
	expected = [0x01, 0x04, 0x00, 0x00, 0x00, 0x3a]
	calc = crc8.crc8()
	calc.update(bytearray(data))
	actual = data.copy()
	checksum = int(calc.hexdigest(), 16)
	actual.append(checksum)
	assert expected == actual