import jsonschema
import json
from jsonschema import validate

def usr_input():
    new_device_tmp = {}
    
    while True:
        try:
            new_device_tmp['name'] = input("enter a name of the device ")
            if not new_device_tmp['name']:
                raise ValueError("a name dont can empty")
            
            new_device_tmp['os'] = input("enter the os name ")
            if not new_device_tmp['os']:
                raise ValueError("a os dont can empty")
            
            new_device_tmp['cpu'] = input("enter the cpu ")
            if not new_device_tmp['cpu']:
                raise ValueError("a cpu dont can empty")
            
            new_device_tmp['ram'] = int(input("enter the go of ram in number "))
            if new_device_tmp['ram'] <= 0:
                raise ValueError("a ram can empty and you need enter number int")
    
            return new_device_tmp
        
        except ValueError as e:
            print(f"ERROR : {e}. pleas enter a data valid")
        except ValueError:
            print("please enter a number int")

new_device = usr_input()
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "os": {"type": "string"},
        "cpu": {"type": "string"},
        "ram": {"type": "integer"},
    },
    "required": ["name", "os", "cpu", "ram"]
}

try:
    with open("configs/instances.json", "a") as f:
        json.dump(new_device, f, indent=4)
    print("Succès !!")
except jsonschema.exceptions.ValidationError as e:
    print(f"Erreur : {e.message}")
