import csv
import json
from pathlib import Path
from typing import TextIO,List,Dict,Union

def write_txt_file(file_path: Path, content:List[str]) -> None:
    with open(file_path,  'w' , encoding='utf-8') as f:
        for line in content:
            f.write(line + '\n' )

def read_text_file(file_path: Path) -> List[str]:

    with open(file_path,'r',encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def write_csv_file(file_path,data):
    with open(file_path,'w',encoding='utd-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_csv_data(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def save_json(file_path, data):
    with open(file_path,'w', encoding='utf-8') as f:
        json.dump(data , f , indent= 2)

def load_json(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return json.load(f)



if __name__ == "__main__":
    txt_file = Path("data.txt")
    csv_file = Path("data.csv")
    json_file = Path("config.json")

    print(read_text_file(txt_file))
    print()
    print()
    print(read_csv_data(csv_file))
    print()
    print()
    print(load_json(json_file))