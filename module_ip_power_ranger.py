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
"""

import os
import socket
import struct


def iter_ips(index=int):
    return socket.inet_ntoa(struct.pack('>I', index))


def ips(start, end):
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def ips_pythonic_list_file_format(start, end):
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    _python_list = [str('    "') + str(socket.inet_ntoa(struct.pack('>I', i))) + str('",') for i in range(start, end+1)]
    _python_list.insert(0, 'reserved_ipv4 = [')
    _python_list[-1] = _python_list[-1].replace(',', ']\n')
    return _python_list


def is_ip_index_public(index=int):
    """
    Takes index integer as ip argument.
    Example: print(module_ip_power_ranger.is_ip_public(16777216))
    """
    for _ in provide_public_ranges():
        start = struct.unpack('>I', socket.inet_aton(_[0]))[0]
        end = struct.unpack('>I', socket.inet_aton(_[1]))[0]
        if index in range(start, end):
            return True
        else:
            return False


def provide_public_ranges():
    return [
        ['1.0.0.0', '9.255.255.255'],
        ['11.0.0.0', '100.63.255.255'],
        ['100.128.0.0', '126.255.255.255'],
        ['128.0.0.0', '169.253.255.255'],
        ['169.255.255.255', '172.15.255.255'],
        ['172.32.0.0', '191.255.255.255'],
        ['192.0.1.0', '192.0.1.255'],
        ['192.0.3.0', '192.88.98.255'],
        ['192.88.100.0', '192.167.255.255'],
        ['192.169.0.0', '198.17.255.255'],
        ['198.20.0.0', '198.51.99.255'],
        ['198.51.101.0', '203.0.112.255'],
        ['203.0.114.0', '223.255.255.255']
    ]


def provide_private_ranges():
    return [
        ['0.0.0.0', '0.255.255.255'],
        ['10.0.0.0', '10.255.255.255'],
        ['100.64.0.0', '100.127.255.255'],
        ['127.0.0.0', '127.255.255.255'],
        ['169.254.0.0', '169.254.255.255'],
        ['172.16.0.0', '172.31.255.255'],
        ['192.0.0.0', '192.0.0.255'],
        ['192.0.2.0', '192.0.2.255'],
        ['192.88.99.0', '192.88.99.255'],
        ['192.168.0.0', '192.168.255.255'],
        ['198.18.0.0', '198.19.255.255'],
        ['198.51.100.0', '198.51.100.255'],
        ['203.0.113.0', '203.0.113.255'],
        ['224.0.0.0', '239.255.255.255'],
        ['233.252.0.0', '233.252.0.255'],
        ['240.0.0.0', '255.255.255.254'],
        ['255.255.255.255']
    ]


def compile_1_0_0_0_to_9_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 150,994,944
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('1.0.0.0', '9.255.255.255')


def compile_11_0_0_0_to_100_63_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses:
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('11.0.0.0', '100.63.255.255')


def compile_100_128_0_0_to_126_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 444,596,224
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('100.128.0.0', '126.255.255.255')


def compile_128_0_0_0_to_169_253_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 704,512,000
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('128.0.0.0', '169.253.255.255')


def compile_169_255_255_255_to_172_15_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 34,603,009
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('169.255.255.255', '172.15.255.255')


def compile_172_32_0_0_to_191_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 333,447,168
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('172.32.0.0', '191.255.255.255')


def compile_192_0_1_0_to_192_0_1_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 256
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('192.0.1.0', '192.0.1.255')


def compile_192_0_3_0_to_192_88_98_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 5,791,744
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('192.0.3.0', '192.88.98.255')


def compile_192_88_100_0_to_192_167_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 5,217,280
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('192.88.100.0', '192.167.255.255')


def compile_192_169_0_0_to_198_17_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 90,767,360
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('192.169.0.0', '198.17.255.255')


def compile_198_20_0_0_to_198_51_99_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 2,057,216
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('198.20.0.0', '198.51.99.255')


def compile_198_51_101_0_to_203_0_112_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 80,546,816
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('198.51.101.0', '203.0.112.255')


def compile_203_0_114_0_to_223_255_255_255(mode='enumeration'):
    """
    Options:
        (mode = str) Default mode='enumeration'
        mode='module'
        mode='enumeration'
        mode='read'
    Description:
    Scope:
    Reserved:
    Expected number of addresses: 352,292,352
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('203.0.114.0', '223.255.255.255')


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
    Expected number of addresses: 16,777,216
    Expected Size on Disk: 219 MB
    """
    if mode == 'enumeration':
        return ips('0.0.0.0', '0.255.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('0.0.0.0', '0.255.255.255')
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
    Expected number of addresses: 16,777,216
    Expected Size on Disk: 235 MB
    """
    if mode == 'enumeration':
        return ips('10.0.0.0', '10.255.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('10.0.0.0', '10.255.255.255')
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
    Expected number of addresses: 4,194,304
    Expected Size on Disk: 62.3 MB
    """
    if mode == 'enumeration':
        return ips('100.64.0.0', '100.127.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('100.64.0.0', '100.127.255.255')
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
    Expected number of addresses: 16,777,216
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('127.0.0.0', '127.255.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('127.0.0.0', '127.255.255.255')
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
    Expected number of addresses: 65,536
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('169.254.0.0', '169.254.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('169.254.0.0', '169.254.255.255')
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
    Expected number of addresses: 1,048,576
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('172.16.0.0', '172.31.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('172.16.0.0', '172.31.255.255')
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
    if mode == 'enumeration':
        return ips('192.0.0.0', '192.0.0.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('192.0.0.0', '192.0.0.255')
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
    if mode == 'enumeration':
        return ips('192.0.2.0', '192.0.2.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('192.0.2.0', '192.0.2.255')
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
    if mode == 'enumeration':
        return ips('192.88.99.0', '192.88.99.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('192.88.99.0', '192.88.99.255')
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
    Expected number of addresses: 65,536
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('192.168.0.0', '192.168.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('192.168.0.0', '192.168.255.255')
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
    Expected number of addresses: 131,072
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('198.18.0.0', '198.19.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('198.18.0.0', '198.19.255.255')
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
    if mode == 'enumeration':
        return ips('198.51.100.0', '198.51.100.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('198.51.100.0', '198.51.100.255')
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
    if mode == 'enumeration':
        return ips('203.0.113.0', '203.0.113.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('203.0.113.0', '203.0.113.255')
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
    Expected number of addresses: 268,435,456
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('224.0.0.0', '239.255.255.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('224.0.0.0', '239.255.255.255')
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
    if mode == 'enumeration':
        return ips('233.252.0.0', '233.252.0.255')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('233.252.0.0', '233.252.0.255')
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
    Expected number of addresses: 268,435,455
    Expected Size on Disk:
    """
    if mode == 'enumeration':
        return ips('240.0.0.0', '255.255.255.254')
    elif mode == 'enumeration_for_python_module_file':
        return ips_pythonic_list_file_format('240.0.0.0', '255.255.255.254')
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

    return '255.255.255.255'
