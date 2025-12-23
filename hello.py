import sys

def make_message(name: str) -> str:
    return f"Hello, {name}!"

def main():
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = "world"

    print(make_message(name))

if __name__ == "__main__":
    main()