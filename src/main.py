import os
from typing import Any
import argparse
import time

parser = argparse.ArgumentParser("promptizer")
parser.add_argument("path", help="the source code file path", type=str)
args = parser.parse_args()


def get_file_content(file_path: str) -> None:
    data = ''
    with open(file_path, 'r') as f:
        data = f"""===\n{file_path}\n{f.read()}"""
    return data


def export_to_file(text, file_name='promptizer.txt') -> None:
    with open(file_name, 'a') as f:
        f.write(text)
    return


def traverse_path(active_directory: str) -> list[str] | str:
    if os.path.isfile(active_directory):
        return active_directory

    folder_content: list[str | list[str]] = [traverse_path(os.path.join(active_directory, content))
                                             for content in os.listdir(active_directory)]

    return folder_content


def flattened_list(traversed_list=list[Any], flat_list=None) -> list[str]:
    if flat_list == None:
        flat_list = []

    for item in traversed_list:
        if type(item) == type(''):
            flat_list.append(item)
        else:
            flattened_list(item, flat_list)

    return flat_list


traversed: list[str] = traverse_path(args.path)

all_files = flattened_list(traversed)

for file in all_files:
    try:
        print(get_file_content(file))
        export_to_file(get_file_content(file))
    except UnicodeDecodeError as e:
        continue
