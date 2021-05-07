import requests
import json
import auth

class TestcaseFieldConfigs():

    def __init__(self, login):

        self.url = login.server_url + '/team/' + login.team_uuid + '/items/graphql'
        self.login = login

    def getTestcaseFieldConfigs(self):

        # graphql的小括号是用来做限制的，例如降序升序
        query = """query QUERY_TEST_CASE_FIELD_CONFIG_LIST {
            testcaseFieldConfigs(orderBy: {isDefault: DESC, namePinyin: ASC}) {
                key
                uuid
                name
                namePinyin
                isDefault
                testcaseLibraries {
                    uuid
                    name
                    __typename
                }
                __typename
            }
        }
        """

        response = requests.post(self.url, json={"query": query}, headers=self.login.common_header).json()

        self.response = response
        self.testcaseFieldConfigs_uuid = response["data"]["testcaseFieldConfigs"][0]["uuid"]

    def getField(self):
        # query = "query QUERY_LIBRARY_TESTCASE_EDIT(\n  $fieldFilter:Filter,\n  $moduleFilter: Filter,\n  $orderBy:Filter\n  ){\n  fields(\n  filter:$fieldFilter,\n  orderBy:$orderBy\n ){\n   aliases,\n   name,\n   uuid,\n   namePinyin,\n   fieldType,\n   key,\n   defaultValue,\n   createTime,\n   hidden,\n   required,\n   canUpdate,\n   builtIn,\n   allowEmpty,\n   options {\n     uuid,\n     value,\n     color,\n     bgColor\n   },\n}\n  \n  testcaseModules(\n    filter:$moduleFilter,\n    groupBy:{\n      testcaseLibrary:{}\n    },\n    orderBy: {\n      isDefault: ASC,\n      position: ASC\n    }\n  ){\n    uuid,\n    name,\n    path,\n    createTime,\n    isDefault,\n    position,\n    key,\n    testcaseCaseCount,\n    testcaseLibrary{\n      key,\n      uuid,\n      name,\n      testcaseCaseCount,\n    },\n    parent{\n      uuid,\n      name,\n      path,\n      createTime,\n      isDefault,\n      position,\n      key\n    }\n  }\n}"

        requestPayload = {
    "query": "query QUERY_LIBRARY_TESTCASE_EDIT(\n  $fieldFilter:Filter,\n  $moduleFilter: Filter,\n  $orderBy:Filter\n  ){\n  fields(\n  filter:$fieldFilter,\n  orderBy:$orderBy\n ){\n   aliases,\n   name,\n   uuid,\n   namePinyin,\n   fieldType,\n   key,\n   defaultValue,\n   createTime,\n   hidden,\n   required,\n   canUpdate,\n   builtIn,\n   allowEmpty,\n   options {\n     uuid,\n     value,\n     color,\n     bgColor\n   },\n}\n  \n  testcaseModules(\n    filter:$moduleFilter,\n    groupBy:{\n      testcaseLibrary:{}\n    },\n    orderBy: {\n      isDefault: ASC,\n      position: ASC\n    }\n  ){\n    uuid,\n    name,\n    path,\n    createTime,\n    isDefault,\n    position,\n    key,\n    testcaseCaseCount,\n    testcaseLibrary{\n      key,\n      uuid,\n      name,\n      testcaseCaseCount,\n    },\n    parent{\n      uuid,\n      name,\n      path,\n      createTime,\n      isDefault,\n      position,\n      key\n    }\n  }\n}",
    "variables": {
        "fieldFilter": {
            "hidden_in": [
                False
            ],
            "pool_in": [
                "testcase"
            ],
            "context": {
                "type_in": [
                    "testcase_field_config"
                ],
                "fieldConfigUUID_in": [
                    "3BWci2q7"
                ]
            }
        },
        "moduleFilter": {
            "testcaseLibrary_in": [
                "H3hEkVvS"
            ]
        },
        "orderBy": {
            "createTime": "ASC"
        }
    }
}

        response = requests.post(self.url, json=requestPayload, headers=self.login.common_header).json()
        print(json.dumps(response, ensure_ascii=False, indent="\t"))

if __name__ == '__main__':

    login = auth.Login()
    testcaseFieldConfig = TestcaseFieldConfigs(login)
    # testcaseFieldConfig.getTestcaseFieldConfigs()
    testcaseFieldConfig.getField()