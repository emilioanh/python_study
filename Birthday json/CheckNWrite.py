import json

def list_entries():
    with open("scientist_birthdays.json", "r") as f:
        info = json.load(f)
    print("We have the following peoples' birthday:")
    for key in info:
        print(key)

def add_entry(entry):
    with open("scientist_birthdays.json", "w") as f:
        json.dump(entry, f, indent=4)
        f.write('\n')

if __name__ == "__main__":
    data = {}
    with open("scientist_birthdays.json", "r") as f:
        data = json.load(f)
    # list_entries()
    # data["shit"] = "con cac"
    # add_entry(data)
    # list_entries()
