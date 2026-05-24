import json

data = {
    "name": "Raj",
    "age": 17
}

json_data = json.dumps(data)

print(json_data)