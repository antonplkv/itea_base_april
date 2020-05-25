import json
JSON_FILE_NAME = 'data.json'
# my_obj = {'title': 30, 'price': 100, 'quantity': 20}
#
# print(type(my_obj))
# print(my_obj)
# result = json.dumps(my_obj)
#
# print(type(result))


# qwe = '{"title": 30, "price": 100, "quantity": 20}'
#
# result = json.loads(qwe)
#
# print(result['title'])

my_obj = {'title': 30, 'price': 100, 'quantity': 20}

def write_to_json_file():
    file_json = open(JSON_FILE_NAME, 'a')
    json.dump(my_obj, file_json)
    file_json.close()

def read_from_json_file():
    file_json = open(JSON_FILE_NAME, 'r')
    res = json.load(file_json)
    file_json.close()
    print(res)
