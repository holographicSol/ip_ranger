""" Written by Benjamin Jack Cullen

This program is designed to compare timings between enumerating address ranges and reading
pre-enumerated address ranges.

Pre-Enumerated Address Ranges:
    Create using ip_ranger.
    Then benchmark.

Notes on performance experimentation when initializing enumerated/pre-enumerated address ranges:
    Enumeration: Medium performance
    Pre-Enumeration stored as pythonic list: Slowest results un-compiled. Fastest if compiled
    Pre-Enumeration stored as list in text file: Fastest un-compiled.

    Different systems may vary results.

"""
print('-'*100)
print('-- importing modules...')
import os.path
import time
import module_ip_ranger
t0 = time.time()
import module_0_0_0_0_to_0_255_255_255                  #1
import module_10_0_0_0_to_10_255_255_255                #2
import module_100_64_0_0_to_100_127_255_255
import module_127_0_0_0_to_127_255_255_255
import module_169_254_0_0_to_169_254_255_255            #5
import module_172_16_0_0_to_172_31_255_255
import module_192_0_0_0_to_192_0_0_255                  #7
import module_192_0_2_0_to_192_0_2_255                  #8
import module_192_88_99_0_to_192_88_99_255              #9
import module_192_168_0_0_to_192_168_255_255
import module_198_18_0_0_to_198_19_255_255
import module_198_51_100_0_to_198_51_100_255            #12
import module_203_0_113_0_to_203_0_113_255              #13
# import module_224_0_0_0_to_239_255_255_255
import module_233_252_0_0_to_233_252_0_255              #15
# import module_240_0_0_0_to_255_255_255_254
import module_255_255_255_255                           #17
print('import address ranges time:', time.time() - t0)

# './module_224_0_0_0_to_239_255_255_255.txt': module_ip_ranger.compile_224_0_0_0_to_239_255_255_255,
# './module_240_0_0_0_to_255_255_255_254.txt': module_ip_ranger.compile_240_0_0_0_to_255_255_255_254}

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
     './module_233_252_0_0_to_233_252_0_255.txt': module_ip_ranger.compile_233_252_0_0_to_233_252_0_255}


def seperator():
    print('-'*50)


def benchmark_enum(data_enum=[]):
    t0 = time.time()
    print('enumeration items: ' + str(len(data_enum())))
    print('enumeration time:', time.time() - t0)


def benchmark_read(data_enum=[]):
    t0 = time.time()
    try:
        t0 = time.time()
        print('read items: ' + str(len(data_enum(disk=True))))
        print('read time:', time.time() - t0)
    except:
        print('file: not yet exists.')
        pass


def benchmark_pythonic_list(data_enum=[], t0=()):
    print('pythonic list items: ' + str(len(data_enum)))
    print('pythonic list time:', time.time() - t0)


def benchmark_all():
    i = 0
    for k in f:
        if os.path.exists(k):
            seperator()
            print('benchmarking:', f[k])
            data_enum = f[k]
            benchmark_enum(data_enum=data_enum)
            benchmark_read(data_enum=data_enum)

            if i == 0:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_0_0_0_0_to_0_255_255_255.reserved_ipv4, t0=t0)
            elif i == 1:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_10_0_0_0_to_10_255_255_255.reserved_ipv4, t0=t0)
            elif i == 2:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_100_64_0_0_to_100_127_255_255.reserved_ipv4, t0=t0)
            elif i == 3:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_127_0_0_0_to_127_255_255_255.reserved_ipv4, t0=t0)
            elif i == 4:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_169_254_0_0_to_169_254_255_255.reserved_ipv4, t0=t0)
            elif i == 5:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_172_16_0_0_to_172_31_255_255.reserved_ipv4, t0=t0)
            elif i == 6:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_192_0_0_0_to_192_0_0_255.reserved_ipv4, t0=t0)
            elif i == 7:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_192_0_2_0_to_192_0_2_255.reserved_ipv4, t0=t0)
            elif i == 8:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_192_88_99_0_to_192_88_99_255.reserved_ipv4, t0=t0)
            elif i == 9:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_192_168_0_0_to_192_168_255_255.reserved_ipv4, t0=t0)
            elif i == 10:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_198_18_0_0_to_198_19_255_255.reserved_ipv4, t0=t0)
            elif i == 11:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_198_51_100_0_to_198_51_100_255.reserved_ipv4, t0=t0)
            elif i == 12:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_203_0_113_0_to_203_0_113_255.reserved_ipv4, t0=t0)
            # elif i == 13:
            #     t0 = time.time()
            #     benchmark_pythonic_list(data_enum=module_224_0_0_0_to_239_255_255_255.reserved_ipv4, t0=t0)
            elif i == 14:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_233_252_0_0_to_233_252_0_255.reserved_ipv4, t0=t0)
            # elif i == 15:
            #     t0 = time.time()
            #     benchmark_pythonic_list(data_enum=module_240_0_0_0_to_255_255_255_254.reserved_ipv4, t0=t0)
        i += 1


benchmark_all()
