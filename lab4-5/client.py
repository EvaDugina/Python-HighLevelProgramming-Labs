import argparse
import asyncio
import aiohttp
import csv
import json

PATH = "output.csv"


def csv_write(html_response):
    html_response = json.loads(html_response)

    if "labs" not in html_response:
        return print("Нет лаб")

    with open(PATH, mode="w+", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter="\t", lineterminator="\r")
        file_writer.writerow(["Название лабораторной работы", "Срок выполнения"])
        for lab_name in html_response['labs'].keys():
            file_writer.writerow([lab_name, html_response['labs'][lab_name]['deadline']])


async def main(method=None, link=None):
    async with aiohttp.ClientSession() as session:
        html = ""
        match str(method).upper():
            case "GET":
                async with session.get(link) as response:
                    html = await response.text()
                    print(html)
            case "POST":
                async with session.post(link) as response:
                    html = await response.text()
                    print(html)
            case "DELETE":
                async with session.delete(link) as response:
                    html = await response.text()
                    print(html)
            case "PATCH":
                async with session.patch(link) as response:
                    html = await response.text()
                    print(html)
            case _:
                return print("Неизвестный метод...")
        csv_write(html)


parser = argparse.ArgumentParser(description="")

parser.add_argument("--method", dest="method", type=str)
parser.add_argument("--link", dest="link", type=str)

args = parser.parse_args()

asyncio.run(main(args.method, args.link))
