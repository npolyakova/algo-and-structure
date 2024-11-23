# Дана информация о времени заезда и отъезда посетителей отеля. Необходимо определить,
# в какой день посетителей в отеле единомоментно находилось больше всего.
# Пример входных данных (один элемент данного листа – кортеж, содержащий дату заезда и
# отъезда одного посетителя): [(“2024-09-15”, “2024-09-15”), (“2024-09-14”, “2024-09-21”)]

import re
from datetime import datetime, timedelta


def get_data():
    date_array = re.findall("\d{4}-\d{2}-\d{2}", input())
    in_dict = dict()
    out_dict = dict()
    for i in range(len(date_array) // 2):
        date_elements = date_array.pop()
        out_dict[i] = datetime.strptime(date_elements, '%Y-%m-%d').date()

        date_elements = date_array.pop()
        in_dict[i] = datetime.strptime(date_elements, '%Y-%m-%d').date()

    print(in_dict)
    print(out_dict)

    result = dict()
    for day in range(len(out_dict)):
        day_date = out_dict[day]
        if day_date in in_dict.values():
            result[day_date] = 2
        else:
            result[day_date] = 1

    for day in range(len(out_dict)):
        day_date = out_dict[day]
        while day_date != in_dict[day]:
            day_date += timedelta(days=-1)
            if day_date in result.keys():
                result[day_date] += 1
            else:
                result[day_date] = 1

    return result

def find_day(result):
    sorted_days = sorted(result.items(), key=lambda x:x[1])
    return sorted_days.pop()


if __name__ == '__main__':
    print(find_day(get_data()))