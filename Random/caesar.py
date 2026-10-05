#!/bin/python3

def caesar_breaker() -> None:
    """Caesar breaker => latin alphabet print all variations"""
    print("Type the caesar code you want to break: ")
    cipher = input()
    print("----------")
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    for i in range(0,len(alphabet)):
        alphabet = alphabet[-1] + alphabet[:len(alphabet) -1]
        new_str = ""
        for j in cipher:
            new_str += alphabet[ord(j) - 97]
        print(new_str)


if __name__ == "__main__":
    caesar_breaker()
