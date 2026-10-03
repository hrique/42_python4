#!/usr/bin/env python3

import sys
import typing


def read_data(filename: str) -> str | None:
    try:
        f = open(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    try:
        data = f.read()
        show_data(data)
    except UnicodeDecodeError as e:
        print(f"Error reading binary file: '{f.name}': {e}")
        return None
    finally:
        f.close()
    print(f"File '{filename}' closed.\n")
    return data


def transform_data(data: str) -> str:
    data = data.split("\n")
    new_data = []
    for line in data:
        if line != "":
            new_data.append(f"{line}#")
        else:
            new_data.append(line)
    data = "\n".join(new_data)
    show_data(data)
    return data


def show_data(data: str) -> None:
    print("---\n")
    print(data)
    print("\n---")


def save_file(filename: str, data: str) -> None:
    print(f"Saving data to '{filename}'")
    try:
        new_file = open(filename, "w")
        new_file.write(data)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    new_file.close()
    print(f"Data saved in file '{filename}'")




def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    data = read_data(sys.argv[1])
    if data is None:
        return
    print("Transform data:")
    new_data = transform_data(data)
    new_file = input("Enter new file name (or empty): ")
    if new_file is None:
        print("Not saving data.")
        return
    else:
        save_file(new_file, new_data)


if __name__ == "__main__":
    main()
