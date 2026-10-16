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
        self.__recursion = recursion
        self.__depth = depth
        self.__path = path
        self.__url = url
        self.__extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']


    def __repr__(self) -> str:
        return f"r: {self.__recursion}\ndepth: {self.__depth}\npath: {self.__path}\nurl: {self.__url}"
   

    def __download_images(self, soup: bs4.BeautifulSoup, link: str) -> None:
        for i in soup.find_all('img'):
            path = urlparse(i['src']).path
            ext = os.path.splitext(path)[1].lower()
            if ext in self.__extensions:
                url = urljoin(link, i['src'])
                img_data = requests.get(url).content
                name = os.path.basename(urlparse(url).path)
                print(f"file {name} downloaded")
                with open(self.__path + name, 'wb') as handler:
                    handler.write(img_data)


    def crawl(self, origin: str) -> None:
        """crawl with the right level of depth"""
        visited = [] # peut etre des () pour le level of depth
        to_visit = []
        # on call simple dans une boucle qui remplit les to_visit
        pass


    def simple(self, link: str) -> list[str]:
        """get the images in the following format ;
        .jpg/ .jpeg /  .png / .gif / .bmp
        return a list of links for further depth level"""
        html = requests.get(link)
        soup = BeautifulSoup(html.content, 'html.parser')
        self.__download_images(soup, link)
        # maintenant ca va etre le return des links
        for i in soup.find_all("a", href=True):
            print(i['href'])


    def hunt(self) -> None:
        """spider hunt download the data"""
        try:
            os.makedirs(self.__path, exist_ok=True)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            print("Spider killed")
            return
        #temporaire c'est juste un simple
        result = self.simple(self.__url) 







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
