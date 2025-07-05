import json

def remember(question, answer):
    try:
        with open("memory.json", "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append({"q": question, "a": answer})
    with open("memory.json", "w") as f:
        json.dump(data, f, indent=2)

def recall():
    with open("memory.json", "r") as f:
        return json.load(f)
