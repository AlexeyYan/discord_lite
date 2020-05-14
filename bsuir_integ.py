import requests


def Get_Schedules(day):
    if day == 0:
        answer = 'Расписание на сегодня:\n'
        key = 'todaySchedules'
        alt_answer = 'Сегодня пар нет, гуляем)'
    else:
        answer = 'Расписание на завтра:\n'
        key = 'tomorrowSchedules'
        alt_answer = 'Завтра пар нет, гуляем)'
    try:
        r = requests.get('https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401').json()
    except Exception:
        return 'Произошла ошибка!'
    else:
        week = r['currentWeekNumber']
        if r[key] != []:
            for lesson in r[key]:
                if week in lesson['weekNumber'] or r[key] is not None:
                    times = f'Время: {lesson["lessonTime"]}'
                    sub = f'Предмет: {lesson["subject"]} ({lesson["lessonType"]})'
                    if lesson['employee'] != []:
                        employeer = f'Препод:  {lesson["employee"][0]["fio"]}'
                    else:
                        employeer = ''
                    if lesson['auditory'] !=[]:
                        aud = f'Аудитория: {lesson["auditory"][0]}'
                    else:
                        aud = ''
                    answer += f'{times}\n{sub}\n{aud}\n{employeer}\n{"-"*17}\n'
            return answer
        else:
            return alt_answer
