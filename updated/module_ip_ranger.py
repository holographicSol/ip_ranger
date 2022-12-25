""" Written by Benjamin Jack Cullen """

import os
import socket
import struct


def ips(start, end):
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def compile_0_0_0_0_to_0_255_255_255(disk=False):
    """
    Description: Current network.
    Scope: Software
    Reserved: True
    Expected number of addresses: 16777216
    Expected Size on Disk: 219 MB
    """
    if disk is False:
        return ips('0.0.0.0', '0.255.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_0_0_0_0_to_0_255_255_255.txt'):
            with open("./module_0_0_0_0_to_0_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_10_0_0_0_to_10_255_255_255(disk=False):
    """
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 16777216
    Expected Size on Disk: 235 MB
    """
    if disk is False:
        return ips('10.0.0.0', '10.255.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_10_0_0_0_to_10_255_255_255.txt'):
            with open("./module_10_0_0_0_to_10_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_100_64_0_0_to_100_127_255_255(disk=False):
    """
    Description: Shared address space for communications between a service provider and
    its subscribers when using a carrier-grade NAT.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 4194304
    Expected Size on Disk: 62.3 MB
    """
    if disk is False:
        return ips('100.64.0.0', '100.127.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_100_64_0_0_to_100_127_255_255.txt'):
            with open("./module_100_64_0_0_to_100_127_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_127_0_0_0_to_127_255_255_255(disk=False):
    """
    Description: Used for loopback addresses to the local host.
    Scope: Host
    Reserved: True
    Expected number of addresses: 16777216
    Expected Size on Disk:
    """
    if disk is False:
        return ips('127.0.0.0', '127.255.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_127_0_0_0_to_127_255_255_255.txt'):
            with open("./module_127_0_0_0_to_127_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_169_254_0_0_to_169_254_255_255(disk=False):
    """
    Description: Used for link-local addresses[5] between two hosts on a
    single link when no IP address is otherwise specified, such
    as would have normally been retrieved from a DHCP server.
    Scope: Subnet
    Reserved: True
    Expected number of addresses: 65536
    Expected Size on Disk:
    """
    if disk is False:
        return ips('169.254.0.0', '169.254.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_169_254_0_0_to_169_254_255_255.txt'):
            with open("./module_169_254_0_0_to_169_254_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_172_16_0_0_to_172_31_255_255(disk=False):
    """
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 1048576
    Expected Size on Disk:
    """
    if disk is False:
        return ips('172.16.0.0', '172.31.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_172_16_0_0_to_172_31_255_255.txt'):
            with open("./module_172_16_0_0_to_172_31_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_0_0_0_to_192_0_0_255(disk=False):
    """
    Description: IETF Protocol Assignments
    Scope: Private network
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if disk is False:
        return ips('192.0.0.0', '192.0.0.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_192_0_0_0_to_192_0_0_255.txt'):
            with open("./module_192_0_0_0_to_192_0_0_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_0_2_0_to_192_0_2_255(disk=False):
    """
    Description: Assigned as TEST-NET-1
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if disk is False:
        return ips('192.0.2.0', '192.0.2.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_192_0_2_0_to_192_0_2_255.txt'):
            with open("./module_192_0_2_0_to_192_0_2_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_88_99_0_to_192_88_99_255(disk=False):
    """
    Description: Formerly used for IPv6 to IPv4 relay
    (included IPv6 address block 2002::/16).
    Scope: Internet
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if disk is False:
        return ips('192.88.99.0', '192.88.99.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_192_88_99_0_to_192_88_99_255.txt'):
            with open("./module_192_88_99_0_to_192_88_99_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_168_0_0_to_192_168_255_255(disk=False):
    """
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 65536
    Expected Size on Disk:
    """
    if disk is False:
        return ips('192.168.0.0', '192.168.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_192_168_0_0_to_192_168_255_255.txt'):
            with open("./module_192_168_0_0_to_192_168_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_198_18_0_0_to_198_19_255_255(disk=False):
    """
    Description: Used for benchmark testing of inter-network communications
    between two separate subnets
    Scope: Private network
    Reserved: True
    Expected number of addresses: 131072
    Expected Size on Disk:
    """
    if disk is False:
        return ips('198.18.0.0', '198.19.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_198_18_0_0_to_198_19_255_255.txt'):
            with open("./module_198_18_0_0_to_198_19_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_198_51_100_0_to_198_51_100_255(disk=False):
    """
    Description: Assigned as TEST-NET-2, documentation and examples
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if disk is False:
        return ips('198.51.100.0', '198.51.100.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_198_51_100_0_to_198_51_100_255.txt'):
            with open("./module_198_51_100_0_to_198_51_100_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_203_0_113_0_to_203_0_113_255(disk=False):
    """
    Description: Assigned as TEST-NET-3, documentation and examples
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if disk is False:
        return ips('203.0.113.0', '203.0.113.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_203_0_113_0_to_203_0_113_255.txt'):
            with open("./module_203_0_113_0_to_203_0_113_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_224_0_0_0_to_239_255_255_255(disk=False):
    """
    Description: In use for IP multicast. (Former Class D network.)
    Scope: Internet
    Reserved: True
    Expected number of addresses: 268435456
    Expected Size on Disk:
    """
    if disk is False:
        return ips('224.0.0.0', '239.255.255.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_224_0_0_0_to_239_255_255_255.txt'):
            with open("./module_224_0_0_0_to_239_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_233_252_0_0_to_233_252_0_255(disk=False):
    """
    Description: Assigned as MCAST-TEST-NET, documentation and examples.
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if disk is False:
        return ips('233.252.0.0', '233.252.0.255')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_233_252_0_0_to_233_252_0_255.txt'):
            with open("./module_233_252_0_0_to_233_252_0_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_240_0_0_0_to_255_255_255_254(disk=False):
    """
    Description: Reserved for future use. (Former Class E network.)
    Scope: Internet
    Reserved: True
    Expected number of addresses: 268435455
    Expected Size on Disk:
    """
    if disk is False:
        return ips('240.0.0.0', '255.255.255.254')
    elif disk is True:
        _ips = []
        if os.path.exists('./module_240_0_0_0_to_255_255_255_254.txt'):
            with open("./module_240_0_0_0_to_255_255_255_254.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_255_255_255_255(disk=False):
    """
    Description: Reserved for the "limited broadcast" destination address
    Scope: Subnet
    Reserved: True
    Expected number of addresses: 1
    Expected Size on Disk:
    """
    if disk is False:
        return '255.255.255.255'
    elif disk is True:
        _ips = []
        if os.path.exists('./module_255_255_255_255.txt'):
            with open("./module_255_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips
