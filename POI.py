def get_cds(file):
    pois = list()

    try:
        for line in open(file, 'r').readlines():
            if line.startswith('Data0') and len(line.strip().split('=')[-1][1:-1].split('),(')) == 1:
                pois.append(line.strip().split('=')[-1][1:-1].split('),(')[0].split(','))
    except FileNotFoundError:
        print('Входной файл не найден')
        exit()

    return pois
