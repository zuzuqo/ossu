import json

users = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {
        "id": "009",
        "x": 7,
        "name": "Alex"
    }
]
'''

info = json.loads(users)
print(f'User count: {len(info)}')

count = 1
for i in info:
    print(f"{count} user")
    print(f"Name:\t{i['name']}")
    print(f"Id:\t\t{i['id']}")
    print(f"Attr x:\t{i['x']}")
    count += 1
