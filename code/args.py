from argparse import ArgumentParser
from typing import Callable


def run(num: int, func: Callable[[], int], kind: str = "2"):
    parser = ArgumentParser()
    parser.add_argument("n", type=int, help="The number of values to print")
    parser.add_argument("p", type=int, help="The number of players", default=2, nargs="?")
    args = parser.parse_args()
    print(
        f"The Thue-Morse sequence for {kind} Players{'' if kind == '2' else f' ({args.p} selected)'}, Definition {num}, up to {args.n} is:",
        *(x for x, y in zip(func(args.p), range(args.n)))
    )
