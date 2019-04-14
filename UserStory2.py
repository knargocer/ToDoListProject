import json
def main():

    data = {}
    data['UserData2'] = []
    data['UserData2'].append({
        'number': 1,
        'question':'What are the tasks you need to accomplish ?',
        'answer':'Programming project'
    })

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

main()
