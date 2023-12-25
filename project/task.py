# Task management system

#points
# - invoke user to input task 
# - unvoke the user to input the task until user inputs 'Exit' String
# - once user exit the task input,print the task items
tasks = []

while True:
    item = input("Enter your task: ")
    
    if item.upper== 'exit':
        break
    
    tasks.append(item)

print("Your tasks are:")
for task in tasks:
    print(task)


# if tasks==exit:
#     print (tasks)
