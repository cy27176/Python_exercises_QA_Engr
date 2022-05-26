import json


ROOT_PATH = '/Users/Lenovo/Downloads/Python_exercises_QA_Engr (5)/Updated_Python_exercises_QA_Engr'


def read_file(file_path):
    f = open(file_path)
    return json.load(f)


def remove_element(json_data, json_element):
    for key in json_data.keys():
        if key == json_element:
            del json_data[key]
            break  
        elif type(json_data[key]) == dict:
            json_data[key] = remove_element(json_data[key], json_element)  # recursive to go deeper

    return json_data


def remove_json_element_with_entire_data(json_data, json_element):
    for key, value in json_data.items():
        if key == json_element.keys()[0] and value == json_element[json_element.keys()[0]]:
            del json_data[key]
            break  # data matched , so break loop
        elif type(json_data[key]) == dict:
            json_data[key] = remove_element(json_data[key], json_element)  # recursive to go deeper

    return json_data


def write(file_path, json_data):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)
        outfile.flush()
        outfile.close()

def test():
    json_data = read_file(ROOT_PATH + '/test_payload.json')
    json_data = remove_element(json_data=json_data, json_element='outParams')
    write(file_path=ROOT_PATH + '/test_payload_output.json', json_data=json_data)

test()
