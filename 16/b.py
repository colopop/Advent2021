with open("input.txt") as inp:
    bits = "".join('0' * (4 - len(bin(int(i, 16))[2:])) + bin(int(i, 16))[2:] for i in inp.readline().strip())

import math
operations = [
    lambda x : sum(p.compute() for p in x),
    lambda x : math.prod(p.compute() for p in x),
    lambda x : min(p.compute() for p in x),
    lambda x : max(p.compute() for p in x),
    lambda x : x[0].compute(),
    lambda x : 1 if x[0].compute() > x[1].compute() else 0,
    lambda x : 1 if x[0].compute() < x[1].compute() else 0,
    lambda x : 1 if x[0].compute() == x[1].compute() else 0
]

class Packet:
    def __init__(self, version, type_id, type_info, size):
        self.version = version
        self.type = type_id
        if self.type == 4:
            self.payload = type_info
            self.req_remaining = 0
        else:
            self.operation = operations[type_id]
            mode, arg = type_info
            self.mode = mode
            self.subpacket_req = self.req_remaining = arg
        self.header_size = size
        self.subpackets = []
        self.parent = None

    def incomplete(self):
        return self.req_remaining > 0

    def add_child(self, packet):
        self.subpackets.append(packet)
        packet.parent = self
        self.update_requirement()

    def update_requirement(self):
        if self.mode == '0':
            self.req_remaining = self.subpacket_req - sum(p.total_size() for p in self.subpackets)
        else:
            self.req_remaining = self.subpacket_req - len(self.subpackets)
        if self.parent is not None:
            self.parent.update_requirement()

    def total_size(self):
        return self.header_size + sum(p.total_size() for p in self.subpackets)

    def compute(self):
        if self.type == 4:
            return self.payload
        else:
            return self.operation(self.subpackets)

packets = []

read_head = 0
while read_head < len(bits):
    #if we only have 0s left, quit
    if bits[read_head:].count('0') == len(bits[read_head:]): break

    # start a new packet
    packet_start = read_head
    version = int(bits[read_head:read_head+3], 2)
    read_head += 3

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

        packet = Packet(version, type_id, payload, read_head - packet_start)

    else:
        #operator
        length_type = bits[read_head]
        read_head += 1

        if length_type == '0':
            subpacket_arg = int(bits[read_head:read_head+15],2)
            read_head += 15
        else:
            subpacket_arg = int(bits[read_head:read_head+11],2)
            read_head += 11

        packet = Packet(version, type_id, (length_type, subpacket_arg), read_head - packet_start)

    #place the packet
    packets.append(packet)
    if len(packets) > 1:
        i = len(packets) - 2
        while i >= 0:
            if packets[i].incomplete():
                packets[i].add_child(packet)
                break
            i -= 1

print(packets[0].compute())