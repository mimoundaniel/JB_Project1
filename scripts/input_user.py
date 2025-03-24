import jsonschema
import json
from jsonschema import validate

def usr_input():
    new_device_tmp = {}
    while True :
        # new_device_tmp['name'] = "device 2"
        # new_device_tmp['os'] = "windows 11"
        # new_device_tmp['cpu'] = "inter core 7"
        # new_device_tmp['ram'] = int(76)

        new_device_tmp['name'] = input("Enter a name of the new device: ")
        if not new_device_tmp['name']:
            raise ValueError("a name cant be empty")
        new_device_tmp['os'] = input("Enter OS (Ubuntu/CentOS): ")
        if not new_device_tmp['os']:
            raise ValueError("a os cant be empty")
        new_device_tmp['cpu'] = input("Enter CPU (e.g., 2vCPU): ")
        if not new_device_tmp['cpu']:
            raise ValueError("a cpu cant be empty")
        new_device_tmp['ram'] = int(input("Enter RAM (e.g., 4GB): "))
        if not new_device_tmp['ram']:
            raise ValueError("a name cant be empty")
        
        except ValueError as e:
            # Si une erreur se produit, afficher un message et redemander l'entrée
            print(f"Erreur : {e}. Veuillez entrer des valeurs valides.")
        except ValueError:
            print("Veuillez entrer un nombre pour la RAM.")

        return new_device_tmp

# Schéma de validation
new_device = usr_input()
schema = {
    "type": "object",
    "properties": {
        "name":{"type" : "string"},
        "os": {"type": "string"},
        "cpu": {"type": "string"},
        "ram": {"type": "integer"},
    },
    "required": ["name","os", "cpu", "ram"]
}
# Validation
try:
    with open("configs/instances.json", "a") as f:
        f.write("\n")
        json.dump(new_device, f, indent=4)
    print("sucsess !!")
except jsonschema.exceptions.ValidationError as e:
    print(f"Erreur : {e.message}")
