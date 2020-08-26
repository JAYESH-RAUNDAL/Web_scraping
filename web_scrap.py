
import requests
login_url="http://3.6.0.2/inject-solar-angular/inject_solar_server/admin/Admin/login"
scrap_url="http://3.6.0.2/inject-solar-angular/inject_solar_server/normal/Alarms/getClearedNormalAlarms"
payload= { "login_id": "triose",
            "password": "triose123"}
s=requests.session()
import json
r=s.post(login_url,data=json.dumps(payload))
headers={}
headers["Authorization"] = r.json()["resultObject"]["token"]
#print(headers)
#print(r.status_code)
dict={'user_id': "90", 'start_date': "2020-01-01", 'end_date': "2020-02-29", 'limit': 10, 'offset': 0}
#print(res.json()["resultObject"])
responce=s.post(scrap_url,headers=headers,data=json.dumps(dict))
#print(responce.json())
list=[]
values=responce.json()["resultObject"]
for i in values:
    list.append((i["dev_name"], i["name"], i["alarm_id"], i['date_time'], i["clear_time"], i["alarm_msg"]))
print(list)
from data_base import table,fetch
table(list)
fetch('error_log')
s.close()





