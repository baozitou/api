import auth
import requests
import json

login = auth.Login()

url = login.server_url + '/team/' + login.team_uuid + '/tasks/update3'

requestPayload = {
    "tasks":[
        {
            "uuid": "Tzd6R3ifVahF4H7i",
            "summary": "40xxxxxxx"
        },
        {
            "uuid":"Tzd6R3ifVahF4H7i",
            "desc_rich":"<p>xxxxxxx</p>\n"
        }
    ]
}
repsonse = requests.post(url, data=json.dumps(requestPayload), headers=login.common_header).json()
print(repsonse)