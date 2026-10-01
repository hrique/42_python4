#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1])
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    try:
        data = f.read()
        print("---\n")
        print(data)
        print("\n---")
    except UnicodeDecodeError as e:
        print(f"Error reading binary file: '{sys.argv[1]}': {e}")
        return
    finally:
        f.close()
    print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
