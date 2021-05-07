import requests
import auth
import json

login = auth.Login()

url = login.server_url + '/team/' + login.team_uuid + '/filters/peek'

requestPayload = {
    "with_boards": False,
    "boards": None,
    "query": {
        "must": [
            {
                "must": [
                    {
                        "in": {
                            "field_values.field006": [  # 任务所属项目
                                "Tzd6R3ifSa3fKcX5"
                            ]
                        }
                    },
                    {
                        "in": {
                            "field_values.field007": [ # 任务类型
                                "GuQKgAkC"
                            ]
                        }
                    }
                ]
            },
            # {
            #     "should": [
            #         {
            #             "must": [
            #                 {
            #                     "in": {
            #                         "field_values.field004": [ # 负责人
            #                             "RGzJnspW",
            #                             "DU6krHBN"
            #                         ]
            #                     }
            #                 }
            #             ]
            #         }
            #     ]
            # }
        ]
    },
    "group_by": "",
    "sort": [
        {
            "field_values.field009": { # 创建时间
                "order": "desc"
            }
        }
    ],
    "include_subtasks": True,
    "include_status_uuid": False,
    "include_issue_type": False,
    "include_project_uuid": False,
    "is_show_derive": False
}

repsonse = requests.post(url, data=json.dumps(requestPayload), headers=login.common_header).json()
print(repsonse)