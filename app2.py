import json
JSON_FILE = 'data.json'

def create_data(name, age):
# Example new data to append
    new_data = {
        "name": name,
        "age": age,
    }
    return new_data
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
    
def write_data(data, json_file):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


# Step 2: Append the new data to the existing JSON object (assuming it's a list)
data = readfile(JSON_FILE)
new_data = create_data("Emir", 24)
data.append(new_data)
write_data(new_data, JSON_FILE)

# Step 3: Write the updated JSON object back to the file
