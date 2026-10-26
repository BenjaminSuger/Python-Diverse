#!/usr/bin/env python3

import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag

'''
https://example.com/ => sans image a trouve
https://books.toscrape.com/ => plein d'images
https://www.scrapethissite.com/ => pas tant d'images mais au moins des liens un peu
https://realpython.github.io/fake-jobs/ => un cas un peu complexe je trouve sur les images peut etre
https://quotes.toscrape.com/
'''

class Spider:

    def __init__(self, url: str, recursion: bool = False, depth: int = 5, path: str = "."):
        self.__recursion = recursion
        self.__depth = depth if recursion else 0
        if self.__depth < 0:
            raise Exception("Depth need to be positive and superior to 0")
        self.__path = path
        self.__url = url
        self.__extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']


    def __repr__(self) -> str:
        return f"r: {self.__recursion}\ndepth: {self.__depth}\npath: {self.__path}\nurl: {self.__url}"
   

    def __download_images(self, soup: BeautifulSoup, link: str) -> None:
        """download images from html source with 'img' balise
        download it to the self.__path given to the program or default './data/'"""
        for i in soup.find_all('img'):
            try:
                path = urlparse(i['src']).path
                ext = os.path.splitext(path)[1].lower()
                if ext in self.__extensions:
                    url = urljoin(link, i['src'])
                    img_data = requests.get(url, timeout=10).content
                    name = os.path.basename(urlparse(url).path)
                    with open(os.path.join(self.__path, name), 'wb') as handler:
                        handler.write(img_data)
            except Exception:
                pass


    def __find_links(self, soup: BeautifulSoup, link: str, depth: int) -> list[tuple]:
        """find links with "a" balise and href, return a list of tuple (link, depth level)
        no duplicate and do not include the starting link"""
        result = []
        for i in soup.find_all("a", href=True):
            href = i["href"]
            if href.startswith(("mailto:", "javascript:", "tel:", "#")):
                continue
            url, _ = urldefrag(urljoin(link, href))
            if url == link:
                continue
            if not (url, depth) in result:
                result.append((url, depth))
        return result


    def crawl(self) -> None:
        """crawl with the right level of depth"""
        actual_depth = 0
        visited = set() 
        to_visit = [(self.__url, actual_depth)]
        while to_visit:
            actual = to_visit.pop(0)
            visited.add(actual)
            print(actual)
            new_links = self.simple(actual[0], actual[1])
            for i in new_links:
                if i[1] >= self.__depth:
                    continue
                if i[0] in [x[0] for x in visited]:
                    continue
                if i[0] in [x[0] for x in to_visit]:
                    continue
                if urlparse(i[0]).hostname !=  urlparse(self.__url).hostname:
                    continue
                to_visit.append(i)


    def simple(self, link: str, depth: int) -> list[tuple]:
        """get the images in the following format ;
        .jpg/ .jpeg /  .png / .gif / .bmp
        return a list of links for further depth level"""
        try:
            html = requests.get(link, timeout = 5)
        except Exception:
            return []
        soup = BeautifulSoup(html.content, 'html.parser')
        self.__download_images(soup, link)
        return self.__find_links(soup, link, depth + 1)


    def hunt(self) -> None:
        """spider hunt download the data"""
        try:
            os.makedirs(self.__path, exist_ok=True)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            print("Spider killed")
            return
        self.crawl()


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


def main() -> None:
    """Spider will check arguments and launch an instance of spider"""
    spider = parsing_args()
    spider.hunt()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
