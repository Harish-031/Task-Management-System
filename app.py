tasks = []
def task():
    print("----WELCOME TO TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many task you want to add = ")) 
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} name = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been added successfully")

        elif operation == 2:
            updated_val = input("Enter task number you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up} has been updated successfully")

            elif operation == 3:
                del_val = input("Enter task number you want to delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task {del_val} has been deleted successfully")

            elif operation == 4:
                print(f"Today's tasks are\n{tasks}")

            elif operation == 5:
                print("Closing the program....")
                break

            else:
                print("Invalid input, please try again")
task()