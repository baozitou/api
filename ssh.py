import paramiko
import json

# ssh进入服务器
ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.connect('45.78.9.10', 29056, 'duxy')

# 开启webhook服务
stdin,stdout,stderr = ssh_client.exec_command('ps -ef | grep test_webhook.py')
result = stdout.readlines()
if len(result) == 1:
    print("webhook服务没有开启，正在开启中。。。")
    ssh_client.exec_command('nohup python3 test_webhook.py > webhook.log &')
    print("开启成功")
else:
    print("webhook服务已开启，不需要再启动")

# 获取webhook通知
stdin,stdout,stderr = ssh_client.exec_command('cat webhook.log | grep message')
webhook_message = stdout.readlines()
# data = json.dumps(eval(webhook_message[-1]), sort_keys=True, ensure_ascii=False, indent=4, separators=(', ',': '))
# print(data)
# data_json = json.loads(data)
# print(data_json['messages'][0]['desc'])

print(eval(webhook_message[-1])["messages"][0]["desc"])
print(eval(webhook_message[-2])["messages"][0]["desc"])

ssh_client.close()