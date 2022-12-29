""" Written by Benjamin Jack Cullen

IPv4 Range Enumerator

"""
import time
import datetime
import socket
import struct
import module_ip_power_ranger


def dt():
    dt = '[' + str(datetime.datetime.now()) + ']'
    return dt


def program_x_function_0():
    """ step over each address in each address range specified """

    public_ip_rages = module_ip_power_ranger.provide_public_ranges()
    total_public = module_ip_power_ranger.total_public_ipv4_addresses()
    total_current_public_ranges = len(public_ip_rages)
    ip_i_total = 1
    for i in range(6, total_current_public_ranges):
        print('-'*150)
        index_0 = struct.unpack('>I', socket.inet_aton(public_ip_rages[i][0]))[0]
        index_1 = struct.unpack('>I', socket.inet_aton(public_ip_rages[i][1]))[0]
        print(dt() + ' stepping over range:', str(public_ip_rages[i]))
        ip_i = 1
        ip_i_total_in_range = public_ip_rages[i][2]
        for n in range(index_0, index_1):
            print('-' * 150)
            prc_total = float(float(int(100) * float((float(ip_i_total) / total_public))) * 1)
            prc_ip_range = float(float(int(100) * float((float(ip_i) / ip_i_total_in_range))) * 1)
            prc_total_range = float(float(int(100) * float((float(i) / total_current_public_ranges))) * 1)
            print(dt() + ' Current IPv4 target address range:', public_ip_rages[i])
            print(dt() + ' IPv4 address in total ranges:', str(ip_i_total), '/', str(total_public), ' ', str(round(prc_total, 3)), '% ')
            print(dt() + ' IPv4 address in current range:', str(ip_i), '/', str(ip_i_total_in_range), ' ', str(round(prc_ip_range, 3)), '% ')
            print(dt() + ' IPv4 address range:', str(i), '/', str(total_current_public_ranges), ' ', str(round(prc_total_range, 3)), '% ')
            x = module_ip_power_ranger.iter_ips(index=n)
            print(dt() + ' Targeting IPv4 address:', str(x))
            print(dt() + ' IPv4 address Public check:', str(module_ip_power_ranger.is_ip_index_public(x)))
            n += 1
            ip_i += 1
            time.sleep(1)
            ip_i_total += 1
    print('-' * 150)
    print(dt() + ' complete.')


program_x_function_0()
