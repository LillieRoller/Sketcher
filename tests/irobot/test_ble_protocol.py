from src.irobot.ble_protocol import drive_forward_distance, packet, Device, Command, drive_distance_packet

def test_drive_forward():
    expected = [0x01, 0x08, 0x00, 0x00, 0x00, 0x00, 0xa0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    actual = drive_forward_distance(160)
    assert actual == expected

def test_packet():
    expected_device = Device.MOTORS
    expected_command = Command.DRIVE_DISTANCE
    expected_id = 1
    actual = packet(dev = expected_device, cmd = expected_command, id = expected_id)
    assert len(actual) == 19
    assert actual[0] == expected_device
    assert actual[1] == expected_command
    assert actual[2] == expected_id

def test_drive_distance_packet():
    expected_cm = 21346497
    actual = drive_distance_packet(expected_cm)
    assert actual[3] == 0x0C
    assert actual[4] == 0xB9
    assert actual[5] == 0x37
    assert actual[6] == 0x8A
    assert actual[19] != 0