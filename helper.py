from datetime import datetime
from os import system
from math import ceil

from POI import get_cds
from constants import header


def get_file_name():
    return input('Введите имя файла: ')


def main():

    func_name = 'no_func'
    while func_name != 'exit' and func_name:
        func_name = input('Введите название операции или help: ')

        if func_name == 'help':
            with open('README.md', 'r') as docs:
                print(docs.read())

        if func_name == 'split':
            file_name = get_file_name()
            data = get_cds(file_name)
            sep_unit = input('Введите желаемое количество точек в файле или bp: ')
            data_f = list()

            if sep_unit.isdigit():
                sep_unit = int(sep_unit)
            else:
                parts = int(input('Желаемое количество файлов для разбития: '))
                sep_unit = ceil((len(data) + 1) / parts)

            print(sep_unit)

            for i in range(len(data) // sep_unit + 1):
                data_f.append(list())

            for i, el in enumerate(data, 1):
                try:
                    data_f[i // sep_unit].append(el)
                except IndexError:
                    print(i // sep_unit, len(data_f))
                    exit(1)

            for i, el in enumerate(data_f, 1):
                file_name_spl = file_name.split('.')[0] + '-' + str(i) + '.mp'
                with open(file_name_spl, 'w') as f_out:
                    f_out.write(header)
                    for cds in el:
                        f_out.write('[POI]\n')
                        f_out.write('Type=0x1710\n')
                        f_out.write(f'Data0=({",".join(cds)})\n')
                        f_out.write('[END]\n\n')

        if func_name == 'fromland':
            file_q = int(input('Введите количество файлов (разделенных): '))
            file_name = input('Введите имя основного файла: ')

            for i in range(1, file_q + 1):
                file_name_spl = file_name.split('.')[0] + '-' + str(i) + '.mp'
                system('main.py ' + file_name_spl)


if __name__ == '__main__':
    main()
