""" Written by Benjamin Jack Cullen

IPv4 Range Enumerator

options:
    return complete lists of IPv4 address range(s).
    return a list of public/private IPv4 address ranges.
    return a single (iterable) IPv4 address by index

    Return a list of IPv4 addresses for a given range: (potentially extremely memory intensive, use only if needed).
    Example: print(module_ip_power_ranger.compile_192_0_1_0_to_192_0_1_255)

    Return a list of public IPv4 address ranges:
    Example: print(module_ip_power_ranger.provide_public_ranges)

    Iterate over n IPv4 addresses in x IPv4 address range:
    Example:
        import module_ip_power_ranger
        import socket
        import struct
        public_ips = module_ip_power_ranger.provide_public_ranges()
        range_0_start = public_ips[0][0]
        range_0_end = public_ips[0][1]
        index_0 = struct.unpack('>I', socket.inet_aton(range_0_start))[0]
        index_1 = struct.unpack('>I', socket.inet_aton(range_0_end))[0]
        for n in range(index_0, index_1):
                x = module_ip_power_ranger.iter_ips(index=n)
                n += 1

    Arbitrary ranging:
    Example:
        for n in range(0, 16777216):
            if module_ip_power_ranger.is_ip_index_public(n) is False:
                x = module_ip_power_ranger.iter_ips(index=n)
            n += 1

"""

import socket
import struct

"""
this is close but not perfect. do not rely on this for now.
trying to adhere to the IANA table.
source: https://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml
"""

def provide_public_ranges():
    return [
        ['1.0.0.0', '9.255.255.255', 150994944],
        ['11.0.0.0', '100.63.255.255', 1497366528],
        ['100.128.0.0', '126.255.255.255', 444596224],
        ['128.0.0.0', '169.253.255.255', 704512000],
        ['169.255.255.255', '172.15.255.255', 34603009],
        ['172.32.0.0', '191.255.255.255', 333447168],
        ['192.0.1.0', '192.0.1.255', 256],
        ['192.0.3.0', '192.88.98.255', 5791744],
        ['192.88.100.0', '192.167.255.255', 5217280],
        ['192.169.0.0', '198.17.255.255', 90767360],
        ['198.20.0.0', '198.51.99.255', 2057216],
        ['198.51.101.0', '203.0.112.255', 80546816],
        ['203.0.114.0', '223.255.255.255', 352292352]
    ]


def provide_private_ranges():
    return [
        ["0.0.0.0", "0.255.255.255", 16777216],
        ["10.0.0.0", "10.255.255.255", 16777216],
        ["100.64.0.0", "100.127.255.255", 4194304],
        ["127.0.0.0", "127.255.255.255", 16777216],
        ["169.254.0.0", "169.254.255.255", 65536],
        ["172.16.0.0", "172.31.255.255", 1048576],
        ["192.0.0.0", "192.0.0.7", 8],
        ["192.0.0.0", "192.0.0.7", 8],
        ["192.0.0.8", "192.0.0.8", 1],
        ["192.0.0.9", "192.0.0.9", 1],
        ["192.0.0.10", "192.0.0.10", 1],
        ["192.0.0.170", "192.0.0.170", 1],
        ["192.0.0.171", "192.0.0.171", 1],
        ["192.0.2.0", "192.0.2.255", 256],
        ["192.31.196.0", "192.31.196.255", 256],
        ["192.52.193.0", "192.52.193.255", 256],
        ["192.88.99.0", "192.88.99.255", 256],
        ["192.168.0.0", "192.168.255.255", 65536],
        ["192.175.48.0", "192.175.48.255", 256],
        ["198.18.0.0", "198.19.255.255", 131072],
        ["198.51.100.0", "198.51.100.255", 256],
        ["203.0.113.0", "203.0.113.255", 256],
        ["224.0.0.0", "239.255.255.255", 268435456],
        ["240.0.0.0", "255.255.255.255", 268435456],
        ["255.255.255.255", "255.255.255.255", 1]
    ]

import ipaddress
start = ipaddress.ip_network('198.18.0.0/15')
print('    ["' + str(start[0]) + '", "' + str(start[-1]) + '"],' )


def iter_ips(index=int):
    return socket.inet_ntoa(struct.pack('>I', index))


def ips(start, end):
    """

    """
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def is_ip_index_public(index=int):
    """
    Takes socket.inet_aton index integer as index=int
    """
    for _ in provide_public_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if index in range(start, end):
            return True
        else:
            return False


def is_ip_index_private(index=int):
    """
    Takes socket.inet_aton index integer as index=int
    """
    for _ in provide_private_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if index in range(start, end):
            return True
        else:
            return False

