import auth
import requests
import json
import time

# 批量更改工作项状态
class Work():

    def __init__(self):
        self.login = auth.Login("saas")

    def searchSprintTask(self, project=None, sprint=None):
        url = self.login.server_url + '/team/' + self.login.team_uuid + '/items/graphql'
        print(url)
        query = '''
        {
          buckets(
            groupBy: { tasks: {} }
            pagination: { limit: 50, after: "", preciseCount: true }
          ) {
            tasks(
              filterGroup: [
                { project_in: ["%s"], sprint_in: ["%s"] }
              ]
              
            ) {
                name
                uuid
                status{
                    uuid
                    name
                }
            }
          }
        }
        ''' %(project, sprint)

        response = requests.post(url, json={"query": query}, headers=self.login.common_header).json()

        return response


    def getTargetTask(self, response=None, target_status_uuid=None):

        # 获取目标状态的 tasks_uuid
        tasks = response["data"]["buckets"][0]["tasks"]
        tasks_uuid = []
        for task in tasks:
            if task["status"]["uuid"] == target_status_uuid:
                tasks_uuid.append(task["uuid"])

        print(tasks_uuid)
        return tasks_uuid


    def changeTaskStatus(self, tasks_uuid=None, transition_uuid=None, conent=None):
        for task_uuid in tasks_uuid:
            url = self.login.server_url + '/team/' + self.login.team_uuid + '/task/' + task_uuid + '/new_transit'
            request_payload = {
                "transition_uuid":transition_uuid,
                "field_values":[
                    {
                        "field_uuid":"84csfh5u",
                        "type":2,
                        "value":conent
                    },
                    {
                        "field_uuid":"CgptJML3",
                        "type":6,
                        "value":int(time.time())
                    }
                ],
                "manhours":[

                ],
                "resource_uuids":[

                ],
                "wiki_pages":{
                    "related":[

                    ],
                    "deletion":[

                    ]
                }
            }
            requests.post(url, headers=self.login.common_header, data=json.dumps(request_payload)).json()

    def relatedTask(self, tasks_uuid=None, task_link_type_uuid=None, relate_task_uuid=None):
        for task_uuid in tasks_uuid:
            url = self.login.server_url + '/team/' + self.login.team_uuid + '/task/' + task_uuid + '/related_tasks'
            request_payload = {
                "task_uuids":[
                    relate_task_uuid
                ],
                "task_link_type_uuid":task_link_type_uuid,
                "link_desc_type":"link_out_desc"
            }
            requests.post(url, headers=self.login.common_header, data=json.dumps(request_payload)).json()

if __name__ == "__main__":

    project_uuid = "GL3ysesFPdnAQNIU"
    sprint_uuid = "B1rQW87c"

    testPass_uuid = "JGPxA2FE" # 测试通过工作项 UUID
    saas_transition_uuid = "UhMqQny9" # 已上线SaaS 步骤UUID
    content = "#214821 ONES v3.1.23" # 修复版本


    work = Work()

    # 查询迭代中的工作项
    response = work.searchSprintTask(project=project_uuid, sprint=sprint_uuid)
    print(json.dumps(response, ensure_ascii=False, indent="\t"))

    # 获取测试通过状态的uuid
    tasks_uuid = work.getTargetTask(target_status_uuid=testPass_uuid)
    print("测试通过状态uuid" + tasks_uuid)

    # 把测试通过状态的工单，批量改为已上线SaaS的状态，且填写版本号
    work.changeTaskStatus(tasks_uuid=tasks_uuid, transition_uuid=saas_transition_uuid, conent=content)


    # 批量关联工作项
    tasks_uuid = work.getSprintTask(project="GL3ysesFPdnAQNIU", sprint="B1rQW87c", target_status_uuid="SRrEGrTV")
    # work.relatedTask(tasks_uuid=tasks_uuid, task_link_type_uuid="UUID0001",relate_task_uuid="Tzd6R3ifpUnmZqK9")