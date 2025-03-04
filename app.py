import json
import sys
from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

JSON_FILE = 'tasks.json'

def create_task(id, description, status="todo", createdAt=formatted_time, updatedAt=None):
    # Example new data to append
    task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    }
    print("task created successfully.")
    return task

def find_max_id(data):
    try: 
        max_id = max(item.get("id") for item in data) 
        return max_id
    except:
        return 0
    
def update_task(json_file, data, id, update):      
        id_found = False
        for d in data:
            if d.get("id") == id:
                id_found = True
                d["description"] = update
                d["updatedAt"] = formatted_time
        if id_found == True:
            print(f"task id: {id} - updated")
        else:
            print(f"id {id} - not found")
        write_file(data, json_file)

def delete_task(json_file, id):
    new_data = []
    data = readfile(JSON_FILE)
    for d in data:
        if d.get("id") != id:
            id_found = True
            new_data.append(d) 
        else:
            print(f"task id {id} - deleted") # task "task_name" deleted
    if (len(new_data) == len(data)):
        print(f"id ({id}) not found")
    write_file(new_data, json_file)

def change_status(json_file, id, new_status):
    updated = False
    data = readfile(json_file)
    for d in data:
        if d.get("id") == id:
            d["status"] = new_status
            d["updatedAt"] = formatted_time
            updated = True
    if updated:
        write_file(data, json_file)
        print(f"status changed | id: {id}, status: {new_status}")
    else:
        print(f"no such id ({id}) in tasks")

def search_status(status, json_file):
    data = readfile(json_file)
    status_list = []
    for d in data:
        if d.get("status") == status:
            status_list.append(d)
    if status_list == []:
        print(f"no tasks with the status: {status}")
    else:    
        status_list = json.dumps(status_list, indent=4)
        print(status_list)

def readfile(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            if data is None:
                return []
            return data
    except:
        return []

def write_file(data, json_file):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def main(command):
    if command.lower() == "add":
        data = readfile(JSON_FILE)
        id = find_max_id(data) + 1
        new_data = create_task(id, sys.argv[2])
        data.append(new_data)
        write_file(data, JSON_FILE)

    elif command.lower() == "update":
        data = readfile(JSON_FILE)
        id = int(sys.argv[2])
        update = sys.argv[3]
        update_task(JSON_FILE, data, id, update)

    elif command.lower() == "delete":
        id = int(sys.argv[2])
        delete_task(JSON_FILE, id)

    elif command.lower() in ("mark-todo", "mark-in-progress", "mark-done"):
        id = int(sys.argv[2])
        new_status = sys.argv[1]
        status = new_status[5:]
        change_status(JSON_FILE, id, status)

    
    elif len(sys.argv) > 2 and sys.argv[2].lower() in ("done", "todo", "in-progress"):
        status = sys.argv[2]
        search_status(status, JSON_FILE)        
        
    elif command.lower() == "list" and len(sys.argv) == 2:
            # print all tasks
            data = readfile(JSON_FILE)
            data = json.dumps(data, indent=4)
            print(data)
    
    elif command.lower() == "delete_all":
        print("are you sure you want to delete all tasks? (Y/n)")
        selection = input()
        if selection.lower() == 'y':                
            data = []
            write_file(data, JSON_FILE)
            print("all tasks deleted.")
        else:    
            print("tasks NOT deleted.")

    else:
        # unknown command
        print("""
              no such command.
              commands available:
              - add "task_desc"
              - update task_id
              - delete task_id
              - mark-todo, mark-in-progress, mark-done
              - list
              - list todo, list done, list in-progress 
              - delete_all
              """)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        main(command)