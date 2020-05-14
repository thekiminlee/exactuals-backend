def encode(id):
    id_byte = id.encode('utf-8')
    num_id = int.from_bytes(id_byte, byteorder='big')
    return num_id

def decode(num_id):
    num_byte = num_id.to_bytes(((num_id.bit_length() + 7) // 8), byteorder='big')
    id = num_byte.decode('utf-8')
    return id