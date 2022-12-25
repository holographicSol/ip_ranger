""" Written by Benjamin Jack Cullen """

import socket
import struct


def ips(start, end):
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def compile_0_0_0_0_to_0_255_255_255():
    """
    Description: Current network.
    Scope: Software
    Reserved: True
    Expected number of addresses: 16777216
    """
    return ips('0.0.0.0', '0.255.255.255')


def compile_10_0_0_0_to_10_255_255_255():
    """
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 16777216
    """
    return ips('10.0.0.0', '10.255.255.255')


def compile_100_64_0_0_to_100_127_255_255():
    """
    Description: Shared address space for communications between a service provider and
    its subscribers when using a carrier-grade NAT.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 4194304
    """
    return ips('100.64.0.0', '100.127.255.255')


def compile_127_0_0_0_to_127_255_255_255():
    """
    Description: Used for loopback addresses to the local host.
    Scope: Host
    Reserved: True
    Expected number of addresses: 16777216
    """
    return ips('127.0.0.0', '127.255.255.255')


def compile_169_254_0_0_to_169_254_255_255():
    """
    Description: Used for link-local addresses[5] between two hosts on a
    single link when no IP address is otherwise specified, such
    as would have normally been retrieved from a DHCP server.
    Scope: Subnet
    Reserved: True
    Expected number of addresses: 65536
    """
    return ips('169.254.0.0', '169.254.255.255')


def compile_172_16_0_0_to_172_31_255_255():
    """
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 1048576
    """
    return ips('172.16.0.0', '172.31.255.255')


def compile_192_0_0_0_to_192_0_0_255():
    """
    Description: IETF Protocol Assignments
    Scope: Private network
    Reserved: True
    Expected number of addresses: 256
    """
    return ips('192.0.0.0', '192.0.0.255')


def compile_192_0_2_0_to_192_0_2_255():
    """
    Description: Assigned as TEST-NET-1
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    """
    return ips('192.0.2.0', '192.0.2.255')


def compile_192_88_99_0_to_192_88_99_255():
    """
    Description: Formerly used for IPv6 to IPv4 relay
    (included IPv6 address block 2002::/16).
    Scope: Internet
    Reserved: True
    Expected number of addresses: 256
    """
    return ips('192.88.99.0', '192.88.99.255')


def compile_192_168_0_0_to_192_168_255_255():
    """
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 65536
    """
    return ips('192.168.0.0', '192.168.255.255')


def compile_198_18_0_0_to_198_19_255_255():
    """
    Description: Used for benchmark testing of inter-network communications
    between two separate subnets
    Scope: Private network
    Reserved: True
    Expected number of addresses: 131072
    """
    return ips('198.18.0.0', '198.19.255.255')


def compile_198_51_100_0_to_198_51_100_255():
    """
    Description: Assigned as TEST-NET-2, documentation and examples
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    """
    return ips('198.51.100.0', '198.51.100.255')


def compile_203_0_113_0_to_203_0_113_255():
    """
    Description: Assigned as TEST-NET-3, documentation and examples
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    """
    return ips('203.0.113.0', '203.0.113.255')


def compile_224_0_0_0_to_239_255_255_255():
    """
    Description: In use for IP multicast. (Former Class D network.)
    Scope: Internet
    Reserved: True
    Expected number of addresses: 268435456
    """
    return ips('224.0.0.0', '239.255.255.255')


def compile_233_252_0_0_to_233_252_0_255():
    """
    Description: Assigned as MCAST-TEST-NET, documentation and examples.
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    """
    return ips('233.252.0.0', '233.252.0.255')


def compile_240_0_0_0_to_255_255_255_254():
    """
    Description: Reserved for future use. (Former Class E network.)
    Scope: Internet
    Reserved: True
    Expected number of addresses: 268435455
    """
    return ips('240.0.0.0', '255.255.255.254')


def compile_255_255_255_255():
    """
    Description: Reserved for the "limited broadcast" destination address
    Scope: Subnet
    Reserved: True
    Expected number of addresses: 1
    """
    return '255.255.255.255'
