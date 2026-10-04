#!/usr/bin/env python3


def secure_archive(filename: str, action: str = "read", content: str = ""
                   ) -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, "Invalid action")
    try:
        with open(filename, action) as f:
            if action == "r":
                data = f.read()
            elif action == "w":
                f.write(content)
                data = "Content successfully written to file"
        return (True, data)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    msg = "Using 'secure_archive' to"

    print(f"{msg} read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'r'))

    print(f"\n{msg} read from an inaccessible file:")
    print(secure_archive('/etc/shadow', 'r'))

    print(f"\n{msg} read from a regular file:")
    print(secure_archive('test', 'r'))

    print(f"\n{msg} write previous content to a new file:")
    print(secure_archive('newfile', 'w', 'some\ntext\nto\ntest\n'))


if __name__ == "__main__":
    main()
