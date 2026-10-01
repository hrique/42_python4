#!/usr/bin/env python3

import sys
import typing


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
    print("---\n")
    print(f.read())
    print("\n---")
    f.close()
    print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
