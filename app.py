import json
JSON_FILE = 'tasks.json'

def create_data(name):
    # Example new data to append
    data = {
        "name": name
    }
    return data

# Step 1: Read the existing JSON data from the file
def readfile(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            if data is None:
                return []
            return data
    except:
        return []
    
def write_file(json_file):
    # Step 3: Write the updated JSON object back to the file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_task(data, json_file):
    new_data = create_data("Emir")
    data = readfile(json_file)
    data.append(new_data)
    write_file(json_file)

# Step 2: Append the new data to the existing JSON object (assuming it's a list)
new_data = create_data("Emir")
data = readfile(JSON_FILE)
data.append(new_data)
write_file(JSON_FILE)

