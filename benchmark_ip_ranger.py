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


import os.path
import time
import module_ip_ranger
t0 = time.time()
import module_0_0_0_0_to_0_255_255_255_pythonic_list
print('import module_0_0_0_0_to_0_255_255_255_pythonic_list time:', time.time() - t0)

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


def seperator():
    print('-'*50)


def benchmark_enum(data_enum=[]):
    t0 = time.time()
    print('items: ' + str(len(data_enum())))
    print('enumeration time:', time.time() - t0)


def benchmark_read(file=str):
    t0 = time.time()
    try:
        l = []
        with open(file, 'r') as fo:
            for line in fo:
                line = line.strip()
                l.append(line)
        print('items: ' + str(len(l)))
        print('read time:', time.time() - t0)
    except:
        print('file: not not yet exists.')
        pass


def benchmark_pythonic_list(data_enum=[], t0=()):
    print('items: ' + str(len(data_enum)))
    print('pythonic list time:', time.time() - t0)


def benchmark_all():
    i = 0
    for k in f:
        if os.path.exists(k):
            seperator()
            print('benchmarking:', f[k])
            data_enum = f[k]
            benchmark_enum(data_enum=data_enum)
            benchmark_read(file=k)
            if i == 0:
                t0 = time.time()
                benchmark_pythonic_list(data_enum=module_0_0_0_0_to_0_255_255_255_pythonic_list.reserved_ipv4, t0=t0)
        i += 1


benchmark_all()
