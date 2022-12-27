import time

import module_speed_writer_pyprogress
import module_ip_ranger

print('enumerating...')
t0 = time.time()
original_list = module_ip_ranger.compile_240_0_0_0_to_255_255_255_254()
print('enumeration time:', time.time() - t0)


def use_speed_writer():
    print('-' * 50)
    print('function: use_speed_writer')
    print('writing...')
    t0 = time.time()
    name = 'pythonic_list'
    fname = './test_pythonic_list.py'
    _pythonic_list = module_speed_writer_pyprogress.make_pythonic_list(items=original_list, name=name)
    module_speed_writer_pyprogress.create_module_file(file=fname, min=0, max=int(len(original_list)+1), _pythonic_list=_pythonic_list)
    d = time.time() - t0
    print("\nwrite time: %.2f s." % d)
    print('complete.')


def use_other_writer():
    print('-'*50)
    print('function: use_other_writer')
    print('writing...')
    t0 = time.time()
    name = 'pythonic_list'
    fname = './test_pythonic_list.py'
    _pythonic_list = [name + ' = [']
    for _ in original_list:
        _pythonic_list.append('    "' + str(_) + '",')
    _pythonic_list[-1] = str(_pythonic_list[-1].replace(',', ']\n'))
    with open(fname, 'a') as fo:
        for _ in _pythonic_list:
            fo.write(_+'\n')
    fo.close()
    d = time.time() - t0
    print("\nwrite time: %.2f s." % d)
    print('complete.')


use_speed_writer()
# use_other_writer()
