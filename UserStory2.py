import json
with open('DataJson.json') as data_file:
    data = json.load(data_file)
task=data["task"]
print(task)
deadline=data["deadline"]
print(deadline)
hours spend=data["hours spend"]
print(hours spend)
priority=data["priority"]
print(priority)
