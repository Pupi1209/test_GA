import pandas as pd
import re

#для сравнительного анализа был выбран ресурс 2ГИС. Были спаршены данные с сайта, код ниже предназначен
#для обработки таблицы с целью выделения координат ПОИ
excel = pd.read_csv("excel для парсинга.csv")

log = []
i = 0
for index, line in enumerate(excel.iterrows()):
    # print(line)
    i += 1
    for elem in line:
        try:
            for column in elem:
                column = str(column)
                found = re.findall('66\.\d+', column)
                if found:
                    # print(found)
                    excel.loc[index, 'latitude'] = found[0]
                found = re.findall('70\.\d+', column)
                if found:
                    excel.loc[index, 'longitude'] = found[0]
            found = False
        except:
            log.append(elem)

    try:
        print(f"{i}: {excel.loc[index, 'latitude']} {excel.loc[index, 'longitude']}")
    except:
        print(i)


excel.to_csv('2gis.csv')