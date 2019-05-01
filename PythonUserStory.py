import json
print("This is your ToDo list helper. It will help you organize your tasks. Please fill in the information bellow")

def new_task():
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
            new_answer = {'Task': task_answer,
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
                else:
                print("file does not exist")
                return user_data

def see_all_tasks():
    with open("DataJson.json") as data:
        data_dict = json.load(data)

        for object in DataJson.json:
            print(object)


def main():

    with open('data.txt') as DataJson:
        data_dict = json.load(DataJson.json)

    DataJson= data["DataJson.json"]

    print("0: To fill in a new task")
    print("1: To see a all tasks")
    print("2: To modify the previous task")

    user_choice = int(input(""));

    if user_choice == 0:
        user_question = input("Please insert a new task")


        data['DataJson.json'].append({
            "Task1": "",
            "Deadline": "",
            "Hours spend": ""
        }

        return new_task()

    elif user_choice == 1:

        task_answer = data['DataJson']
        return see_all_tasks()

    elif:
        user_choice == 2

        task_answer = data['DataJson']

        return task_modifaction()
        
    else :
        print("Please type 0, 1 or 2")
        exit
        
main()
