import json 
import os

def import_users(user_locations="/backEnd/users/users.json"):
    print("importing users")
    output = {}
    if os.path.isfile(user_locations):
        with open(user_locations, 'r') as file:
            output = json.load(file)
    else:
        print("there are not recorded users")
        
    return output

def export_users(users, user_locations="/backEnd/users/users.json"):
    print("exporting users")
    with open(user_locations, 'w') as json_file:
        json.dump(users, json_file, indent=4)