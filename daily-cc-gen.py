import json

with open("options.json", encoding="utf-8") as json_file:
    options = json.load(json_file)

# option or exit to quit > rank > next option
data = []
while True:
    val = input("Please enter option or q to quit: ")
    if val == "q":
        break
    elif val == "list":
        print(options.keys())
    elif val in options:
        if val == "lifepoint":
            data.append({"category": val, "options": [options[val]]})
        else:
            try:
                rank = int(input("Please enter rank: "))
                data.append({"category": val, "options": [options[val][(rank - 1)]]})
            except (ValueError):
                print("Invalid rank")
                continue
    else:
        print(f"{val} option not found")


with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Done.")
