import json

# TODO решите задачу
def task() -> float:
    file = 'input.json'
    c = 0
    with open(file) as f:
        data = json.load(f)
        for i in range( len(data)):
            c += data[i]['score'] * data[i]['weight']
    return f"{c:.3f}"


print(task())
