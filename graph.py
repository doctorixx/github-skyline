import json

with open("doctorixx.json") as f:
    data = json.loads(f.read())

print(len(data['contributions']))

mesh = [[0] * 53 for _ in range(7)]

[print(x) for x in mesh]
print("_" * 50)

for i, value in enumerate(data['contributions']):
    x = i // 7
    y = i % 7

    mapper = {
        0: " ",
        1: ".",
        2: "+",
        3: "O",
        4: "@"
    }

    mesh[y][x] = mapper[value['level']]
    # mesh[y][x] = value['level']

for x in mesh:
    print("\n", end="")
    for f in x:
        print(f, end=" ")
# print("_" * 50)
