""" Written by Benjamin Jack Cullen

IP Ranger

This program creates human lists of IPv4 address ranges and writes them to files.

"""

import os
import time
import module_ip_ranger
import pyprogress
import module_speed_writer_pyprogress

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
     './modules-pythonic/module_10_0_0_0_to_10_255_255_255.py': module_ip_ranger.compile_10_0_0_0_to_10_255_255_255,
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
        print('')

        with open(file, 'a') as fo:
            fo.write('reserved_ipv4 = [\n')
        fo.close()

        if loop is True:
            t0 = time.time()
            name = 'reserved_ipv4'
            fname = file
            print('[ADVANCED] Write Mode')
            print('[ADVANCED] Converting List...')
            _pythonic_list = module_speed_writer_pyprogress.make_pythonic_list(items=data_enum, name=name)
            print('[ADVANCED] List Converted')
            module_speed_writer_pyprogress.create_module_file(file=fname, min=0, max=int(len(data_enum) + 1),
                                                              _pythonic_list=_pythonic_list)
            d = time.time() - t0
            print("\n[TIME] %.2f s." % d)

        else:
            with open(file, 'a') as fo:
                fo.write('    "' + str(data_enum) + '"]\n')
            fo.close()

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


def validator_pythonic(file=str, data_enum=[]):
    print('')
    print('-' * 100)
    print('[IP RANGER - MODULE VALIDATOR]')
    print('[MODE] Pythonic List')
    print('')
    print('[VALIDATING] Attempting to validate:', file, 'with function:', data_enum)
    module_data = []
    failed_data = []
    first_line_check = False
    if os.path.exists(file):
        print('[VALIDATION] File exists: PASSED')
        with open(file, 'r') as fo:
            i = 0
            for line in fo:
                line = line.strip()
                if i == 0:
                    if line == 'reserved_ipv4 = [':
                        print('[VALIDATION] First Line Check: PASSED')
                        first_line_check = True
                    else:
                        print('[VALIDATION] First Line Check: FAILED')
                        print('[VALIDATION] FAILED')
                        first_line_check = False
                        failed_data.append(file)
                        break
                if i > 0:
                    module_data.append(line)
                i += 1
        fo.close()

        if first_line_check is True:
            print('[ENUMERATING] This may take a moment...')
            data_enum = data_enum()
            print('[ENUMERATING] Completed.')

            validation = []
            if len(module_data) > 1:
                if len(data_enum) == len(module_data):
                    print('[VALIDATION] List length check: PASSED')
                    print('[VALIDATION] Attempting to compare each IPv4 address to each line in the module file.')
                    i = 0
                    for _ in data_enum:
                        if _ != data_enum[-1]:
                            if str('"' + str(_) + str('",')) == module_data[i]:
                                validation.append(True)
                            else:
                                validation.append(False)
                        elif _ == data_enum[-1]:
                            if str('"' + str(_) + str('"]')) == module_data[i]:
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
                print('[VALIDATION] Attempting to compare each IPv4 address to each line in the module file.')

                if str('"' + str(data_enum) + str('"]')) == module_data[0]:
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


def validate_pythonic():
    failed_data = []
    for k in fp:
        data_enum = fp[k]
        failed_data.append(validator_pythonic(file=k, data_enum=data_enum))

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


def validator(file=str, data_enum=[]):
    print('')
    print('-' * 100)
    print('[IP RANGER - MODULE VALIDATOR]')
    print('[MODE] Standard List')
    print('')
    print('[VALIDATING] Attempting to validate:', file, 'with function:', data_enum)
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
    print('')
    print(' [POWER RANGER]')
    print('')
    print('')
    print(' [KEY]')
    print('       [DEVELOPER TOOL] ?')
    print('       [DESCRIPTION] Creates files of IPv4 address ranges that can be used for speed ranging.')
    print('       [A] [ALL]')
    print('       [V] [VERIFY] Verify an existing list of an IPv4 address range.')
    print('       [S] [STANDARD LIST] Used with just digits creates a specific range standard list.')
    print('       [P] [PYTHONIC LIST] Used with just digits creates a specific range pythonic list.')
    print('       [ASV] Verify all standard lists.')
    print('       [APV] Verify all pythonic lists.')
    print('       [AS] Create all standard lists.')
    print('       [AP] Create all pythonic lists.')
    print('')
    print('')
    print(' [ARGUMENT]                [IPv4 START]           [IPv4 END]        [QUANTITY]  [S][SIZE] [P][SIZE]')
    print('')
    print(' [AS]  [ASV]  [AP]  [APV]')
    print('')
    print(' [3S]  [3SV]  [3P]  [3PV]  [0.0.0.0]         [->] [0.255.255.255]   [16777216]  [219 MB]  [331 MB]')
    print(' [4S]  [4SV]  [4P]  [4PV]  [10.0.0.0]        [->] [10.255.255.255]  [16777216]  [235 MB]  [347 MB]')
    print(' [5S]  [5SV]  [5P]  [5PV]  [100.64.0.0]      [->] [100.127.255.255] [4194304]   [62.3 MB] [90.3 MB]')
    print(' [6S]  [6SV]  [6P]  [6PV]  [127.0.0.0]       [->] [127.255.255.255] [16777216]  [251 MB]  [363 MB]')
    print(' [7S]  [7SV]  [7P]  [7PV]  [169.254.0.0]     [->] [169.254.255.255] [65536]     [1.1 MB]  [1.44 MB]')
    print(' [8S]  [8SV]  [8P]  [8PV]  [172.16.0.0]      [->] [172.31.255.255]  [1048576]   [15.1 MB] [22.1MB]')
    print(' [9S]  [9SV]  [9P]  [9PV]  [192.0.0.0]       [->] [192.0.0.255]     [256]       [4 KB]    [5 KB]')
    print(' [10S] [10SV] [10P] [10PV] [192.0.2.0]       [->] [192.0.2.255]     [256]       [4 KB]    [5 KB]')
    print(' [11S] [11SV] [11P] [11PV] [192.88.99.0]     [->] [192.88.99.255]   [256]       [4 KB]    [6 KB]')
    print(' [12S] [12SV] [12P] [12PV] [192.168.0.0]     [->] [192.168.255.255] [65536]     [1.01 MB] [1.44 MB]')
    print(' [13S] [13SV] [13P] [13PV] [198.18.0.0]      [->] [198.19.255.255]  [131072]    [1.89 MB] [2.76 MB]')
    print(' [14S] [14SV] [14P] [14PV] [198.51.100.0]    [->] [198.51.100.255]  [256]       [4 kB]    [8 KB]')
    print(' [15S] [15SV] [15P] [15PV] [203.0.113.0]     [->] [203.0.113.255]   [256]       [4 kB]    [8 KB]')
    print(' [16S] [16SV] [16P] [16PV] [224.0.0.0]       [->] [239.255.255.255] [268435456] [...]     [...]')
    print(' [17S] [17SV] [17P] [17PV] [233.252.0.0]     [->] [233.252.0.255]   [256]       [4 kB]    [8 KB]')
    print(' [18S] [18SV] [18P] [18PV] [240.0.0.0]       [->] [255.255.255.254] [268435455] [...]     [...]')
    print(' [19S] [19SV] [19P] [19PV] [255.255.255.255]                        [1]         [1 kB]    [1 KB]')
    print('')
    print(' [Q] [QUIT]')
    print('')
    print('')
    user_input = input(' select: ')

    if user_input == 'q' or user_input == 'Q':
        print('')
        print(' [QUITTING]')
        print('')
        print('-'*100)
        print('')
        break

    elif user_input == "ASV":
        validate()

    elif user_input == "APV":
        validate_pythonic()

    elif user_input == "AS":
        compile_all_reserved_ip_ranges()

    elif user_input == "AP":
        compile_all_reserved_ip_ranges_pythonic()

    elif user_input == "3S":
        ip_ranges_compiler(file='./modules-standard/module_0_0_0_0_to_0_255_255_255.txt',
                           data_enum=f['./modules-standard/module_0_0_0_0_to_0_255_255_255.txt']())
    elif user_input == "3SV":
        validator(file='./modules-standard/module_0_0_0_0_to_0_255_255_255.txt', data_enum=f['./modules-standard/module_0_0_0_0_to_0_255_255_255.txt'])

    elif user_input == "4S":
        ip_ranges_compiler(file='./modules-standard/module_10_0_0_0_to_10_255_255_255.txt',
                           data_enum=f['./modules-standard/module_10_0_0_0_to_10_255_255_255.txt']())
    elif user_input == "4SV":
        validator(file='./modules-standard/module_10_0_0_0_to_10_255_255_255.txt', data_enum=f['./modules-standard/module_10_0_0_0_to_10_255_255_255.txt'])

    elif user_input == "5S":
        ip_ranges_compiler(file='./modules-standard/module_100_64_0_0_to_100_127_255_255.txt',
                           data_enum=f['./modules-standard/module_100_64_0_0_to_100_127_255_255.txt']())

    elif user_input == "5SV":
        validator(file='./modules-standard/module_100_64_0_0_to_100_127_255_255.txt', data_enum=f['./modules-standard/module_100_64_0_0_to_100_127_255_255.txt'])

    elif user_input == "6S":
        ip_ranges_compiler(file='./modules-standard/module_127_0_0_0_to_127_255_255_255.txt',
                           data_enum=f['./modules-standard/module_127_0_0_0_to_127_255_255_255.txt']())

    elif user_input == "6SV":
        validator(file='./modules-standard/module_127_0_0_0_to_127_255_255_255.txt', data_enum=f['./modules-standard/module_127_0_0_0_to_127_255_255_255.txt'])

    elif user_input == "7S":
        ip_ranges_compiler(file='./modules-standard/module_169_254_0_0_to_169_254_255_255.txt',
                           data_enum=f['./modules-standard/module_169_254_0_0_to_169_254_255_255.txt']())

    elif user_input == "7SV":
        validator(file='./modules-standard/module_169_254_0_0_to_169_254_255_255.txt', data_enum=f['./modules-standard/module_169_254_0_0_to_169_254_255_255.txt'])

    elif user_input == "8S":
        ip_ranges_compiler(file='./modules-standard/module_172_16_0_0_to_172_31_255_255.txt',
                           data_enum=f['./modules-standard/module_172_16_0_0_to_172_31_255_255.txt']())

    elif user_input == "8SV":
        validator(file='./modules-standard/module_172_16_0_0_to_172_31_255_255.txt', data_enum=f['./modules-standard/module_172_16_0_0_to_172_31_255_255.txt'])

    elif user_input == "9S":
        ip_ranges_compiler(file='./modules-standard/module_192_0_0_0_to_192_0_0_255.txt',
                           data_enum=f['./modules-standard/module_192_0_0_0_to_192_0_0_255.txt']())

    elif user_input == "9SV":
        validator(file='./modules-standard/module_192_0_0_0_to_192_0_0_255.txt', data_enum=f['./modules-standard/module_192_0_0_0_to_192_0_0_255.txt'])

    elif user_input == "10S":
        ip_ranges_compiler(file='./modules-standard/module_192_0_2_0_to_192_0_2_255.txt',
                           data_enum=f['./modules-standard/module_192_0_2_0_to_192_0_2_255.txt']())

    elif user_input == "10SV":
        validator(file='./modules-standard/module_192_0_2_0_to_192_0_2_255.txt', data_enum=f['./modules-standard/module_192_0_2_0_to_192_0_2_255.txt'])

    elif user_input == "11S":
        ip_ranges_compiler(file='./modules-standard/module_192_88_99_0_to_192_88_99_255.txt',
                           data_enum=f['./modules-standard/module_192_88_99_0_to_192_88_99_255.txt']())

    elif user_input == "11SV":
        validator(file='./modules-standard/module_192_88_99_0_to_192_88_99_255.txt', data_enum=f['./modules-standard/module_192_88_99_0_to_192_88_99_255.txt'])

    elif user_input == "12S":
        ip_ranges_compiler(file='./modules-standard/module_192_168_0_0_to_192_168_255_255.txt',
                           data_enum=f['./modules-standard/module_192_168_0_0_to_192_168_255_255.txt']())

    elif user_input == "12SV":
        validator(file='./modules-standard/module_192_168_0_0_to_192_168_255_255.txt', data_enum=f['./modules-standard/module_192_168_0_0_to_192_168_255_255.txt'])

    elif user_input == "13S":
        ip_ranges_compiler(file='./modules-standard/module_198_18_0_0_to_198_19_255_255.txt',
                           data_enum=f['./modules-standard/module_198_18_0_0_to_198_19_255_255.txt']())

    elif user_input == "13SV":
        validator(file='./modules-standard/module_198_18_0_0_to_198_19_255_255.txt', data_enum=f['./modules-standard/module_198_18_0_0_to_198_19_255_255.txt'])

    elif user_input == "14S":
        ip_ranges_compiler(file='./modules-standard/module_198_51_100_0_to_198_51_100_255.txt',
                           data_enum=f['./modules-standard/module_198_51_100_0_to_198_51_100_255.txt']())

    elif user_input == "14SV":
        validator(file='./modules-standard/module_198_51_100_0_to_198_51_100_255.txt', data_enum=f['./modules-standard/module_198_51_100_0_to_198_51_100_255.txt'])

    elif user_input == "15S":
        ip_ranges_compiler(file='./modules-standard/module_203_0_113_0_to_203_0_113_255.txt',
                           data_enum=f['./modules-standard/module_203_0_113_0_to_203_0_113_255.txt']())

    elif user_input == "15SV":
        validator(file='./modules-standard/module_203_0_113_0_to_203_0_113_255.txt', data_enum=f['./modules-standard/module_203_0_113_0_to_203_0_113_255.txt'])

    elif user_input == "16S":
        ip_ranges_compiler(file='./modules-standard/module_224_0_0_0_to_239_255_255_255.txt',
                           data_enum=f['./modules-standard/module_224_0_0_0_to_239_255_255_255.txt']())

    elif user_input == "16SV":
        validator(file='./modules-standard/module_224_0_0_0_to_239_255_255_255.txt', data_enum=f['./modules-standard/module_224_0_0_0_to_239_255_255_255.txt'])

    elif user_input == "17S":
        ip_ranges_compiler(file='./modules-standard/module_233_252_0_0_to_233_252_0_255.txt',
                           data_enum=f['./modules-standard/module_233_252_0_0_to_233_252_0_255.txt']())

    elif user_input == "17SV":
        validator(file='./modules-standard/module_233_252_0_0_to_233_252_0_255.txt', data_enum=f['./modules-standard/module_233_252_0_0_to_233_252_0_255.txt'])

    elif user_input == "18S":
        ip_ranges_compiler(file='./modules-standard/module_240_0_0_0_to_255_255_255_254.txt',
                           data_enum=f['./modules-standard/module_240_0_0_0_to_255_255_255_254.txt']())

    elif user_input == "18SV":
        validator(file='./modules-standard/module_240_0_0_0_to_255_255_255_254.txt', data_enum=f['./modules-standard/module_240_0_0_0_to_255_255_255_254.txt'])

    elif user_input == "19S":
        ip_ranges_compiler(file='./modules-standard/module_255_255_255_255.txt', data_enum=f['./modules-standard/module_255_255_255_255.txt'](), loop=False)

    elif user_input == "19SV":
        validator(file='./modules-standard/module_255_255_255_255.txt', data_enum=f['./modules-standard/module_255_255_255_255.txt'])

    elif user_input == "3P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py']())

    elif user_input == "3PV":
        validator_pythonic(file='./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py', data_enum=fp['./modules-pythonic/module_0_0_0_0_to_0_255_255_255.py'])

    elif user_input == "4P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_10_0_0_0_to_10_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_10_0_0_0_to_10_255_255_255.py']())

    elif user_input == "4PV":
        validator_pythonic(file='./modules-pythonic/module_10_0_0_0_to_10_255_255_255.py', data_enum=fp['./modules-pythonic/module_10_0_0_0_to_10_255_255_255.py'])

    elif user_input == "5P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_100_64_0_0_to_100_127_255_255.py',
                           data_enum=fp['./modules-pythonic/module_100_64_0_0_to_100_127_255_255.py']())

    elif user_input == "5PV":
        validator_pythonic(file='./modules-pythonic/module_100_64_0_0_to_100_127_255_255.py', data_enum=fp['./modules-pythonic/module_100_64_0_0_to_100_127_255_255.py'])

    elif user_input == "6P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_127_0_0_0_to_127_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_127_0_0_0_to_127_255_255_255.py']())

    elif user_input == "6PV":
        validator_pythonic(file='./modules-pythonic/module_127_0_0_0_to_127_255_255_255.py', data_enum=fp['./modules-pythonic/module_127_0_0_0_to_127_255_255_255.py'])

    elif user_input == "7P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_169_254_0_0_to_169_254_255_255.py',
                           data_enum=fp['./modules-pythonic/module_169_254_0_0_to_169_254_255_255.py']())

    elif user_input == "7PV":
        validator_pythonic(file='./modules-pythonic/module_169_254_0_0_to_169_254_255_255.py', data_enum=fp['./modules-pythonic/module_169_254_0_0_to_169_254_255_255.py'])

    elif user_input == "8P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_172_16_0_0_to_172_31_255_255.py',
                           data_enum=fp['./modules-pythonic/module_172_16_0_0_to_172_31_255_255.py']())

    elif user_input == "8PV":
        validator_pythonic(file='./modules-pythonic/module_172_16_0_0_to_172_31_255_255.py', data_enum=fp['./modules-pythonic/module_172_16_0_0_to_172_31_255_255.py'])

    elif user_input == "9P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_0_0_0_to_192_0_0_255.py',
                           data_enum=fp['./modules-pythonic/module_192_0_0_0_to_192_0_0_255.py']())

    elif user_input == "9PV":
        validator_pythonic(file='./modules-pythonic/module_192_0_0_0_to_192_0_0_255.py', data_enum=fp['./modules-pythonic/module_192_0_0_0_to_192_0_0_255.py'])

    elif user_input == "10P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_0_2_0_to_192_0_2_255.py',
                           data_enum=fp['./modules-pythonic/module_192_0_2_0_to_192_0_2_255.py']())

    elif user_input == "10PV":
        validator_pythonic(file='./modules-pythonic/module_192_0_2_0_to_192_0_2_255.py', data_enum=fp['./modules-pythonic/module_192_0_2_0_to_192_0_2_255.py'])

    elif user_input == "11P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_88_99_0_to_192_88_99_255.py',
                           data_enum=fp['./modules-pythonic/module_192_88_99_0_to_192_88_99_255.py']())

    elif user_input == "11PV":
        validator_pythonic(file='./modules-pythonic/module_192_88_99_0_to_192_88_99_255.py', data_enum=fp['./modules-pythonic/module_192_88_99_0_to_192_88_99_255.py'])

    elif user_input == "12P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_192_168_0_0_to_192_168_255_255.py',
                           data_enum=fp['./modules-pythonic/module_192_168_0_0_to_192_168_255_255.py']())

    elif user_input == "12PV":
        validator_pythonic(file='./modules-pythonic/module_192_168_0_0_to_192_168_255_255.py', data_enum=fp['./modules-pythonic/module_192_168_0_0_to_192_168_255_255.py'])

    elif user_input == "13P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_198_18_0_0_to_198_19_255_255.py',
                           data_enum=fp['./modules-pythonic/module_198_18_0_0_to_198_19_255_255.py']())

    elif user_input == "13PV":
        validator_pythonic(file='./modules-pythonic/module_198_18_0_0_to_198_19_255_255.py', data_enum=fp['./modules-pythonic/module_198_18_0_0_to_198_19_255_255.py'])

    elif user_input == "14P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_198_51_100_0_to_198_51_100_255.py',
                           data_enum=fp['./modules-pythonic/module_198_51_100_0_to_198_51_100_255.py']())

    elif user_input == "14PV":
        validator_pythonic(file='./modules-pythonic/module_198_51_100_0_to_198_51_100_255.py', data_enum=fp['./modules-pythonic/module_198_51_100_0_to_198_51_100_255.py'])

    elif user_input == "15P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_203_0_113_0_to_203_0_113_255.py',
                           data_enum=fp['./modules-pythonic/module_203_0_113_0_to_203_0_113_255.py']())

    elif user_input == "15PV":
        validator_pythonic(file='./modules-pythonic/module_203_0_113_0_to_203_0_113_255.py', data_enum=fp['./modules-pythonic/module_203_0_113_0_to_203_0_113_255.py'])

    elif user_input == "16P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_224_0_0_0_to_239_255_255_255.py',
                           data_enum=fp['./modules-pythonic/module_224_0_0_0_to_239_255_255_255.py']())

    elif user_input == "16PV":
        validator_pythonic(file='./modules-pythonic/module_224_0_0_0_to_239_255_255_255.py', data_enum=fp['./modules-pythonic/module_224_0_0_0_to_239_255_255_255.py'])

    elif user_input == "17P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_233_252_0_0_to_233_252_0_255.py',
                           data_enum=fp['./modules-pythonic/module_233_252_0_0_to_233_252_0_255.py']())

    elif user_input == "17PV":
        validator_pythonic(file='./modules-pythonic/module_233_252_0_0_to_233_252_0_255.py', data_enum=fp['./modules-pythonic/module_233_252_0_0_to_233_252_0_255.py'])

    elif user_input == "18P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_240_0_0_0_to_255_255_255_254.py',
                           data_enum=fp['./modules-pythonic/module_240_0_0_0_to_255_255_255_254.py']())

    elif user_input == "18PV":
        validator_pythonic(file='./modules-pythonic/module_240_0_0_0_to_255_255_255_254.py', data_enum=fp['./modules-pythonic/module_240_0_0_0_to_255_255_255_254.py'])

    elif user_input == "19P":
        ip_ranges_compiler_pythonic(file='./modules-pythonic/module_255_255_255_255.py', data_enum=fp['./modules-pythonic/module_255_255_255_255.py'](), loop=False)

    elif user_input == "19PV":
        validator_pythonic(file='./modules-pythonic/module_255_255_255_255.py', data_enum=fp['./modules-pythonic/module_255_255_255_255.py'])
