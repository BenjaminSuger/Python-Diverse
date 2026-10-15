#!/bin/python3

import argparse


class Spider:

    def __init__(self, url: str, recursion: bool = False, depth: int = 5, path: str = "."):
        self.recursion = recursion
        self.depth = depth
        self.path = path
        self.url = url
        # queue peut etre a voir mais je pense ca va etre fait au fur et a mesure

    def __repr__(self):
        return f"r: {self.recursion}\ndepth: {self.depth}\npath: {self.path}\nurl: {self.url}"


def parsing_args() -> Spider:
    """parsing args to create a Spider instance"""
    parser = argparse.ArgumentParser(prog='Spider')
    parser.add_argument("-r", action="store_true", help="recursive download")
    parser.add_argument("-l", type=int, nargs="?", const=5, default=None, help="depth for recursive download => by default 5")
    parser.add_argument("-p", default="./data/", help="path to DL information")
    parser.add_argument("url")
    values = parser.parse_args()
    if not values.r and values.l:
        print(parser.error("-l option require -r option"))
    if values.l is None:
        values.l = 5
    return Spider(values.url, values.r, values.l, values.p)


def spider() -> None:
    """Spider will check arguments and launch an instance of spider"""
    spider = parsing_args()
    print(spider)


if __name__ == "__main__":
    try:
        spider()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
