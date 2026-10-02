#!/usr/bin/env python3

import sys
import typing


def read_data(f: typing.IO[str]) -> str | None:
    try:
        data = f.read()
    except UnicodeDecodeError as e:
        print(f"Error reading binary file: '{f.name}': {e}")
        return None
    return data


def transform_data(data: str) -> str:
    new_data = data.split("\n")
    for i in new_data:
        if i != "":
            i = i + "#"
    data = "\n".join(new_data)
    return data 


def show_data(data: str) -> None:
    print("---\n")
    print(data)
    print("\n---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1])
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    data = read_data(f)
    f.close()
    if data is None:
        return
    show_data(data)
    print(f"File '{sys.argv[1]}' closed.\n")
    new_data = transform_data(data)
    print("Transform data:")
    show_data(new_data)
    filename = input("Enter new file name (or empty): ")
    if filename is None:
        print("Not saving data.")
        return
    print(f"Saving data to '{filename}'")
    filename.write(new_data)


if __name__ == "__main__":
    main()
