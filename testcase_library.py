import requests
import json
import auth
import testcaseFieldConfigs

class TestcaseLibrary():

    def __init__(self, login):

        self.url = login.server_url + '/team/' + login.team_uuid + '/testcase/libraries/add'
        self.login = login

    def sendRequest(self, libraryName="TEST", field_config_uuid=None):

        # 发送请求
        request_payload = {
            "library": {
                'name': libraryName,
                "members": [
                    {
                        'user_domain_type': 'testcase_administrators',
                        'user_domain_param': ''
                    },
                    {
                        'user_domain_type': 'single_user',
                        'user_domain_param': self.login.user_uuid
                    }
                ],
                'field_config_uuid': field_config_uuid
            }
        }
        respose = requests.post(self.url, headers=self.login.common_header, data=json.dumps(request_payload)).json()

        # 获取数据
        self.response = respose
        self.library_uuid = respose['library']['uuid']
        self.library_modules_uuid = respose['library']['modules'][0]['uuid']

if __name__ == '__main__':

    login = auth.Login()

    testcaseFieldConfigs = testcaseFieldConfigs.TestcaseFieldConfigs(login)
    testcaseFieldConfigs.getTestcaseFieldConfigs()

    testcaseLibrary = TestcaseLibrary(login)

    testcaseLibrary.sendRequest(libraryName="1", field_config_uuid=testcaseFieldConfigs.testcaseFieldConfigs_uuid)

    print(json.dumps(testcaseLibrary.response, ensure_ascii=False, indent="\t"))

    # for i in range(0, 100):
    #     testcaseLibrary.sendRequest(testcaseLibrary.login, testcaseLibrary.url, str(i))