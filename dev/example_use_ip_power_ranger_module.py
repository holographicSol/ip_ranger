""" Written by Benjamin Jack Cullen

IPv4 Range Enumerator

"""
import time

import module_ip_power_ranger
import socket
import struct


def seperator():
    print('-'*50)


def example_list_public_ipv4_ranges():
    """ Return a specific list of IPv4 address ranges"""
    seperator()
    public_ips = module_ip_power_ranger.provide_public_ranges()
    print('[PUBLIC IPv4 RANGES]')
    print(public_ips)


example_list_public_ipv4_ranges()


def example_iterate_over_ipv4_addresses_in_x_range():
    """ step over each ipv4 address in x address block """
    seperator()
    print('[example_iterate_over_ipv4_addresses_in_x_range]')
    provide_private_ranges = module_ip_power_ranger.provide_private_ranges()
    index_0 = struct.unpack('>I', socket.inet_aton(provide_private_ranges[0][0]))[0]
    index_1 = struct.unpack('>I', socket.inet_aton(provide_private_ranges[0][1]))[0]
    i = 0
    print('stepping over range:', provide_private_ranges[-3])
    for n in range(index_0, index_1):
        x = module_ip_power_ranger.iter_ips(index=n)
        n += 1
        i += 1
    print('ips:', i)


example_iterate_over_ipv4_addresses_in_x_range()


def example_iterate_over_ipv4_addresses_in_each_private_range():
    """
    step over each address in each address range specified
    """
    seperator()
    print('[example_iterate_over_ipv4_addresses_in_each_private_range]')
    private_ip_rages = module_ip_power_ranger.provide_private_ranges()
    ip_i_total = 0
    for i in range(0, len(private_ip_rages)):
        print('-'*50)
        index_0 = struct.unpack('>I', socket.inet_aton(private_ip_rages[i][0]))[0]
        index_1 = struct.unpack('>I', socket.inet_aton(private_ip_rages[i][1]))[0]
        print('stepping over range:', private_ip_rages[i])
        ip_i = 1
        for n in range(index_0, index_1):
            n += 1
            ip_i += 1
        print('ips in range:', ip_i)
        ip_i_total += ip_i
    print('-' * 50)
    print('ip_i_total private:', ip_i_total)


example_iterate_over_ipv4_addresses_in_each_private_range()


def example_iterate_over_ipv4_addresses_in_each_public_range():
    """ step over each address in each address range specified """
    seperator()
    print('[example_iterate_over_ipv4_addresses_in_each_public_range]')
    public_ip_rages = module_ip_power_ranger.provide_public_ranges()
    ip_i_total = 0
    for i in range(0, len(public_ip_rages)):
        print('-'*50)
        index_0 = struct.unpack('>I', socket.inet_aton(public_ip_rages[i][0]))[0]
        index_1 = struct.unpack('>I', socket.inet_aton(public_ip_rages[i][1]))[0]
        print('stepping over range:', public_ip_rages[i])
        ip_i = 1
        for n in range(index_0, index_1):
            n += 1
            ip_i += 1
        print('ips in range:', ip_i)
        ip_i_total += ip_i
    print('-' * 50)
    print('ip_i_total public:', ip_i_total)


example_iterate_over_ipv4_addresses_in_each_public_range()


def example_iterate_over_ipv4_addresses_in_each_private_range_and_count_public():
    """ step over each address in each address range specified and cross-examine (developer proof)
    """
    seperator()
    print('[example_iterate_over_ipv4_addresses_in_each_private_range_and_count_public] (should be 0)')
    private_ip_rages = module_ip_power_ranger.provide_private_ranges()
    ip_true_in_public = 0
    for i in range(0, len(private_ip_rages)):
        print('-'*50)
        index_0 = struct.unpack('>I', socket.inet_aton(private_ip_rages[i][0]))[0]
        index_1 = struct.unpack('>I', socket.inet_aton(private_ip_rages[i][1]))[0]
        print('stepping over range:', private_ip_rages[i])
        for n in range(index_0, index_1):
            n += 1

            if module_ip_power_ranger.is_ip_index_public(index=n) is True:
                ip_true_in_public += 1
        print('total public IPv4 addresses found across every range scanned so far:', ip_true_in_public)

    print('-' * 50)
    print('total public IPv4 addresses found across every range scanned:', ip_true_in_public)


example_iterate_over_ipv4_addresses_in_each_private_range_and_count_public()


def example_iterate_over_ipv4_addresses_in_each_public_range_and_count_private():
    """ step over each address in each address range specified and cross-examine (developer proof)
    """
    seperator()
    print('[example_iterate_over_ipv4_addresses_in_each_public_range_and_count_private] (should be 0)')
    public_ip_ranges = module_ip_power_ranger.provide_public_ranges()
    ip_true_in_private = 0
    for i in range(0, len(public_ip_ranges)):
        print('-'*50)
        index_0 = struct.unpack('>I', socket.inet_aton(public_ip_ranges[i][0]))[0]
        index_1 = struct.unpack('>I', socket.inet_aton(public_ip_ranges[i][1]))[0]
        print('stepping over range:', public_ip_ranges[i])
        for n in range(index_0, index_1):
            n += 1
            if module_ip_power_ranger.is_ip_index_private(index=n) is True:
                ip_true_in_private += 1
        print('total private IPv4 addresses found across every range scanned so far:', ip_true_in_private)

    print('-' * 50)
    print('total private IPv4 addresses found across every range scanned:', ip_true_in_private)


example_iterate_over_ipv4_addresses_in_each_public_range_and_count_private()
