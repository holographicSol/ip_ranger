import codecs
import pyprogress

multiplier = pyprogress.multiplier_from_inverse_factor(factor=25)


def iter_items(_pythonic_list, i):
    pyprogress.progress_bar(part=int(i+1), whole=int(len(_pythonic_list)-1),
                            pre_append='[WRITING] ',
                            append=str(' ' + str(i) + ' / ' + str(int(len(_pythonic_list))-1)),
                            encapsulate_l='|',
                            encapsulate_r='|',
                            encapsulate_l_color='LIGHTCYAN_EX',
                            encapsulate_r_color='LIGHTCYAN_EX',
                            progress_char=' ',
                            bg_color='LIGHTCYAN_EX',
                            factor=25,
                            multiplier=multiplier)
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
