#!/bin/python3

import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

'''
https://example.com/ => sans image a trouve
https://books.toscrape.com/ => plein d'images
https://www.scrapethissite.com/ => pas tant d'images mais au moins des liens un peu
https://realpython.github.io/fake-jobs/ => un cas un peu complexe je trouve sur les images peut etre
'''

class Spider:

    def __init__(self, url: str, recursion: bool = False, depth: int = 5, path: str = "."):
        self.recursion = recursion
        self.depth = depth
        self.path = path
        self.url = url

    def __repr__(self) -> str:
        return f"r: {self.recursion}\ndepth: {self.depth}\npath: {self.path}\nurl: {self.url}"
   
    def crawl(self, origin: str) -> None:
        """crawl with the right level of depth"""
        visited = [] # peut etre des () pour le level of depth
        to_visit = []
        # on call simple dans une boucle qui remplit les to_visit
        pass


    def simple(self, link: str) -> list[str]:
        """get the images in the following format ;
        .jpg/ .jpeg /  .png / .gif / .bmp
        return a list of linked for further depth level"""
        html = requests.get(link)
        soup = BeautifulSoup(html.content, 'html.parser')
        images = soup.find_all('img')
        for i in images:
            print(urljoin(link, i['src']))
            


    def hunt(self) -> None:
        """spider hunt download the data"""
        # d'abord on cree le dossier et check que c'est possible autre erreur a gerer plus tard sur les images et les mettres au bon endroit
        try:
            os.mkdir(self.path)
        except FileExistsError:
            #print(f"{self.path} already existing, re using this")
            pass
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            print("Spider killed")
            return
        #ensuite on va faire simple() deja pour une page mais sinon on devait faire crawl() qui va gerer
        result = self.simple(self.url) 








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
    spider.hunt()


if __name__ == "__main__":
    try:
        spider()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
