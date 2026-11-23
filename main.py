import sys

if len(sys.argv) < 2:
    print("Please provide a command.")
else:
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("please provide a task description")
        else:    
            description = sys.argv[2]

            task = {
                "id" : 1,
                "descriotion" : description,
                "status" : "todo"
            }
            print(task)

    elif command == "list":
        print("You selected LIST")

    else:
        print("Unknown command")