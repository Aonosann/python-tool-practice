import argparse


def make_message(name: str) -> str:
    return f"Hello, {name}!"


def positive_int(value: str) -> int:
    n = int(value)
    if n < 1:
        raise argparse.ArgumentTypeError("--times must be >= 1")
    return n


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple hello CLI")
    parser.add_argument("name", nargs="?", default="world", help="Name to greet")
    parser.add_argument(
        "--times",
        type=positive_int,
        default=1,
        help="Number of times to greet (>= 1)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    for _ in range(args.times):
        print(make_message(args.name))


if __name__ == "__main__":
    main()