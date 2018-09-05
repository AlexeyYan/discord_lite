import requests

def getTodaySchedules():
      answer=''
      r=requests.get('https://students.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401')
      week=r.json()['currentWeekNumber']
      if r.json()['todaySchedules']!=[]:
          answer+='Рассписание на сегодня:\n'
          for lesson in r.json()['todaySchedules']:
             if week in lesson['weekNumber'] or r.json()['todaySchedules']!=None:
                 times=('Время: ' + lesson['lessonTime'])
                 sub=('Предмет: ' + lesson['subject']+' ('+lesson['lessonType']+')')
                 if 'employee' in lesson.keys():
                     employeer=('Препод: ' + lesson['employee'][0]['fio'])
                 else:
                     employeer=''
                 aud=('Аудитория: ' + lesson['auditory'][0])
                 answer+=times+'\n'+sub+'\n'+aud+'\n'+employeer+'\n-----------------\n'
          return answer
      else: return 'Сегодня пар нет, гуляем)'

def getTomorrowSchedules():
      answer=''
      r=requests.get('https://students.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401')
      week=r.json()['currentWeekNumber']
      if r.json()['tomorrowSchedules']!=[]:
         answer+='Рассписание на завтра:\n'
         for lesson in r.json()['tomorrowSchedules']:
               if week in lesson['weekNumber'] or r.json()['tomorrowSchedules']!=None:
                   times=('Время: ' + lesson['lessonTime'])
                   sub=('Предмет: ' + lesson['subject']+' ('+lesson['lessonType']+')')
                   if 'employee' in lesson.keys():
                     employeer=('Препод: ' + lesson['employee'][0]['fio'])
                   else:
                     employeer=''
                   aud=('Аудитория: ' + lesson['auditory'][0])
                   answer+=times+'\n'+sub+'\n'+aud+'\n'+employeer+'\n-----------------\n'
         return answer
      else: return 'Завтра пар нет, гуляем)'
