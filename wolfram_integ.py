import wolframalpha                                
import readline  
import os

app_id = os.environ['WOLF_ID']
                        
def Question(question):
 client = wolframalpha.Client(app_id)               
 res=client.query(question)
 if res['@success']=='true':
     answer = res['pod'][0]['subpod']['img']['@src']
 else: answer = 'Упс, что-то пошло не так. Проверьте вопрос'
 return answer                                     

def Plot(question):
    client=wolframalpha.Client(app_id)
    res=client.query(question)                         
    if res['@success']=='true':                            
      answer = res['pod'][1]['subpod']                   
      if len(answer)>=4:
        answer=answer[1]['img']['@src']
      else: answer=answer[1]['img']['@src']
    else: answer = 'Упс, что-то пошло не так. Проверьте вопрос'
    return answer
                                                                                     
def Solve (question):
 client=wolframalpha.Client(app_id)
 res=client.query(question)
 if res['@success']=='true': answer = next(res.results).text
 else: answer = 'Упс, что-то пошло не так. Проверьте вопрос'
 return answer
