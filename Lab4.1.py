import json


def task() -> float:
    with open('input.json', "r") as input_file:
        data = json.load(input_file)
        list_of_multiplies = []
        for dict in data:
            result = 1
            for value in dict.values():
                result *= value
            list_of_multiplies.append(result)
        return round(sum(list_of_multiplies), 3)

print(task())
