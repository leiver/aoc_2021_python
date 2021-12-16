import math

from timing import timing
import os
import sys
from numpy import prod


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    packet, _, _ = parse_packet("", get_binary_input_from_file())

    print(sum_version(packet))


def part2():
    packet, _, _ = parse_packet("", get_binary_input_from_file())

    print(calculate_packet(packet))


def calculate_packet(packet):
    packet_type = packet.packet_type
    if packet_type == 4:
        return packet.packet_value
    else:
        sub_packet_values = [calculate_packet(sub_packet) for sub_packet in packet.sub_packets]
        if packet_type == 0:
            return sum(sub_packet_values)
        elif packet_type == 1:
            return prod(sub_packet_values)
        elif packet_type == 2:
            return min(sub_packet_values)
        elif packet_type == 3:
            return max(sub_packet_values)
        elif packet_type == 5:
            return sub_packet_values[0] > sub_packet_values[1]
        elif packet_type == 6:
            return sub_packet_values[0] < sub_packet_values[1]
        elif packet_type == 7:
            return sub_packet_values[0] == sub_packet_values[1]
        else:
            raise Exception("unsupported operation")


def get_binary_input_from_file():
    file = open(os.path.join(sys.path[0], "inputs/input_day16.txt"), "r")
    hex_input = file.read().strip()
    amount_of_bits = len(hex_input) * 4
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=amount_of_bits, type='b')
    binary_input = format(int(hex_input, 16), spec)
    return binary_input


def sum_version(packet):
    return packet.packet_version + sum([sum_version(sub_packet) for sub_packet in packet.sub_packets])


def parse_packet(packet_data, binary_input):
    packet_version, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, 3)
    packet_version = int(packet_version, 2)
    packet_type, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, 3)
    packet_type = int(packet_type, 2)

    packet_value = None
    sub_packets = []
    if packet_type == 4:
        literal_value_binary = ""
        while True:
            value, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, 5)
            literal_value_continues = int(value[0])
            literal_value_binary += value[1:5]
            if not literal_value_continues:
                break
        packet_value = int(literal_value_binary, 2)
    else:
        length_indicator, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, 1)
        length_indicator = int(length_indicator)
        if length_indicator:
            amount_of_packets, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, 11)
            amount_of_packets = int(amount_of_packets, 2)
            for _ in range(amount_of_packets):
                sub_packet, packet_data, binary_input = parse_packet(packet_data, binary_input)
                sub_packets.append(sub_packet)
        else:
            amount_of_bits, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, 15)
            amount_of_bits = int(amount_of_bits, 2)
            sub_packet_data, packet_data, binary_input = get_value_from_packet_data(packet_data, binary_input, amount_of_bits)
            while sub_packet_data:
                sub_packet, sub_packet_data, _ = parse_packet(sub_packet_data, "")
                sub_packets.append(sub_packet)

    return (Packet(packet_version, packet_type, packet_value, sub_packets)), packet_data, binary_input


def get_value_from_packet_data(packet_data, binary_input, length):
    if len(packet_data) < length:
        bits_to_fill = math.ceil((length - len(packet_data)) / 4) * 4
        packet_data += binary_input[:bits_to_fill]
        binary_input = binary_input[bits_to_fill:]
    return packet_data[:length], packet_data[length:], binary_input


def fill_packet_data(packet_data, binary_input, min_length):
    if len(packet_data) < min_length:
        bits_to_fill = math.ceil((min_length - len(packet_data)) / 4)
        packet_data += binary_input[:bits_to_fill]
        binary_input = binary_input[bits_to_fill:]
    return packet_data, binary_input


class Packet:
    def __init__(self, packet_version, packet_type, packet_value, sub_packets):
        self.packet_version = packet_version
        self.packet_type = packet_type
        self.packet_value = packet_value
        self.sub_packets = sub_packets

    def __str__(self):
        sub_packet_joiner = '\nsub_packet: '
        sub_packets_string = f"sub_packets={sub_packet_joiner}{sub_packet_joiner.join([sub_packet.__str__() for sub_packet in self.sub_packets])}" if self.sub_packets else "sub_packets=None"
        return f"Packet: packet_version={self.packet_version}, packet_type={self.packet_type}, packet_value={self.packet_value}, {sub_packets_string}"
