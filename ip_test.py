#Автор https://github.com/vetprogs
#По вопросам и предложениям:  vetprogs@rambler.ru

import time
import requests

st_run=time.time()
myip=requests.get('https://ifconfig.me').text.strip() #узнать внешний IP
apiget = 'https://www.iplocate.io/api/lookup/'+myip
zapros=requests.get(apiget)   #получаем информацию про IP

for k, v in zapros.json().items(): 
    if v:                     #показываем только не пустые ключи  
        print(f"{k}:{v}")

print("Выполнено за: {:1.2f} ms".format((time.time()-st_run)*1000))
