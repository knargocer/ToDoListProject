def setupTask():
    task = int(input('Please, insert the task'))
    return(task)

def setupDate():
    date = int(input('Please, insert the deadline in the format DD/MM/YYYY'))
    return (date)

def setupPriority():
    priority = int(input('Please, insert the priority of the task, from 1 to 5'))
    while priority>5 and priority<1:
        print ("Please, insert a priority from 1 - 5")
    else:
        return(priority)
