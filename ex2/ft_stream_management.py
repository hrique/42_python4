#!/usr/bin/env python3

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
    sys.stdout.write("---\n\n")
    sys.stdout.write(f"{data}\n")
    sys.stdout.write("---\n")


def save_file(filename: str, data: str) -> bool:
    sys.stdout.write(f"Saving data to '{filename}'\n")
    try:
        new_file = open(filename, "w")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return False
    try:
        new_file.write(data)
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error saving file '{filename}': {e}\n")
        return False
    finally:
        new_file.close()
    return True


def main() -> None:
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_stream_management.py <file>\n")
        return
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{sys.argv[1]}'\n")
    data = read_data(sys.argv[1])
    if data is None:
        return
    show_data(data)
    sys.stdout.write(f"File '{sys.argv[1]}' closed.\n\n")
    sys.stdout.write("Transform data:\n")
    new_data = transform_data(data)
    show_data(new_data)
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline()
    new_file = new_file.rstrip()
    if new_file:
        if save_file(new_file, new_data):
            sys.stdout.write(f"Data saved in file '{new_file}'.\n")
        else:
            sys.stdout.write("Data not saved.\n")
    else:
        sys.stdout.write("Not saving data.\n")


if __name__ == "__main__":
    main()
