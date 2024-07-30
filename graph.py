import datetime
import json

with open("doctorixx.json") as f:
    data = json.loads(f.read())

print(len(data['contributions']))

mesh = [[0] * 54 for _ in range(7)]

[print(x) for x in mesh]
print("_" * 50)

first_day = list(map(int, data['contributions'][0]["date"].split("-")))
fdate = datetime.date(first_day[0], first_day[1], first_day[2])

shift = fdate.isoweekday()
print(shift)

for i, value in enumerate(data['contributions']):
    x = (i + shift) // 7
    y = (i + shift) % 7

    mapper = {
        0: " ",
        1: ".",
        2: "+",
        3: "O",
        4: "@"
    }

    # mesh[y][x] = mapper[value['level']]
    mesh[y][x] = value['count']

print(mesh)

for x in mesh:
    print("\n", end="")
    for f in x:
        print(f, end=" ")
# print("_" * 50)
