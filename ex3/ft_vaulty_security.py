#!/usr/bin/env python3


def secure_archive(filename: str, action: str "read", content: str = "") -> tuple[bool, str]:
    try:
        with open(filename) as f:
            data = f.read()
        return (True, data)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")



if __name__ == "__main__":
    main()
