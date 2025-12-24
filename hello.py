import argparse


def make_message(name: str) -> str:
    return f"Hello, {name}!"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple hello CLI")
    parser.add_argument("name", nargs="?", default="world", help="Name to greet")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    print(make_message(args.name))

if __name__ == "__main__":
    main()