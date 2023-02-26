def drive_forward_distance(mm:int):
    """Instruct the robot to drive straight forward the given distance in millimeters"""
    base_bytes = [1, 8, 0]
    distance_bytes = list(mm.to_bytes(4, byteorder = 'big'))
    base_bytes.extend(distance_bytes)
    zero_fill_length = 19 - len(base_bytes)
    listofzeros = [0] * zero_fill_length
    base_bytes.extend(listofzeros)
    return base_bytes