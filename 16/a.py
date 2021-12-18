with open("input.txt") as inp:
    bits = "".join('0' * (4 - len(bin(int(i, 16))[2:])) + bin(int(i, 16))[2:] for i in inp.readline().strip())

read_head = 0
version_sum = 0

while read_head < len(bits):
    #if we only have 0s left, quit
    if bits[read_head:].count('0') == len(bits[read_head:]): break
    print(bits[read_head:])
    # start a new packet
    version = int(bits[read_head:read_head+3], 2)
    read_head += 3

    version_sum += version
    print(version_sum)
    type_id = int(bits[read_head:read_head+3], 2)
    read_head += 3

    if type_id == 4:
        #literal value
        chunk = bits[read_head:read_head+5]
        read_head += 5
        payload = ''
        while chunk[0] == '1':
            payload += chunk[1:]
            chunk = bits[read_head:read_head+5]
            read_head += 5
        payload += chunk[1:]
        payload = int(payload,2)
    else:
        #operator
        length_type = bits[read_head]
        read_head += 1

        if length_type == '0':
            subpacket_bits = int(bits[read_head:read_head+15],2)
            read_head += 15
        else:
            subpacket_num = int(bits[read_head:read_head+11],2)
            read_head += 11

print(version_sum)