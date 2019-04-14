import json
def main():

    with open('data.txt') as json_file:
        data = json.load(json_file)

    UserStory2= data["UserStory2"]

    print("0: to answer new topic")
    print("1: to see a previous answer")
    print("2: to answer again a question")

    user_choice = int(input(""));

    if user_choice == 0:
        user_question = input("please insert a task.")

        data['UserStory2'].append({
            'number': 1,
            'task':user_task,
            'answer': ""
        })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

    elif user_choice == 1:

        task_answer = data['UserStory2']


        for object in questions_answer:
            print(object)


    elif user_choice == 2:

        task_answer = data['UserStory2']


        for object in questions_answer:
            print(object)


        number_of_tasks = input ("enter the number of tasks you want to accomplish?")
        task_answer = input("Please enter the ask you want to accomplish")
        answer_to_question = input("Enter the name of the task.")
        deadline_question = input("Enter the deadline of the task")
        time_question = input("Enter the time it will take to accomplish it")
        answer = {'Number': number_of_tasks,
                  'Task': task_answer,
                  'Answer': answer_to_question,
                  'Deadline': deadline_question,
                  'Time': time_question}


        data['UserStory2'].remove(
            questions_answer[int(number_of_task) - 1]
        )

        data['UserStory2'].append({
            'number': int(next(iter(object.values()))),
            'question': question_to_answer,
            'answer': answer_to_question
        })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
