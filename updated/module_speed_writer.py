import time
import codecs


def iter_items(_pythonic_list, i):
    return _pythonic_list[i]


def make_pythonic_list(items=[], name=str):
    _pythonic_list = [name + ' = [']
    for _ in items:
        _pythonic_list.append('    "' + str(_) + '",')
    _pythonic_list[-1] = str(_pythonic_list[-1].replace(',', ']\n'))
    return _pythonic_list


def create_module_file(file, min=int, max=int, _pythonic_list=[]):
    codecs.open(file, "w", encoding='utf8').close()
    codecs.open(file, "a", encoding='utf8').write('\n'.join(str(iter_items(_pythonic_list, i)) for i in range(min, max)))

