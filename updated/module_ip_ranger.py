""" Written by Benjamin Jack Cullen

Note: * Modules module_0_0_0_0_to_0_255_255_255 --> module_255_255_255_255 are not needed to run this module.
      * Importing modules module_0_0_0_0_to_0_255_255_255 --> module_255_255_255_255 is
        only faster when program x (that imports this module) is compiled.
      * Any module from module_0_0_0_0_to_0_255_255_255 --> module_255_255_255_255 will be imported
        if exists in THIS module working directory OR in PATH.
      * Place only module module_0_0_0_0_to_0_255_255_255 --> module_255_255_255_255 that are required into
        THIS module directory.
      * Otherwise use enumeration mode or read mode (requires no module module_0_0_0_0_to_0_255_255_255
        --> module_255_255_255_255) (But slower when compiled).
      * Best performance: A compiled program 'x' that imports this module with
        each module module_0_0_0_0_to_0_255_255_255 --> module_255_255_255_255.

"""

import os
import socket
import struct

try:
    import module_0_0_0_0_to_0_255_255_255
except:
    pass

try:
    import module_10_0_0_0_to_10_255_255_255
except:
    pass

try:
    import module_100_64_0_0_to_100_127_255_255
except:
    pass

try:
    import module_127_0_0_0_to_127_255_255_255
except:
    pass

try:
    import module_169_254_0_0_to_169_254_255_255
except:
    pass

try:
    import module_172_16_0_0_to_172_31_255_255
except:
    pass

try:
    import module_192_0_0_0_to_192_0_0_255
except:
    pass

try:
    import module_192_0_2_0_to_192_0_2_255
except:
    pass

try:
    import module_192_88_99_0_to_192_88_99_255
except:
    pass

try:
    import module_192_168_0_0_to_192_168_255_255
except:
    pass

try:
    import module_198_18_0_0_to_198_19_255_255
except:
    pass

try:
    import module_198_51_100_0_to_198_51_100_255
except:
    pass

try:
    import module_203_0_113_0_to_203_0_113_255
except:
    pass

try:
    import module_224_0_0_0_to_239_255_255_255
except:
    pass

try:
    import module_233_252_0_0_to_233_252_0_255
except:
    pass

try:
    import module_240_0_0_0_to_255_255_255_254
except:
    pass

try:
    import module_255_255_255_255
except:
    pass


def ips(start, end):
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def compile_0_0_0_0_to_0_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Current network.
    Scope: Software
    Reserved: True
    Expected number of addresses: 16777216
    Expected Size on Disk: 219 MB
    """
    if mode == 'module':
        return module_0_0_0_0_to_0_255_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('0.0.0.0', '0.255.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_0_0_0_0_to_0_255_255_255.txt'):
            with open("./module_0_0_0_0_to_0_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_10_0_0_0_to_10_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 16777216
    Expected Size on Disk: 235 MB
    """
    if mode == 'module':
        return module_10_0_0_0_to_10_255_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('10.0.0.0', '10.255.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_10_0_0_0_to_10_255_255_255.txt'):
            with open("./module_10_0_0_0_to_10_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_100_64_0_0_to_100_127_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Shared address space for communications between a service provider and
    its subscribers when using a carrier-grade NAT.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 4194304
    Expected Size on Disk: 62.3 MB
    """
    if mode == 'module':
        return module_100_64_0_0_to_100_127_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('100.64.0.0', '100.127.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_100_64_0_0_to_100_127_255_255.txt'):
            with open("./module_100_64_0_0_to_100_127_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_127_0_0_0_to_127_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Used for loopback addresses to the local host.
    Scope: Host
    Reserved: True
    Expected number of addresses: 16777216
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_127_0_0_0_to_127_255_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('127.0.0.0', '127.255.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_127_0_0_0_to_127_255_255_255.txt'):
            with open("./module_127_0_0_0_to_127_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_169_254_0_0_to_169_254_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Used for link-local addresses[5] between two hosts on a
    single link when no IP address is otherwise specified, such
    as would have normally been retrieved from a DHCP server.
    Scope: Subnet
    Reserved: True
    Expected number of addresses: 65536
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_169_254_0_0_to_169_254_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('169.254.0.0', '169.254.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_169_254_0_0_to_169_254_255_255.txt'):
            with open("./module_169_254_0_0_to_169_254_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_172_16_0_0_to_172_31_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 1048576
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_172_16_0_0_to_172_31_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('172.16.0.0', '172.31.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_172_16_0_0_to_172_31_255_255.txt'):
            with open("./module_172_16_0_0_to_172_31_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_0_0_0_to_192_0_0_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: IETF Protocol Assignments
    Scope: Private network
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_192_0_0_0_to_192_0_0_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('192.0.0.0', '192.0.0.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_192_0_0_0_to_192_0_0_255.txt'):
            with open("./module_192_0_0_0_to_192_0_0_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_0_2_0_to_192_0_2_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Assigned as TEST-NET-1
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_192_0_2_0_to_192_0_2_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('192.0.2.0', '192.0.2.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_192_0_2_0_to_192_0_2_255.txt'):
            with open("./module_192_0_2_0_to_192_0_2_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_88_99_0_to_192_88_99_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Formerly used for IPv6 to IPv4 relay
    (included IPv6 address block 2002::/16).
    Scope: Internet
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_192_88_99_0_to_192_88_99_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('192.88.99.0', '192.88.99.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_192_88_99_0_to_192_88_99_255.txt'):
            with open("./module_192_88_99_0_to_192_88_99_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_192_168_0_0_to_192_168_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Used for local communications within a private network.
    Scope: Private network
    Reserved: True
    Expected number of addresses: 65536
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_192_168_0_0_to_192_168_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('192.168.0.0', '192.168.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_192_168_0_0_to_192_168_255_255.txt'):
            with open("./module_192_168_0_0_to_192_168_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_198_18_0_0_to_198_19_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Used for benchmark testing of inter-network communications
    between two separate subnets
    Scope: Private network
    Reserved: True
    Expected number of addresses: 131072
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_198_18_0_0_to_198_19_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('198.18.0.0', '198.19.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_198_18_0_0_to_198_19_255_255.txt'):
            with open("./module_198_18_0_0_to_198_19_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_198_51_100_0_to_198_51_100_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Assigned as TEST-NET-2, documentation and examples
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_198_51_100_0_to_198_51_100_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('198.51.100.0', '198.51.100.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_198_51_100_0_to_198_51_100_255.txt'):
            with open("./module_198_51_100_0_to_198_51_100_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_203_0_113_0_to_203_0_113_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Assigned as TEST-NET-3, documentation and examples
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_203_0_113_0_to_203_0_113_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('203.0.113.0', '203.0.113.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_203_0_113_0_to_203_0_113_255.txt'):
            with open("./module_203_0_113_0_to_203_0_113_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_224_0_0_0_to_239_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: In use for IP multicast. (Former Class D network.)
    Scope: Internet
    Reserved: True
    Expected number of addresses: 268435456
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_224_0_0_0_to_239_255_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('224.0.0.0', '239.255.255.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_224_0_0_0_to_239_255_255_255.txt'):
            with open("./module_224_0_0_0_to_239_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_233_252_0_0_to_233_252_0_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Assigned as MCAST-TEST-NET, documentation and examples.
    Scope: Documentation
    Reserved: True
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_233_252_0_0_to_233_252_0_255.reserved_ipv4
    elif mode == 'enumeration':
        return ips('233.252.0.0', '233.252.0.255')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_233_252_0_0_to_233_252_0_255.txt'):
            with open("./module_233_252_0_0_to_233_252_0_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_240_0_0_0_to_255_255_255_254(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Reserved for future use. (Former Class E network.)
    Scope: Internet
    Reserved: True
    Expected number of addresses: 268435455
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_240_0_0_0_to_255_255_255_254.reserved_ipv4
    elif mode == 'enumeration':
        return ips('240.0.0.0', '255.255.255.254')
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_240_0_0_0_to_255_255_255_254.txt'):
            with open("./module_240_0_0_0_to_255_255_255_254.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips


def compile_255_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description: Reserved for the "limited broadcast" destination address
    Scope: Subnet
    Reserved: True
    Expected number of addresses: 1
    Expected Size on Disk:
    """
    if mode == 'module':
        return module_255_255_255_255.reserved_ipv4
    elif mode == 'enumeration':
        return '255.255.255.255'
    elif mode == 'read':
        _ips = []
        if os.path.exists('./module_255_255_255_255.txt'):
            with open("./module_255_255_255_255.txt", "r") as fo:
                for line in fo:
                    line = line.strip()
                    _ips.append(line)
            fo.close()
            return _ips
