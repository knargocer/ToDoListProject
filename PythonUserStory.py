import json

def new_task();
    with open("DataJson.json") as data:
        data_dict = json.load(data)
        data.write(json.dumps(data_dict))
        
def task_modifaction():
    with open("DataJson.json") as data:
            data_dict = json.load(data)
            if (data_dict):
                print("File exists:")
            task_answer = input("Please enter the task you want to modify")
            json_load['tasks'][task_answer]['deadline'] = input("Enter the deadline of the task")
            json_load['tasks'][task_answer]['Time'] = input("Enter the time it will take to accomplish it")
            answer = {'Task': task_answer,
                      'Deadline': deadline_question,
                      'Time':  time_question}

            data['DataJson.json'].remove(
                task_answer[int(tasks) - 1]
            )

            data['DataJson.json'].append({
                'Task': int(next(iter(object.values()))),
                'Deadline': deadline_question,
                'Time': time_question
            })

            with open('data.json', 'w') as outfile:
                outfile.write(json.dump(data, outfile))
                
        else :
            print("file does not exist")
            return user_data

def see_all_tasks():
    with open("DataJson.json") as data:
        data_dict = json.load(data)



def main():

    with open('data.txt') as DataJson:
        data_dict = json.load(DataJson.json)

    DataJson= data["DataJson"]

    print("0: To fill in a new task")
    print("1: To see a all tasks")
    print("2: To modify the previous task")

    user_choice = int(input(""));

    if user_choice == 0:
        user_question = input("Please insert a new task")

        data['DataJson'].append({
            "Task1": "",
            "Deadline": "",
            "Hours spend": ""
        })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

    elif user_choice == 1:

        task_answer = data['DataJson']

        for object in questions_answer:
            print(object)


    elif user_choice == 2:

        task_answer = data['DataJson']


        for object in json_load['tasks'].keys():
            print(object)
