import requests

def getTodaySchedules():
      answer=''
      r=requests.get('https://students.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401')
      week=r.json()['currentWeekNumber']
      leng=len(r.json()['todaySchedules'])
      i=0
      if r.json()['todaySchedules']!=[]:
          answer+='Рассписание на сегодня:\n'
          while i<leng:
             if week in r.json()['todaySchedules'][i]['weekNumber'] or r.json()['todaySchedules']!=None:
                 times=('Время: ' + r.json()['todaySchedules'][i]['lessonTime'])
                 sub=('Предмет: ' + r.json()['todaySchedules'][i]['subject']+' ('+r.json()['todaySchedules'][i]['lessonType']+')')
                 employeer=('Препод: ' + r.json()['todaySchedules'][i]['employee'][0]['lastName']+' '+r.json()['todaySchedules'][i]['employee'][0]['firstName'][0]+'. '+r.json()['tomorrowSchedules'][i]['employee'][0]['middleName'][0]+'.')
                 aud=('Аудитория: ' + r.json()['todaySchedules'][i]['auditory'][0])
                 answer+=times+'\n'+sub+'\n'+aud+'\n'+employeer+'\n-----------------\n'
                 i+=1
          return answer
      else: return 'Сегодня пар нет, гуляем)'

def getTomorrowSchedules():
      answer=''
      r=requests.get('https://students.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401')
      week=r.json()['currentWeekNumber']
      leng=len(r.json()['tomorrowSchedules'])
      i=0
      if r.json()['tomorrowSchedules']!=[]:
         answer+='Рассписание на завтра:\n'
         while i<leng:
               if week in r.json()['tomorrowSchedules'][i]['weekNumber'] or r.json()['tomorrowSchedules']!=None:
                   times=('Время: ' + r.json()['tomorrowSchedules'][i]['lessonTime'])
                   sub=('Предмет: ' + r.json()['tomorrowSchedules'][i]['subject']+' ('+r.json()['tomorrowSchedules'][i]['lessonType']+')')
                   employeer=('Препод: ' + r.json()['tomorrowSchedules'][i]['employee'][0]['lastName']+' '+r.json()['tomorrowSchedules'][i]['employee'][0]['firstName'][0]+'. '+r.json()['tomorrowSchedules'][i]['employee'][0]['middleName'][0]+'.')
                   aud=('Аудитория: ' + r.json()['tomorrowSchedules'][i]['auditory'][0])
                   answer+=times+'\n'+sub+'\n'+aud+'\n'+employeer+'\n-----------------\n'
                   i+=1
         return answer
      else: return 'Завтра пар нет, гуляем)'
