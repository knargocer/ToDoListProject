import json
with open('Data.json') as data_file:
    data = json.load(data_file)
task=data["task"]
print(task)
daedline=data["deadline"]
print(deadline)
priority=data["priority"]
print(priority)
