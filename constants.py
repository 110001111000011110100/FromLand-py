# -*- coding: UTF-8 -*-

# Заголовок для mp-файла
header = (
            "; Generated by GPSMapEdit 2.1.78.8\n\n"
            "[IMG ID]\n"
            "CodePage=1251\n"
            "LblCoding=9\n"
            "ID=115300\n"
            "Name=Нижегородская область\n"
            "TypeSet=NG\n"
            "Elevation=M\n"
            "Preprocess=F\n"
            "TreSize=511\n"
            "TreMargin=0.000000\n"
            "RgnLimit=127\n"
            "POIIndex=Y\n"
            "POINumberFirst=Y\n"
            "POIZipFirst=Y\n"
            "Copyright=© Нижегородский GPS-клуб, 2005-2015|www.gps-nnov.ru\n"
            "LocalName=Нижегородская область\n"
            "MainTown=Нижегородская область\n"
            "OverviewMap=Eurasia.dcm\n"
            "PointView=N56.282837 E43.945023\n"
            "Version=18\n"
            "VersionSub=1\n"
            "Levels=2\n"
            "Level0=26\n"
            "Level1=14\n"
            "Zoom0=0\n"
            "Zoom1=1\n"
            "[END-IMG ID]\n\n"
        )

# Далее идут шаблоны регулярных выражений. Учитываются и пробелы и регистр.
# Шаблоны разделяются вертикальной чертой (синтаксис регулярок)
# Внутри каждого шаблона шаблоны должны идти от более строгого к менее строгому

# Шаблоны названий улиц.
ul_patt = u' ул. | ул |,ул.| улица | УЛ '   # преобразуется в окончание "улица"
per_patt = u' пер. | пер |,пер.| переулок'  # преобразуется в окончание "переулок"
pass_patt = u' проезд '                     # преобразуется в окончание "проезд"
trakt_patt = u' тракт '                     # преобразуется в окончание "тракт"
ave_patt = u', пр-кт '                      # преобразуется в окончание "проспект"
road_patt = u', ш. '                        # преобразуется в окончание "шоссе"
snt_patt = u' СНТ '                         # преобразуется в окончание "СНТ"

# Шаблоны разделителя названия улицы и номера дома
house_patt = u', дом |, д. |, д.|, д|, |,'
