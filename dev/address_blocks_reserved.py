""" Written by Benjamin Jack Cullen

This program helps me find ranges by using source:
source: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml

Then makes me a function I can copy into my module.

"""

import ipaddress

# 3970693120(pub) + 324274190(res) = 4,294,967,310 - 14(below_overlap) = 4,294,967,296

address_blocks = [
    '0.0.0.0/8',

    '0.0.0.0/32',  # = -1  overlap

    '10.0.0.0/8',

    '100.64.0.0/10',

    '127.0.0.0/8',

    '169.254.0.0/16',

    '172.16.0.0/12',

    '192.0.0.0/24',

    '192.0.0.0/29',  # = -7  overlap

    '192.0.0.8/32',  # = -1  overlap

    '192.0.0.9/32',  # = -1  overlap

    '192.0.0.10/32',  # = -1  overlap

    '192.0.0.170/32',  # = -1  overlap

    '192.0.0.171/32',  # -1  overlap

    '192.0.2.0/24',

    '192.31.196.0/24',

    '192.52.193.0/24',

    '192.88.99.0/24',

    '192.168.0.0/16',

    '192.175.48.0/24',

    '198.18.0.0/15',

    '198.51.100.0/24',

    '203.0.113.0/24',

    '240.0.0.0/4',

    '255.255.255.255/32'  # -1  overlap
]

print('def provide_private_ranges():')
print('    return [')
for _ in address_blocks:
    start = ipaddress.ip_network(_)
    if _ == address_blocks[-1]:
        print('        ["' + str(start[0]) + '", "' + str(start[-1]) + '"]')
    else:
        print('        ["' + str(start[0]) + '", "' + str(start[-1]) + '"],')
print('    ]')
