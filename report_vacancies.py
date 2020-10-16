def report_vacancies(numbers, periods):
    #максимальное количество интервалов с максимальным количеством вакансий в период времени
    max_intervals = 0
    #суммарное время, в который было открыто максимальное количество вакансий
    max_time = 0
    #счетчик вакансий
    count = 0
    #счетчик вакансий на промежутке
    max_vac = 0
    start = 0
    for p in periods:
        if p[1] < 0:
            count = count + 1
            if count > max_vac:
                max_vac = count
                max_intervals = 1
                start = p[0]
                max_time = 0
            elif count == max_vac:
                max_intervals = max_intervals + 1
                start = p[0]
        else:
            if count == max_vac:
                max_time = max_time + p[0] - start + 1
            count = count - 1
    return max_intervals, max_time


count_vacancies = int(input())
periods = []
while count_vacancies > 0:
    count_vacancies = count_vacancies - 1
    start, end = map(int, input().split())
    periods.append([start, -1])
    periods.append([end, 1])
periods.sort()
print(*report_vacancies(count_vacancies, periods), sep=" ")