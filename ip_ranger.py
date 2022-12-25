""" Written by Benjamin Jack Cullen

IP Ranger

This program creates human lists of IPv4 address ranges and writes them to files.

"""

import os
import module_ip_ranger
import pyprogress

multiplier = pyprogress.multiplier_from_inverse_factor(factor=25)

f = {'./module_0_0_0_0_to_0_255_255_255.txt': module_ip_ranger.compile_0_0_0_0_to_0_255_255_255,
     './module_10_0_0_0_to_10_255_255_255.txt': module_ip_ranger.compile_10_0_0_0_to_10_255_255_255,
     './module_100_64_0_0_to_100_127_255_255.txt': module_ip_ranger.compile_100_64_0_0_to_100_127_255_255,
     './module_127_0_0_0_to_127_255_255_255.txt': module_ip_ranger.compile_127_0_0_0_to_127_255_255_255,
     './module_169_254_0_0_to_169_254_255_255.txt': module_ip_ranger.compile_169_254_0_0_to_169_254_255_255,
     './module_172_16_0_0_to_172_31_255_255.txt': module_ip_ranger.compile_172_16_0_0_to_172_31_255_255,
     './module_192_0_0_0_to_192_0_0_255.txt': module_ip_ranger.compile_192_0_0_0_to_192_0_0_255,
     './module_192_0_2_0_to_192_0_2_255.txt': module_ip_ranger.compile_192_0_2_0_to_192_0_2_255,
     './module_192_88_99_0_to_192_88_99_255.txt': module_ip_ranger.compile_192_88_99_0_to_192_88_99_255,
     './module_192_168_0_0_to_192_168_255_255.txt': module_ip_ranger.compile_192_168_0_0_to_192_168_255_255,
     './module_198_18_0_0_to_198_19_255_255.txt': module_ip_ranger.compile_198_18_0_0_to_198_19_255_255,
     './module_198_51_100_0_to_198_51_100_255.txt': module_ip_ranger.compile_198_51_100_0_to_198_51_100_255,
     './module_203_0_113_0_to_203_0_113_255.txt': module_ip_ranger.compile_203_0_113_0_to_203_0_113_255,
     './module_224_0_0_0_to_239_255_255_255.txt': module_ip_ranger.compile_224_0_0_0_to_239_255_255_255,
     './module_233_252_0_0_to_233_252_0_255.txt': module_ip_ranger.compile_233_252_0_0_to_233_252_0_255,
     './module_240_0_0_0_to_255_255_255_254.txt': module_ip_ranger.compile_240_0_0_0_to_255_255_255_254,
     './module_255_255_255_255.txt': module_ip_ranger.compile_255_255_255_255}


def display_header():
    print('')
    print('-'*100)
    print('[IP RANGER - MODULE CREATOR]')
    print('')


def warn_user(file=str):
    allow_write = False
    if os.path.exists(file):
        print('[WARNING] This operation will overwrite:', file)
        user_input = input('continue? ')
        print('')
        if user_input == 'y' or user_input == 'Y':
            allow_write = True
    else:
        allow_write = True
    return allow_write


def display_progress(i_x, data_enum_len, pre_append):
    pyprogress.progress_bar(part=int(i_x), whole=int(data_enum_len),
                            pre_append=pre_append,
                            append=str(' ' + str(i_x) + ' / ' + str(data_enum_len)),
                            encapsulate_l='|',
                            encapsulate_r='|',
                            encapsulate_l_color='LIGHTCYAN_EX',
                            encapsulate_r_color='LIGHTCYAN_EX',
                            progress_char=' ',
                            bg_color='LIGHTCYAN_EX',
                            factor=25,
                            multiplier=multiplier)


def ip_ranges_compiler(file=str, data_enum=[], loop=True):
    display_header()
    print('[FILE] ', file)
    if warn_user(file=file) is True:
        open(file, 'w').close()
        pre_append = '[WRITING] '
        print('')
        i_x = 0
        if loop is True:
            data_enum_len = len(data_enum)
            print('[WRITING]', data_enum_len, 'items to file.')
            for _ in data_enum:
                with open(file, 'a') as fo:
                    fo.write(_+'\n')
                fo.close()
                i_x += 1
                display_progress(i_x, data_enum_len, pre_append)
        else:
            data_enum_len = 1
            with open(file, 'a') as fo:
                fo.write(str(data_enum) + '\n')
            fo.close()
            i_x += 1
            display_progress(i_x, data_enum_len, pre_append)
    print('\n[COMPLETED]\n')


def compile_all_reserved_ip_ranges():
    print('[WARNING] This requires a lot of disk space!')
    user_input = input('continue? ')
    if user_input == 'y' or user_input == 'Y':
        i = 0
        for k in f:
            print('')
            print('-' * 100)
            print('[IP RANGER - MODULE CREATOR]')
            print('')
            print('[FILE] Attempting to create:', k, 'with associated function:', f[k])
            print('[ENUMERATING] This may take a moment...')
            data_enum = f[k]()
            print('[ENUMERATING] Completed.')
            ip_ranges_compiler(file=k, data_enum=data_enum)
            i += 1
    else:
        print('Aborting!')
        print('')
        print('-'*100)


def validator(file=str, data_enum=[]):
    module_data = []
    if os.path.exists(file):
        print('[VALIDATION] File exists: PASSED')
        with open(file, 'r') as fo:
            for line in fo:
                line = line.strip()
                module_data.append(line)
        fo.close()
        if len(data_enum) == len(module_data):
            print('[VALIDATION] List length check: PASSED')
            validation = []
            i = 0
            for _ in data_enum:
                if _ == module_data[i]:
                    validation.append(True)
                else:
                    validation.append(False)
                i += 1
            if False in validation:
                print('[VALIDATION] List comparison check: FAILED')
                print('[VALIDATION] FAILED')
                print('[SUMMARY] Re-write: necessary')
            else:
                print('[VALIDATION] List comparison check: PASSED')
                print('[VALIDATION] PASSED')
                print('[SUMMARY] Re-write: unnecessary')
        else:
            print('[VALIDATION] List length check: FAILED')
            print('[VALIDATION] FAILED')
            print('[SUMMARY] Re-write: necessary')
    else:
        print('[VALIDATION] File exists: FAILED')
        print('[VALIDATION] FAILED')
        print('[SUMMARY] Re-write: necessary')


def validate():
    for k in f:
        print('')
        print('-' * 100)
        print('[IP RANGER - MODULE VALIDATOR]')
        print('')
        print('[VALIDATING] Attempting to validate:', k, 'with associated function:', f[k])
        print('[ENUMERATING] This may take a moment...')
        data_enum = f[k]()
        print('[ENUMERATING] Completed.')
        validator(file=k, data_enum=data_enum)


while True:
    print('')
    print('-'*100)
    print(' [IP RANGER]')
    print('')
    print(' [DESCRIPTION]')
    print('     This program intends to create files of IPv4 ranges that can be used for speed ranging.')
    print('')
    print(' [1] VALIDATOR  (attempts to verify IPv4 range files)')
    print(' [2] CREATOR    (creates all currently supported IPv4 range files)')
    print('')
    print(' [3]  CREATE SPECIFIC RANGE: 0.0.0.0       to  0.255.255.255     ')
    print(' [4]  CREATE SPECIFIC RANGE: 10.0.0.0      to  10.255.255.255    ')
    print(' [5]  CREATE SPECIFIC RANGE: 100.64.0.0    to  100.127.255.255   ')
    print(' [6]  CREATE SPECIFIC RANGE: 127.0.0.0     to  127.255.255.255   ')
    print(' [7]  CREATE SPECIFIC RANGE: 169.254.0.0   to  169.254.255.255   ')
    print(' [8]  CREATE SPECIFIC RANGE: 172.16.0.0    to  172.31.255.255    ')
    print(' [9]  CREATE SPECIFIC RANGE: 192.0.0.0     to  192.0.0.255       ')
    print(' [10] CREATE SPECIFIC RANGE: 192.0.2.0     to  192.0.2.255       ')
    print(' [11] CREATE SPECIFIC RANGE: 192.88.99.0   to  192.88.99.255     ')
    print(' [12] CREATE SPECIFIC RANGE: 192.168.0.0   to  192.168.255.255   ')
    print(' [13] CREATE SPECIFIC RANGE: 198.18.0.0    to  198.19.255.255    ')
    print(' [14] CREATE SPECIFIC RANGE: 198.51.100.0  to  198.51.100.255    ')
    print(' [15] CREATE SPECIFIC RANGE: 203.0.113.0   to  203.0.113.255     ')
    print(' [16] CREATE SPECIFIC RANGE: 224.0.0.0     to  239.255.255.255   ')
    print(' [17] CREATE SPECIFIC RANGE: 233.252.0.0   to  233.252.0.255     ')
    print(' [18] CREATE SPECIFIC RANGE: 240.0.0.0     to  255.255.255.254   ')
    print(' [19] CREATE SPECIFIC RANGE: 255.255.255.255                     ')
    print('')
    print(' [Q]  QUIT')
    print('')
    user_input = input('select: ')

    if user_input == 'q' or user_input == 'Q':
        print('')
        print('[QUITTING]')
        print('')
        print('-'*100)
        print('')
        break

    elif user_input == "1":
        validate()
    elif user_input == "2":
        compile_all_reserved_ip_ranges()
    elif user_input == "3":
        ip_ranges_compiler(file='./module_0_0_0_0_to_0_255_255_255.txt',
                           data_enum=f['./module_0_0_0_0_to_0_255_255_255.txt']())
    elif user_input == "4":
        ip_ranges_compiler(file='./module_10_0_0_0_to_10_255_255_255.txt',
                           data_enum=f['./module_10_0_0_0_to_10_255_255_255.txt']())
    elif user_input == "5":
        ip_ranges_compiler(file='./module_100_64_0_0_to_100_127_255_255.txt',
                           data_enum=f['./module_100_64_0_0_to_100_127_255_255.txt']())
    elif user_input == "6":
        ip_ranges_compiler(file='./module_127_0_0_0_to_127_255_255_255.txt',
                           data_enum=f['./module_127_0_0_0_to_127_255_255_255.txt']())
    elif user_input == "7":
        ip_ranges_compiler(file='./module_169_254_0_0_to_169_254_255_255.txt',
                           data_enum=f['./module_169_254_0_0_to_169_254_255_255.txt']())
    elif user_input == "8":
        ip_ranges_compiler(file='./module_172_16_0_0_to_172_31_255_255.txt',
                           data_enum=f['./module_172_16_0_0_to_172_31_255_255.txt']())
    elif user_input == "9":
        ip_ranges_compiler(file='./module_192_0_0_0_to_192_0_0_255.txt',
                           data_enum=f['./module_192_0_0_0_to_192_0_0_255.txt']())
    elif user_input == "10":
        ip_ranges_compiler(file='./module_192_0_2_0_to_192_0_2_255.txt',
                           data_enum=f['./module_192_0_2_0_to_192_0_2_255.txt']())
    elif user_input == "11":
        ip_ranges_compiler(file='./module_192_88_99_0_to_192_88_99_255.txt',
                           data_enum=f['./module_192_88_99_0_to_192_88_99_255.txt']())
    elif user_input == "12":
        ip_ranges_compiler(file='./module_192_168_0_0_to_192_168_255_255.txt',
                           data_enum=f['./module_192_168_0_0_to_192_168_255_255.txt']())
    elif user_input == "13":
        ip_ranges_compiler(file='./module_198_18_0_0_to_198_19_255_255.txt',
                           data_enum=f['./module_198_18_0_0_to_198_19_255_255.txt']())
    elif user_input == "14":
        ip_ranges_compiler(file='./module_198_51_100_0_to_198_51_100_255.txt',
                           data_enum=f['./module_198_51_100_0_to_198_51_100_255.txt']())
    elif user_input == "15":
        ip_ranges_compiler(file='./module_203_0_113_0_to_203_0_113_255.txt',
                           data_enum=f['./module_203_0_113_0_to_203_0_113_255.txt']())
    elif user_input == "16":
        ip_ranges_compiler(file='./module_224_0_0_0_to_239_255_255_255.txt',
                           data_enum=f['./module_224_0_0_0_to_239_255_255_255.txt']())
    elif user_input == "17":
        ip_ranges_compiler(file='./module_233_252_0_0_to_233_252_0_255.txt',
                           data_enum=f['./module_233_252_0_0_to_233_252_0_255.txt']())
    elif user_input == "18":
        ip_ranges_compiler(file='./module_240_0_0_0_to_255_255_255_254.txt',
                           data_enum=f['./module_240_0_0_0_to_255_255_255_254.txt']())
    elif user_input == "19":
        ip_ranges_compiler(file='./module_255_255_255_255.txt', data_enum=f['./module_255_255_255_255.txt'](), loop=False)

