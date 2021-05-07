import auth
import testcase_library
import requests
import json
import testcaseFieldConfigs
import threading



class Testcase():

    def __init__(self, login=None, library=None):

        self.url = login.server_url + '/team/' + login.team_uuid + '/items/add'
        self.login = login
        self.library = library


    def sendRequest(self, testcaseName=None):

        request_payload = {
            "item": {
                "assign": self.login.user_uuid,
                "condition": "",
                "desc": "",
                "item_type": "testcase_case",
                "library_uuid": self.library.library_uuid,
                "module_uuid": self.library.library_modules_uuid,
                "name": testcaseName,
                "priority": "SR3FtRES", # private: YT5sqbC1  dev: SR3FtRES
                "related_wiki_page": [],
                "steps": [],
                "testcase_case_steps": [],
                "type": "XN49jUUV",  #private:L2HJXEQw  dev:XN49jUUV
                "testcase_library": self.library.library_uuid,
                "testcase_module": self.library.library_modules_uuid,
                "_HaRRhb96": None
            }
        }

        response = requests.post(self.url, headers=self.login.common_header, data=json.dumps(request_payload)).json()
        # print(json.dumps(response, ensure_ascii=False, indent="\t"))

        self.response = response
        print(threading.current_thread().getName())


if __name__ == '__main__':

    login = auth.Login()

    testcaseFieldConfigs = testcaseFieldConfigs.TestcaseFieldConfigs(login)
    testcaseFieldConfigs.getTestcaseFieldConfigs()

    library = testcase_library.TestcaseLibrary(login)
    library.sendRequest(libraryName="20000", field_config_uuid=testcaseFieldConfigs.testcaseFieldConfigs_uuid)

    testcase = Testcase(login=login, library=library)
    # testcase.sendRequest(testcaseName="a")
    # print(json.dumps(testcase.response, ensure_ascii=False, indent="\t"))


    for i in range(20000):
        threading.Thread(target=testcase.sendRequest, kwargs={"testcaseName":str(i)}).start()



