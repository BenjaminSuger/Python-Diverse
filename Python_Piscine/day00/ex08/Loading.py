import os # temporaire 
import time

def ft_tqdm(lst: range) -> None:
    pass


if __name__ == "__main__":
    columns = os.get_terminal_size().columns - 6 # minus 6 for the first char
    value = 0
    for percentage in range(0, 101):
        print(f"\r{percentage:>3}% |" + (columns * "a"), end='')
        time.sleep(0.05)
    

    
