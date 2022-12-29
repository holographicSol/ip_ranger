""" Written by Benjamin Jack Cullen

Module: IPv4_Power_Ranger_Module

Description:
    * Returns lists of private IPV4 address ranges.
    * Returns lists of public IPV4 address ranges.
    * Iterate through listed ranges.
    * Iterate through unlisted ranges.

"""

import socket
import struct


def total_private_ipv4_addresses():
    """ return total current private IPv4 addresses """
    i = 0
    for _ in provide_private_ranges():
        i += _[2]
    return i


def total_public_ipv4_addresses():
    """ return total current public IPv4 addresses """
    i = 0
    for _ in provide_public_ranges():
        i += _[2]
    return i


def total_ipv4_addresses():
    return total_private_ipv4_addresses() + total_public_ipv4_addresses()


def provide_public_ranges():
    """
    IPv4 address range source:
    source: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
    """
    return [
        ['1.0.0.0', '9.255.255.255', 150994944],
        ['11.0.0.0', '100.63.255.255', 1497366528],
        ['100.128.0.0', '126.255.255.255', 444596224],
        ['128.0.0.0', '169.253.255.255', 704512000],
        ['169.255.0.0', '172.15.255.255', 34668544],
        ['172.32.0.0', '191.255.255.255', 333447168],
        ['192.0.1.0', '192.0.1.255', 256],
        ['192.0.3.0', '192.31.195.255', 2081024],
        ['192.31.197.0', '192.52.192.255', 1375232],
        ['192.52.194.0', '192.88.98.255', 2334976],
        ['192.88.100.0', '192.167.255.255', 5217280],
        ['192.169.0.0', '192.175.47.255', 405504],
        ['192.175.49.0', '198.17.255.255', 90361600],
        ['198.20.0.0', '198.51.99.255', 2057216],
        ['198.51.101.0', '203.0.112.255', 80546816],
        ['203.0.114.0', '239.255.255.255', 620727808],
    ]


def provide_private_ranges():
    """
    Source table:
    source: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
    Note: excluded from these lists: overlap in accordance to above source table.
    [Start_Range, End_Range, Quantity_In_Range]
    """
    return [
        ["0.0.0.0", "0.255.255.255", 16777216],
        ["10.0.0.0", "10.255.255.255", 16777216],
        ["100.64.0.0", "100.127.255.255", 4194304],
        ["127.0.0.0", "127.255.255.255", 16777216],
        ["169.254.0.0", "169.254.255.255", 65536],
        ["172.16.0.0", "172.31.255.255", 1048576],
        ["192.0.0.0", "192.0.0.255", 256],
        ["192.0.2.0", "192.0.2.255", 256],
        ["192.31.196.0", "192.31.196.255", 256],
        ["192.52.193.0", "192.52.193.255", 256],
        ["192.88.99.0", "192.88.99.255", 256],
        ["192.168.0.0", "192.168.255.255", 65536],
        ["192.175.48.0", "192.175.48.255", 256],
        ["198.18.0.0", "198.19.255.255", 131072],
        ["198.51.100.0", "198.51.100.255", 256],
        ["203.0.113.0", "203.0.113.255", 256],
        ["240.0.0.0", "255.255.255.254", 268435455],
        ["255.255.255.255", "255.255.255.255", 1]
    ]


def iter_ips(index=int):
    """ Return an address
    int(index) refers to socket.inet_ntoa(struct.pack('>I', index))
    """
    return socket.inet_ntoa(struct.pack('>I', index))


def iter_ips_inverse(ip):
    """ Return an index
    str(ip) refers to struct.unpack('>I', socket.inet_aton(ip))[0]
    """
    return struct.unpack('>I', socket.inet_aton(ip))[0]


def ips(start, end):
    """
    Create a complete list of addresses in xrange (potentially memory intensive)
    """
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def is_ip_index_public(ip):
    """
    is_ip_index_public(int) Example: int(0)
    is_ip_index_public(str) Example: str("0.0.0.0")
    """
    q = False
    if not str(ip).isdigit():
        ip = int(struct.unpack('>I', socket.inet_aton(ip))[0])
    for _ in provide_public_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if ip in range(start, end):
            q = True
            break
    return q


def is_ip_private(ip):
    """
    is_ip_index_private(int) Example: int(0)
    is_ip_index_private(str) Example: str("0.0.0.0")
    """
    q = False
    if not str(ip).isdigit():
        ip = int(struct.unpack('>I', socket.inet_aton(ip))[0])
    for _ in provide_private_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if ip in range(start, end):
            q = True
            break
    return q

# print(is_ip_index_public('1.0.0.0'))
