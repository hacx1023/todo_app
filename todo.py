import json, os, sys

FILE = "tasks.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(tasks):
    json.dump(tasks, open(FILE, "w"), indent=2)

tasks = load()

if len(sys.argv) < 2:
    print("Usage: python todo.py <add/list/remove> [task]")
    exit()

cmd = sys.argv[1]

if cmd == "add":
    task = " ".join(sys.argv[2:])
    tasks.append(task)
    save(tasks)
    print("Added:", task)

elif cmd == "list":
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")

elif cmd == "remove":
    idx = int(sys.argv[2]) - 1
    tasks.pop(idx)
    save(tasks)
    print("Removed task", idx+1)
