# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
li = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']
gl=[]
def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        data ={}
        i=0
        # Чтение данных
        for row in reader:
            gl.append(row)
            #print(row['longitude'], row['latitude'], row['housing_median_age'], row['total_rooms'], row['total_bedrooms'], row['population'], row['households'], row['median_income'], row['median_house_value'])
    ...  # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, 'w') as out:
        out.write(json.dumps(gl, indent=4))
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
