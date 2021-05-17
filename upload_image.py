import auth
import requests
import json

login = auth.Login("private")

url = login.server_url + '/team/' + login.team_uuid + '/res/attachments/upload'
print(url)

request_payload = {
    "type": "avatar", 
    "name": "1.jpg", 
    "description": "", 
    "ignore_notice": True
}

response = requests.post(url, data=json.dumps(request_payload), headers=login.common_header)
response_json = response.json()
print(json.dumps(response_json, indent="\t"))


upload_url = response_json["upload_url"]
token = response_json["token"]
file = [('file',('dep.txt',open('/Users/duxy/Downloads/dep.txt','rb'),'text/plain'))]
data = {"token": token}

# 为什么要用cookies，不用header？
# 原因：上传文件的接口，公有云与私有云不一样，公有云是上传到七牛云上的，私有云是上传到客户的服务器的。所以后端只支持用cookies发送请求，如果上传到七牛云的话我们没法做校验header。
re = requests.post(upload_url, files=file, data=data, cookies=login.cookies)
print(re.text)