# -*- coding: UTF-8 -*-
import requests
import json
import configparser
import os.path


class Login():

    def __init__(self, plaform="dev"):

        # 加载数据
        self.load_data(plaform=plaform)

        # 发送请求
        login_url = self.server_url + '/auth/login'
        login_headers = {'Content-Type': 'application/json'}
        login_body = {'email': self.__email, 'password': self.__password}

        login_response = requests.post(login_url, data=json.dumps(login_body), headers=login_headers)
        login_response_json = login_response.json()

        # 获取通用信息
        self.cookies = login_response.cookies
        self.login_reponse_json = login_response_json
        self.user_uuid = login_response_json['user']['uuid']
        self.user_token = login_response_json['user']['token']
        self.common_header = {
            'Content-Type': 'application/json',
            'Ones-User-ID': self.user_uuid,
            'Ones-Auth-Token': self.user_token
        }
        if plaform == "dev":
            self.team_uuid = login_response_json['teams'][6]['uuid']
        elif plaform == "saas":
            self.team_uuid = login_response_json['teams'][-1]['uuid']
        elif plaform == "private":
            self.team_uuid = login_response_json['teams'][0]['uuid']
        elif plaform == "preview2":
            self.team_uuid = login_response_json['teams'][0]['uuid']



    def load_data(self, plaform):

        config = configparser.ConfigParser()
        file_path = os.path.abspath('.') + '/config.ini'
        config.read(file_path)

        self.server_url = config.get('Server', plaform)
        self.__email = config.get(plaform, "email")
        self.__password =config.get(plaform, "password")


if __name__ == '__main__':
    login = Login("dev")
    print(json.dumps(login.login_reponse_json, indent="\t"))





