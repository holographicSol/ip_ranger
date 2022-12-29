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


def provide_public_ranges():
    """
    Source table:
    source: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
    """
    return [
        ['1.0.0.0', '9.255.255.255'],
        ['11.0.0.0', '100.63.255.255'],
        ['100.128.0.0', '126.255.255.255'],
        ['128.0.0.0', '169.253.255.255'],
        ['169.255.0.0', '172.15.255.255'],
        ['172.32.0.0', '191.255.255.255'],
        ['192.0.1.0', '192.0.1.255'],
        ['192.0.3.0', '192.31.195.255'],
        ['192.31.197.0', '192.52.192.255'],
        ['192.52.194.0', '192.88.98.255'],
        ['192.88.100.0', '192.167.255.255'],
        ['192.169.0.0', '192.175.47.255'],
        ['192.175.49.0', '198.17.255.255'],
        ['198.20.0.0', '198.51.99.255'],
        ['198.51.101.0', '203.0.112.255'],
        ['203.0.114.0', '239.255.255.255'],
    ]


def provide_private_ranges():
    """
    Source table:
    source: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
    """
    return [
        ["0.0.0.0", "0.255.255.255"],
        ["10.0.0.0", "10.255.255.255"],
        ["100.64.0.0", "100.127.255.255"],
        ["127.0.0.0", "127.255.255.255"],
        ["169.254.0.0", "169.254.255.255"],
        ["172.16.0.0", "172.31.255.255"],
        ["192.0.0.0", "192.0.0.255"],
        ["192.0.0.0", "192.0.0.7"],
        ["192.0.0.8", "192.0.0.8"],
        ["192.0.0.9", "192.0.0.9"],
        ["192.0.0.10", "192.0.0.10"],
        ["192.0.0.170", "192.0.0.170"],
        ["192.0.0.171", "192.0.0.171"],
        ["192.0.2.0", "192.0.2.255"],
        ["192.31.196.0", "192.31.196.255"],
        ["192.52.193.0", "192.52.193.255"],
        ["192.88.99.0", "192.88.99.255"],
        ["192.168.0.0", "192.168.255.255"],
        ["192.175.48.0", "192.175.48.255"],
        ["198.18.0.0", "198.19.255.255"],
        ["198.51.100.0", "198.51.100.255"],
        ["203.0.113.0", "203.0.113.255"],
        ["240.0.0.0", "255.255.255.255"],
        ["255.255.255.255", "255.255.255.255"]
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
    if not str(ip).isdigit():
        ip = int(struct.unpack('>I', socket.inet_aton(ip))[0])
    for _ in provide_public_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if ip in range(start, end):
            return True
        else:
            return False


def is_ip_private(ip):
    """
    is_ip_index_private(int) Example: int(0)
    is_ip_index_private(str) Example: str("0.0.0.0")
    """
    if not str(ip).isdigit():
        ip = int(struct.unpack('>I', socket.inet_aton(ip))[0])
    for _ in provide_private_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if ip in range(start, end):
            return True
        else:
            return False
