import json
emp_json= '''{
    "eid":"101",
    "ename":"rahul",
    "avail":true,
    "loc":"undefined",
    "esal":null
}'''
print(emp_json)
emp_json=json.dumps(emp_json)
print(type(emp_json))
print(emp_json)