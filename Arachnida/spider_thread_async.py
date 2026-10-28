#!/usr/bin/env python3

import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
import concurrent.futures

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
   

    def __download_images(self, soup: BeautifulSoup, link: str) -> list[str]:
        """download images from html source with 'img' balise
        download it to the self.__path given to the program or default './data/'"""
        result = []
        for i in soup.find_all('img'):
            try:
                path = urlparse(i['src']).path
                ext = os.path.splitext(path)[1].lower()
                if ext in self.__extensions:
                    url = urljoin(link, i['src'])
                    result.append(url)
                    #img_data = requests.get(url, timeout=10).content
                    #name = os.path.basename(urlparse(url).path)
                    #with open(os.path.join(self.__path, name), 'wb') as handler:
                    #    handler.write(img_data)
            except Exception:
                pass
        return result


    def __find_links(self, soup: BeautifulSoup, link: str) -> list:
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
            if not url in result:
                result.append(url)
        return result


    def crawl(self) -> None:
        """crawl with the right level of depth use threads"""
        actual_depth = 0
        visited = set()
        visited.add(self.__url)
        to_visit = [self.__url]
        with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
            to_download = set()
            while to_visit:
                output = list(executor.map(self.simple, to_visit))
                result = []
                for i in output:
                    result.extend(i[0])
                    to_download.update(i[1])
                visited.update(to_visit)     
                to_visit.clear()
                actual_depth += 1
                if actual_depth >= self.__depth:
                    break
                for i in result:
                    if i in visited:
                        continue
                    if i in to_visit:
                        continue
                    if urlparse(i).hostname != urlparse(self.__url).hostname:
                        continue
                    to_visit.append(i)
        print("-----")
        for i in to_download:
            print(i)


    def simple(self, link: str) -> list:
        """get the images in the following format ;
        .jpg/ .jpeg /  .png / .gif / .bmp
        return a list of links for further depth level"""
        try:
            html = requests.get(link, timeout = 5)
            print(link)
        except Exception:
            return []
        soup = BeautifulSoup(html.content, 'html.parser')
        return [self.__find_links(soup, link), self.__download_images(soup, link)]


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
