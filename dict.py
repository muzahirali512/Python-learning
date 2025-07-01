
make_dict = {

    "group" : ["students", "teachers", "general employes", "volentiers"],
    "age": [30, 48, 30, 20],
    "address": {"city": "washington", "zipcode": 300}
}

#new_dic = {"marks": 100, "position":1}#

print(make_dict)
print(make_dict.keys())
print(make_dict.values())
print(make_dict.get("group"))

new_dic = {"marks": 100, "position":1}
make_dict.update(new_dic)
print(make_dict)



