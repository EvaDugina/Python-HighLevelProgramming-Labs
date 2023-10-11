import argparse
import json
import os.path

# storage.py --key key_name --val value
# storage.py --key key_name

# --key <имя ключа>, где <имя ключа> - ключ по которому сохраняются/получаются значения
# --val <значение>, где <значение> - сохраняемое значение.

# ВЫВОД ПО КЛЮЧУ: value_1, value_2 или None
import os

FILE_NAME = "storage.json"


def work(key=None, value=None):
    if key is None:
        print("Invalid arguments!")

    if not os.path.exists(FILE_NAME):
        create_file()

    if value is None:
        print(get_value(key))
    else:
        set_value(key, value)


def get_value(key):
    text = get_file_contents()
    if text:
        data = json.loads(text)
        index = find_key(key, data)
        if index != -1:
            return ", ".join(data[index].get(key))
        else:
            return "None"
    else:
        return "None"


def set_value(key, value):
    text = get_file_contents()
    if text:
        data = json.loads(text)
        index = find_key(key, data)
        if index != -1:
            data[index].get(key).append(value)
        else:
            data.append({key: [value]})
        new_text = json.dumps(data)
    else:
        new_text = json.dumps([{key: [value]}])

    put_file_contents(new_text)


def find_key(key, data):
    for index, element in enumerate(data):
        if element.get(key) is not None:
            return index
    return -1


def create_file():
    with open(FILE_NAME, "w") as f:
        f.write("")
        f.close()
        # json.dump("", write_file)

def get_file_contents():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        text = file.read()
        file.close()
    return text

def put_file_contents(text):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write(text)
        file.close()


parser = argparse.ArgumentParser(description="Task №6", exit_on_error=False)
parser.add_argument('--key', dest="key", type=str)
parser.add_argument('--val', dest="value", type=str)

if __name__ == "__main__":
    try:
        args = parser.parse_args()
        work(args.key, args.value)
    except argparse.ArgumentError:
        print("Invalid arguments!")


