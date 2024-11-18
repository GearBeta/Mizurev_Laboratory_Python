import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Читаем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as input_f:
        reader = csv.DictReader(input_f)
        data = [row for row in reader]

    # Сериализуем данные в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as output_f:
        json.dump(data, output_f, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

