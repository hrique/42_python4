#!/bin/usr/env python3

import sys


def read_data(filename: str) -> str | None:
    try:
        f = open(filename, "r")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return None
    try:
        data = f.read()
    except (OSError, UnicodeDecodeError) as e:
        sys.stderr.write(f"[STDERR] Error reading file: '{f.name}': {e}\n")
        return None
    finally:
        f.close()
    return data


def transform_data(data: str) -> str:
    lines = data.split("\n")
    new_data = []
    for line in lines:
        if line != "":
            new_data.append(f"{line}#")
        else:
            new_data.append(line)
    data = "\n".join(new_data)
    return data


def show_data(data: str) -> None:
    print("---\n")
    print(data)
    print("---")


def save_file(filename: str, data: str) -> None:
    print(f"Saving data to '{filename}'")
    try:
        new_file = open(filename, "w")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    try:
        new_file.write(data)
    except OSError as e:
        print(f"Error saving file '{filename}': {e}")
        return
    finally:
        new_file.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    data = read_data(sys.argv[1])
    if data is None:
        return
    show_data(data)
    print(f"File '{sys.argv[1]}' closed.\n")
    print("Transform data:")
    new_data = transform_data(data)
    show_data(new_data)
    new_file = input("Enter new file name (or empty): ")
    if new_file:
        save_file(new_file, new_data)
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
