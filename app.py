import json
JSON_FILE = 'tasks.json'

def create_data(name):
    # Example new data to append
    data = {
        "name": name
    }
    return data

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

def main():
    new_data = create_data("Emir")
    data = readfile(JSON_FILE)
    data.append(new_data)
    write_file(data, JSON_FILE)

if __name__ == '__main__':
    main()