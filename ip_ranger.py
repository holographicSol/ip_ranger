""" Written by Benjamin Jack Cullen

IP Ranger

This program creates human lists of IPv4 address ranges and writes them to files.

"""

import os
import module_ip_ranger
import pyprogress

multiplier = pyprogress.multiplier_from_inverse_factor(factor=25)

f = {'./modules-standard/module_0_0_0_0_to_0_255_255_255.txt': module_ip_ranger.compile_0_0_0_0_to_0_255_255_255,
     './modules-standard/module_10_0_0_0_to_10_255_255_255.txt': module_ip_ranger.compile_10_0_0_0_to_10_255_255_255,
     './modules-standard/module_100_64_0_0_to_100_127_255_255.txt': module_ip_ranger.compile_100_64_0_0_to_100_127_255_255,
     './modules-standard/module_127_0_0_0_to_127_255_255_255.txt': module_ip_ranger.compile_127_0_0_0_to_127_255_255_255,
     './modules-standard/module_169_254_0_0_to_169_254_255_255.txt': module_ip_ranger.compile_169_254_0_0_to_169_254_255_255,
     './modules-standard/module_172_16_0_0_to_172_31_255_255.txt': module_ip_ranger.compile_172_16_0_0_to_172_31_255_255,
     './modules-standard/module_192_0_0_0_to_192_0_0_255.txt': module_ip_ranger.compile_192_0_0_0_to_192_0_0_255,
     './modules-standard/module_192_0_2_0_to_192_0_2_255.txt': module_ip_ranger.compile_192_0_2_0_to_192_0_2_255,
     './modules-standard/module_192_88_99_0_to_192_88_99_255.txt': module_ip_ranger.compile_192_88_99_0_to_192_88_99_255,
     './modules-standard/module_192_168_0_0_to_192_168_255_255.txt': module_ip_ranger.compile_192_168_0_0_to_192_168_255_255,
     './modules-standard/module_198_18_0_0_to_198_19_255_255.txt': module_ip_ranger.compile_198_18_0_0_to_198_19_255_255,
     './modules-standard/module_198_51_100_0_to_198_51_100_255.txt': module_ip_ranger.compile_198_51_100_0_to_198_51_100_255,
     './modules-standard/module_203_0_113_0_to_203_0_113_255.txt': module_ip_ranger.compile_203_0_113_0_to_203_0_113_255,
     './modules-standard/module_224_0_0_0_to_239_255_255_255.txt': module_ip_ranger.compile_224_0_0_0_to_239_255_255_255,
     './modules-standard/module_233_252_0_0_to_233_252_0_255.txt': module_ip_ranger.compile_233_252_0_0_to_233_252_0_255,
     './modules-standard/module_240_0_0_0_to_255_255_255_254.txt': module_ip_ranger.compile_240_0_0_0_to_255_255_255_254,
     './modules-standard/module_255_255_255_255.txt': module_ip_ranger.compile_255_255_255_255}


fp = {'./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py': module_ip_ranger.compile_0_0_0_0_to_0_255_255_255,
     './modules-pythonic/module_10_0_0_0_to_10_255_255_255.txt': module_ip_ranger.compile_10_0_0_0_to_10_255_255_255,
     './modules-pythonic/module_100_64_0_0_to_100_127_255_255.py': module_ip_ranger.compile_100_64_0_0_to_100_127_255_255,
     './modules-pythonic/module_127_0_0_0_to_127_255_255_255.py': module_ip_ranger.compile_127_0_0_0_to_127_255_255_255,
     './modules-pythonic/module_169_254_0_0_to_169_254_255_255.py': module_ip_ranger.compile_169_254_0_0_to_169_254_255_255,
     './modules-pythonic/module_172_16_0_0_to_172_31_255_255.py': module_ip_ranger.compile_172_16_0_0_to_172_31_255_255,
     './modules-pythonic/module_192_0_0_0_to_192_0_0_255.py': module_ip_ranger.compile_192_0_0_0_to_192_0_0_255,
     './modules-pythonic/module_192_0_2_0_to_192_0_2_255.py': module_ip_ranger.compile_192_0_2_0_to_192_0_2_255,
     './modules-pythonic/module_192_88_99_0_to_192_88_99_255.py': module_ip_ranger.compile_192_88_99_0_to_192_88_99_255,
     './modules-pythonic/module_192_168_0_0_to_192_168_255_255.py': module_ip_ranger.compile_192_168_0_0_to_192_168_255_255,
     './modules-pythonic/module_198_18_0_0_to_198_19_255_255.py': module_ip_ranger.compile_198_18_0_0_to_198_19_255_255,
     './modules-pythonic/module_198_51_100_0_to_198_51_100_255.py': module_ip_ranger.compile_198_51_100_0_to_198_51_100_255,
     './modules-pythonic/module_203_0_113_0_to_203_0_113_255.py': module_ip_ranger.compile_203_0_113_0_to_203_0_113_255,
     './modules-pythonic/module_224_0_0_0_to_239_255_255_255.py': module_ip_ranger.compile_224_0_0_0_to_239_255_255_255,
     './modules-pythonic/module_233_252_0_0_to_233_252_0_255.py': module_ip_ranger.compile_233_252_0_0_to_233_252_0_255,
     './modules-pythonic/module_240_0_0_0_to_255_255_255_254.py': module_ip_ranger.compile_240_0_0_0_to_255_255_255_254,
     './modules-pythonic/module_255_255_255_255.py': module_ip_ranger.compile_255_255_255_255}


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
    print('[MODE] STANDARD LIST')
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


def compile_all_reserved_ip_ranges_pythonic():
    print('[MODE] PYTHONIC LIST')
    print('[WARNING] This requires a lot of disk space!')
    user_input = input('continue? ')
    if user_input == 'y' or user_input == 'Y':
        i = 0
        for k in fp:
            print('')
            print('-' * 100)
            print('[IP RANGER - MODULE CREATOR]')
            print('')
            print('[FILE] Attempting to create:', k, 'with associated function:', fp[k])
            print('[ENUMERATING] This may take a moment...')
            data_enum = fp[k]()
            print('[ENUMERATING] Completed.')
            ip_ranges_compiler_pythonic(file=k, data_enum=data_enum)
            i += 1
    else:
        print('Aborting!')
        print('')
        print('-'*100)


def ip_ranges_compiler_pythonic(file=str, data_enum=[], loop=True):
    display_header()
    print('[FILE] ', file)
    if warn_user(file=file) is True:
        open(file, 'w').close()
        pre_append = '[WRITING] '
        print('')

        with open(file, 'a') as fo:
            fo.write('reserved_ipv4 = [\n')
        fo.close()

        i_x = 0
        if loop is True:
            data_enum_len = len(data_enum)
            print('[WRITING]', data_enum_len, 'items to file.')

            for _ in data_enum:
                with open(file, 'a') as fo:
                    if _ == data_enum[-1]:
                        fo.write('    "' + str(_) + '"]\n')
                    else:
                        fo.write('    "' + str(_) + '",\n')
                fo.close()

                i_x += 1
                display_progress(i_x, data_enum_len, pre_append)
        else:
            data_enum_len = 1
            with open(file, 'a') as fo:
                fo.write('    "' + str(data_enum) + '"]\n')
            fo.close()
            i_x += 1
            display_progress(i_x, data_enum_len, pre_append)
    print('\n[COMPLETED]\n')


def compile_all_reserved_ip_ranges_pythonic():
    print('[MODE] PYTHONIC LIST')
    print('[WARNING] This requires a lot of disk space!')
    user_input = input('continue? ')
    if user_input == 'y' or user_input == 'Y':
        i = 0
        for k in fp:
            print('')
            print('-' * 100)
            print('[IP RANGER - MODULE CREATOR]')
            print('')
            print('[FILE] Attempting to create:', k, 'with associated function:', fp[k])
            print('[ENUMERATING] This may take a moment...')
            data_enum = fp[k]()
            print('[ENUMERATING] Completed.')
            ip_ranges_compiler_pythonic(file=k, data_enum=data_enum)
            i += 1
    else:
        print('Aborting!')
        print('')
        print('-'*100)


def validator(file=str, data_enum=[]):
    module_data = []
    failed_data = []
    if os.path.exists(file):
        print('[VALIDATION] File exists: PASSED')
        with open(file, 'r') as fo:
            for line in fo:
                line = line.strip()
                module_data.append(line)
        fo.close()

        print('[ENUMERATING] This may take a moment...')
        data_enum = data_enum()
        print('[ENUMERATING] Completed.')

        validation = []
        if len(module_data) > 1:
            if len(data_enum) == len(module_data):
                print('[VALIDATION] List length check: PASSED')

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
                    failed_data.append(file)
                else:
                    print('[VALIDATION] List comparison check: PASSED')
                    print('[VALIDATION] PASSED')
            else:
                print('[VALIDATION] List length check: FAILED')
                print('[VALIDATION] FAILED')
                failed_data.append(file)

        elif len(module_data) == 1:
            print('[VALIDATION] List length check: PASSED')

            if data_enum == module_data[0]:
                validation.append(True)
            else:
                validation.append(False)

            if False in validation:
                print('[VALIDATION] List comparison check: FAILED')
                print('[VALIDATION] FAILED')
                failed_data.append(file)
            else:
                print('[VALIDATION] List comparison check: PASSED')
                print('[VALIDATION] PASSED')

        else:
            print('[VALIDATION] List length check: FAILED')
            print('[VALIDATION] FAILED')
            failed_data.append(file)

    else:
        print('[VALIDATION] File exists: FAILED')
        print('[VALIDATION] FAILED')
        failed_data.append(file)

    return failed_data


def validate():
    failed_data = []
    for k in f:
        print('')
        print('-' * 100)
        print('[IP RANGER - MODULE VALIDATOR]')
        print('[MODE] Standard List')
        print('')
        print('[VALIDATING] Attempting to validate:', k, 'with associated function:', f[k])
        data_enum = f[k]
        failed_data.append(validator(file=k, data_enum=data_enum))

    print('-' * 100)
    print('[SUMMARY] The following files did not pass the validation test.')
    print('          Either the files did not exist or the file(s) contents was incorrect.')
    print('')
    print('Consider re-writing the following files:')
    print('')
    count = 0
    for _ in failed_data:
        if _:
            print('   ', _)
            count += 1
    print('')
    print('[RESULTS] ' + str(count) + ' files should be written/re-written.')
    print('')


while True:
    print('')
    print('-'*100)
    print(' [IP RANGER]')
    print('')
    print(' [DESCRIPTION]')
    print('     This program intends to create files of IPv4 ranges that can be used for speed ranging.')
    print('')
    print(' [KEY]')
    print('       [S] [STANDARD LIST]')
    print('       [P] [PYTHONIC LIST]')
    print('')
    print(' [1]         [VALIDATOR]')
    print(' [2S]  [2P]  [CREATE ALL]')
    print('')
    print(' [3S]  [3P]  [CREATE SPECIFIC RANGE] [0.0.0.0]         [0.255.255.255]   [16777216]  [P] [331 MB]')
    print(' [4S]  [4P]  [CREATE SPECIFIC RANGE] [10.0.0.0]        [10.255.255.255]  [16777216]  [P] [347 MB]')
    print(' [5S]  [5P]  [CREATE SPECIFIC RANGE] [100.64.0.0]      [100.127.255.255] [4194304]   [P] [90.3 MB]')
    print(' [6S]  [6P]  [CREATE SPECIFIC RANGE] [127.0.0.0]       [127.255.255.255] [16777216]  [P] [363 MB]')
    print(' [7S]  [7P]  [CREATE SPECIFIC RANGE] [169.254.0.0]     [169.254.255.255] [65536]     [P] [1.44 MB]')
    print(' [8S]  [8P]  [CREATE SPECIFIC RANGE] [172.16.0.0]      [172.31.255.255]  [1048576]   [P] [22.1MB]')
    print(' [9S]  [9P]  [CREATE SPECIFIC RANGE] [192.0.0.0]       [192.0.0.255]     [256]       [P] [5 KB]')
    print(' [10S] [10P] [CREATE SPECIFIC RANGE] [192.0.2.0]       [192.0.2.255]     [256]       [P] [5 KB]')
    print(' [11S] [11P] [CREATE SPECIFIC RANGE] [192.88.99.0]     [192.88.99.255]   [256]       [P] [6 KB]')
    print(' [12S] [12P] [CREATE SPECIFIC RANGE] [192.168.0.0]     [192.168.255.255] [65536]     [P] [1.44 MB]')
    print(' [13S] [13P] [CREATE SPECIFIC RANGE] [198.18.0.0]      [198.19.255.255]  [131072]    [P] [2.76 MB]')
    print(' [14S] [14P] [CREATE SPECIFIC RANGE] [198.51.100.0]    [198.51.100.255]  [256]       [P] [8 KB]')
    print(' [15S] [15P] [CREATE SPECIFIC RANGE] [203.0.113.0]     [203.0.113.255]   [256]       [P] [8 KB]')
    print(' [16S] [16P] [CREATE SPECIFIC RANGE] [224.0.0.0]       [239.255.255.255] [268435456] [P] [...]')
    print(' [17S] [17P] [CREATE SPECIFIC RANGE] [233.252.0.0]     [233.252.0.255]   [256]       [P] [8 KB]')
    print(' [18S] [18P] [CREATE SPECIFIC RANGE] [240.0.0.0]       [255.255.255.254] [268435455] [P] [...]')
    print(' [19S] [19P] [CREATE SPECIFIC RANGE] [255.255.255.255]                   [1]         [P] [1 KB]')
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
    elif user_input == "2S":
        compile_all_reserved_ip_ranges()
    elif user_input == "2P":
        compile_all_reserved_ip_ranges_pythonic()
    elif user_input == "3S":
        ip_ranges_compiler(file='./modules-standard/module_0_0_0_0_to_0_255_255_255.txt',
                           data_enum=f['./modules-standard/module_0_0_0_0_to_0_255_255_255.txt']())
    elif user_input == "4S":
        ip_ranges_compiler(file='./modules-standard/module_10_0_0_0_to_10_255_255_255.txt',
                           data_enum=f['./modules-standard/module_10_0_0_0_to_10_255_255_255.txt']())
    elif user_input == "5S":
        ip_ranges_compiler(file='./modules-standard/module_100_64_0_0_to_100_127_255_255.txt',
                           data_enum=f['./modules-standard/module_100_64_0_0_to_100_127_255_255.txt']())
    elif user_input == "6S":
        ip_ranges_compiler(file='./modules-standard/module_127_0_0_0_to_127_255_255_255.txt',
                           data_enum=f['./modules-standard/module_127_0_0_0_to_127_255_255_255.txt']())
    elif user_input == "7S":
        ip_ranges_compiler(file='./modules-standard/module_169_254_0_0_to_169_254_255_255.txt',
                           data_enum=f['./modules-standard/module_169_254_0_0_to_169_254_255_255.txt']())
    elif user_input == "8S":
        ip_ranges_compiler(file='./modules-standard/module_172_16_0_0_to_172_31_255_255.txt',
                           data_enum=f['./modules-standard/module_172_16_0_0_to_172_31_255_255.txt']())
    elif user_input == "9S":
        ip_ranges_compiler(file='./modules-standard/module_192_0_0_0_to_192_0_0_255.txt',
                           data_enum=f['./modules-standard/module_192_0_0_0_to_192_0_0_255.txt']())
    elif user_input == "10S":
        ip_ranges_compiler(file='./modules-standard/module_192_0_2_0_to_192_0_2_255.txt',
                           data_enum=f['./modules-standard/module_192_0_2_0_to_192_0_2_255.txt']())
    elif user_input == "11S":
        ip_ranges_compiler(file='./modules-standard/module_192_88_99_0_to_192_88_99_255.txt',
                           data_enum=f['./modules-standard/module_192_88_99_0_to_192_88_99_255.txt']())
    elif user_input == "12S":
        ip_ranges_compiler(file='./modules-standard/module_192_168_0_0_to_192_168_255_255.txt',
                           data_enum=f['./modules-standard/module_192_168_0_0_to_192_168_255_255.txt']())
    elif user_input == "13S":
        ip_ranges_compiler(file='./modules-standard/module_198_18_0_0_to_198_19_255_255.txt',
                           data_enum=f['./modules-standard/module_198_18_0_0_to_198_19_255_255.txt']())
    elif user_input == "14S":
        ip_ranges_compiler(file='./modules-standard/module_198_51_100_0_to_198_51_100_255.txt',
                           data_enum=f['./modules-standard/module_198_51_100_0_to_198_51_100_255.txt']())
    elif user_input == "15S":
        ip_ranges_compiler(file='./modules-standard/module_203_0_113_0_to_203_0_113_255.txt',
                           data_enum=f['./modules-standard/module_203_0_113_0_to_203_0_113_255.txt']())
    elif user_input == "16S":
        ip_ranges_compiler(file='./modules-standard/module_224_0_0_0_to_239_255_255_255.txt',
                           data_enum=f['./modules-standard/module_224_0_0_0_to_239_255_255_255.txt']())
    elif user_input == "17S":
        ip_ranges_compiler(file='./modules-standard/module_233_252_0_0_to_233_252_0_255.txt',
                           data_enum=f['./modules-standard/module_233_252_0_0_to_233_252_0_255.txt']())
    elif user_input == "18S":
        ip_ranges_compiler(file='./modules-standard/module_240_0_0_0_to_255_255_255_254.txt',
                           data_enum=f['./modules-standard/module_240_0_0_0_to_255_255_255_254.txt']())
    elif user_input == "19S":
        ip_ranges_compiler(file='./modules-standard/module_255_255_255_255.txt', data_enum=f['./modules-standard/module_255_255_255_255.txt'](), loop=False)

    elif user_input == "3P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py']())
    elif user_input == "4P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_10_0_0_0_to_10_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_10_0_0_0_to_10_255_255_255.py']())
    elif user_input == "5P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_100_64_0_0_to_100_127_255_255.py',
                           data_enum=fp['./modules-pythonic/module_100_64_0_0_to_100_127_255_255.py']())
    elif user_input == "6P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_127_0_0_0_to_127_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_127_0_0_0_to_127_255_255_255.py']())
    elif user_input == "7P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_169_254_0_0_to_169_254_255_255.py',
                           data_enum=fp['./modules-pythonic/module_169_254_0_0_to_169_254_255_255.py']())
    elif user_input == "8P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_172_16_0_0_to_172_31_255_255.py',
                           data_enum=fp['./modules-pythonic/module_172_16_0_0_to_172_31_255_255.py']())
    elif user_input == "9P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_0_0_0_to_192_0_0_255.py',
                           data_enum=fp['./modules-pythonic/module_192_0_0_0_to_192_0_0_255.py']())
    elif user_input == "10P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_0_2_0_to_192_0_2_255.py',
                           data_enum=fp['./modules-pythonic/module_192_0_2_0_to_192_0_2_255.py']())
    elif user_input == "11P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_88_99_0_to_192_88_99_255.py',
                           data_enum=fp['./modules-pythonic/module_192_88_99_0_to_192_88_99_255.py']())
    elif user_input == "12P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_168_0_0_to_192_168_255_255.py',
                           data_enum=fp['./modules-pythonic/module_192_168_0_0_to_192_168_255_255.py']())
    elif user_input == "13P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_198_18_0_0_to_198_19_255_255.py',
                           data_enum=fp['./modules-pythonic/module_198_18_0_0_to_198_19_255_255.py']())
    elif user_input == "14P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_198_51_100_0_to_198_51_100_255.py',
                           data_enum=fp['./modules-pythonic/module_198_51_100_0_to_198_51_100_255.py']())
    elif user_input == "15P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_203_0_113_0_to_203_0_113_255.py',
                           data_enum=fp['./modules-pythonic/module_203_0_113_0_to_203_0_113_255.py']())
    elif user_input == "16P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_224_0_0_0_to_239_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_224_0_0_0_to_239_255_255_255.py']())
    elif user_input == "17P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_233_252_0_0_to_233_252_0_255.py',
                           data_enum=fp['./modules-pythonic/module_233_252_0_0_to_233_252_0_255.py']())
    elif user_input == "18P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_240_0_0_0_to_255_255_255_254.py',
                           data_enum=fp['./modules-pythonic/module_240_0_0_0_to_255_255_255_254.py']())
    elif user_input == "19P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_255_255_255_255.py', data_enum=fp['./modules-pythonic/module_255_255_255_255.py'](), loop=False)

