import requests
import json
import os

accuw_key = os.environ['ACCUW_KEY']

def Daily_Forecast():
    r=requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/5day/28580', params={'apikey':accuw_key, 'language':'ru'})
    date=r.json()['Headline']['EffectiveDate']
    day=r.json()['DailyForecasts'][1]
    temperature=str(int((day['Temperature']['Minimum']['Value']-32)/1.8))+' - '+str(int((day['Temperature']['Maximum']['Value']-32)/1.8))
    dayw=day['Day']['IconPhrase']
    icon=day['Day']['Icon']
    print(icon)
    if icon==1: dayw+=':sunny:'
    elif icon==4: dayw+=' :partly_sunny:'
    elif icon==17: dayw+=':partly_sunny: :thunder_cloud_rain:' 
    elif icon==14: dayw+=' :white_sun_rain_cloud:'
    nightw=day['Night']['IconPhrase']
    icon=day['Day']['Icon']
    if icon==34: nightw+=' :first_quarter_moon_with_face: '
    
    result=str(date)+'\n'+'Ночью: '+nightw+'\n'+'Днём: '+dayw+'\n'+'Температура в течении суток: '+temperature+u' \u2103'
    return result
